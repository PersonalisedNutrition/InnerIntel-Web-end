import datetime
import json

from django.shortcuts import render, redirect
import pyrebase

# Import this library for pop-up alert messages
from django.contrib import messages

firebaseConfig = {
    "apiKey": "AIzaSyBr78-kuY_PVb-qXc8ka2iDce88mLXrj5k",
    "authDomain": "innerintel-4e391.firebaseapp.com",
    "databaseURL": "https://innerintel-4e391-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "innerintel-4e391",
    "storageBucket": "innerintel-4e391.appspot.com",
    "messagingSenderId": "1070596195661",
    "appId": "1:1070596195661:web:fa472958c98f63446da304",
    "measurementId": "G-5BP9RC7EXY"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()


def get_client_list(clients_list):
    print(clients_list)
    out_client = []
    for cli in clients_list:
        # print(cli)
        new_client = []
        for k, v in cli.items():
            new_client.append(v)
        # correct time format
        new_client[3] = new_client[3].replace('/', '-')
        # swap
        change = new_client[2]
        new_client[2] = new_client[1]
        new_client[1] = change
        out_client.append(new_client)
        # print(out_client)
    return out_client


def index(request):
    if request.method == "POST":
        pass
    else:
        username = request.get_signed_cookie("username")
        email = request.get_signed_cookie('email')
        user = database.child('Nutritionist').order_by_child('email').equal_to(email).get()
        clients_list = list(user.val().items())[0][1].get('clients_list')
        out_client = get_client_list(clients_list)
        return render(request, 'index.html', {'out_client': out_client, "username": username})


# manipulate database

# check the pwd by email
def check_pwd(input_email, input_pwd):
    user = database.child('Nutritionist').order_by_child('email').equal_to(input_email).get()
    if user.val():
        # print(list(user.val().items())[0][1].get('clients_list'))
        return list(user.val().items())[0][1].get('first_name'), \
               list(user.val().items())[0][1].get('last_name'), \
               list(user.val().items())[0][1].get('email'), \
               list(user.val().items())[0][1].get('clients_list'), \
               list(user.val().items())[0][1].get('pwd') == input_pwd

    else:
        return False


#  views functions
def login(request):
    # check the request type, if the type is POST,
    # check the user email and pwd.
    error_msg = ""
    if request.method == "POST":
        login_email = request.POST.get('input_email')
        login_pwd = request.POST.get('input_pwd')
        # check if the email and pwd can match the Database
        first_name, last_name, email, client_list, state = check_pwd(login_email, login_pwd)
        if state:
            # put the login username to cookies
            username = first_name + " " + last_name
            dic = {'username': username, 'email': email, 'client_list': client_list}
            out_client = get_client_list(client_list)
            response = render(request, "index.html", {'out_client': out_client, 'username': username})
            response.set_signed_cookie("username", username)
            response.set_signed_cookie("email", email)
            response.set_signed_cookie("client_list", client_list)
            return response
        # if the email and pwd can not match
        else:
            error_msg = 'Wrong email or password'
            return render(request, 'login.html', {'error_msg': error_msg})
    # If the request type is GET, just jump to the login page.
    else:
        return render(request, "login.html", {'error_msg': error_msg})


# get the value of input key in an OrderedDict
def get_value(ordered_dict, key):
    return ordered_dict.val().get(key)


# get client data from database by cid
def get_client_data(cid):
    client_data = database.child('Client').child(cid).get()

    client_first_name = get_value(client_data, 'first_name')
    client_last_name = get_value(client_data, 'last_name')
    client_gender = get_value(client_data, 'gender')
    client_height = get_value(client_data, 'height')
    client_weight = get_value(client_data, 'weight')
    client_dob = get_value(client_data, 'dob')

    # make the data reading code more robust with if
    client_medical_con = get_value(client_data, 'medical_conditions')
    if client_medical_con:
        client_medical_con = client_medical_con.split(",")
    client_medication = get_value(client_data, 'medication')
    if client_medication:
        client_medication = client_medication.split(",")
    return client_first_name, client_last_name, client_gender, \
           client_weight, client_height, client_medication, client_medical_con, client_dob


def get_age(birthday):
    # This function returns the age as of that date based on the 8-digit date of birth data entered
    today = str(datetime.datetime.now().strftime('%Y-%m-%d')).split("-")
    # Fetch the year, month and day data of the system for the day as a list [year, month, day]
    n_monthandday = today[1] + today[2]
    # Linking the months and days together
    n_year = today[0]
    # Separate current year
    r_monthandday = birthday[4:]
    # Fetch the month and day of the entered date
    r_year = birthday[:4]
    # Fetch the year of the entered date
    if (int(n_monthandday) >= int(r_monthandday)):
        r_age = int(n_year) - int(r_year)
    else:
        r_age = int(n_year) - int(r_year) - 1
    return r_age


def client(request):
    # get cid of client and fetch the data of client
    cid = request.GET.get('cid')
    client_first_name, client_last_name, client_gender, \
    client_weight, client_height, client_medication, client_medical_con, client_dob \
        = get_client_data(cid)
    client_age = get_age(client_dob)
    username = request.get_signed_cookie('username')
    response = render(request, 'client.html', {'username': username, 'client_first_name': client_first_name,
                                               'client_last_name': client_last_name, 'client_gender': client_gender,
                                               'client_weight': client_weight, 'client_height': client_height,
                                               'client_medication': client_medication,
                                               'client_medical_con': client_medical_con,
                                               'client_age': client_age})
    response.set_signed_cookie("cid", cid)
    return response


def client_appointment(request):
    username = request.get_signed_cookie('username')
    return render(request, 'client_appointment.html', {'username': username})


def client_note(request):
    username = request.get_signed_cookie('username')
    return render(request, 'client_note.html', {'username': username})


def client_profile(request):
    username = request.get_signed_cookie('username')
    return render(request, 'client_profile.html', {'username': username})


def message(request):
    username = request.get_signed_cookie('username')
    return render(request, 'message.html', {'username': username})


def update_client_setting(email, first_name, last_name, phone, password):
    user = database.child('Nutritionist').order_by_child('email').equal_to(email).get()
    nid = list(user.val().items())[0][1].get('nid')
    print(nid)
    if user.val():
        database.child('Nutritionist').child(nid).update(
            {"first_name": first_name, 'last_name': last_name, 'phone': phone, 'password': password})
        return True
    else:
        return False


def find_information(email):
    user = database.child('Nutritionist').order_by_child('email').equal_to(email).get()
    firstname = list(user.val().items())[0][1].get('first_name')
    lastname = list(user.val().items())[0][1].get('last_name')
    phone = list(user.val().items())[0][1].get('phone')
    password = list(user.val().items())[0][1].get('pwd')
    email = list(user.val().items())[0][1].get('email')
    return {'email': email, 'first_name': firstname, 'last_name': lastname, 'phone': phone, 'password': password}


def setting(request):
    username = request.get_signed_cookie('username')
    email = request.get_signed_cookie('email')
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if update_client_setting(email, first_name, last_name, phone, password):
            find_info = find_information(email)
            msg = 'Update Successful!'
            find_info['msg'] = msg
            find_info['username'] = first_name + " " + last_name
            response = render(request, "setting.html", find_info)
            response.set_signed_cookie("email", email)
            response.set_signed_cookie("username", find_info['username'])
            return response
        else:
            msg = 'Failed to update'
            return render(request, "setting.html", {'msg': msg, 'username': username})
    else:
        find_info = find_information(email)
        find_info['username'] = username
        return render(request, 'setting.html', find_info)


# get client logs from database by cid
def get_client_logs(cid):
    # logs = database.child('LOGS').order_by_child('cid').equal_to(1).get()
    client_logs = []
    logs = database.child('LOGS').get()
    for log in logs.each():
        if log.val().get('cid') == int(cid):
            client_logs.append(log.val())
    return client_logs


def client_data(request):
    cid = request.get_signed_cookie('cid')
    username = request.get_signed_cookie('username')
    logs = get_client_logs(cid)
    if request.method == "POST":
        print("**** client_data POST ****")
        changes_list = request.POST.get('changes_list')
        changes_list = json.loads(changes_list)
        logsDB = database.child('LOGS').get()
        if changes_list:
            for change in changes_list:
                print(change['lid'])
                for log in logsDB.each():
                    if log.val().get('lid') == int(change['lid']):
                        database.child('LOGS').child(log.key()).update(change)
        response = render(request, "client_data.html", {'username': username, 'logs': logs, 'cid': cid})
        return response
    else:
        return render(request, 'client_data.html', {'username': username, 'logs': logs, 'cid': cid})


# def update_client_data(ad_hoc,client_drink_input,client_food_break_out,client_food_input,cooking_fats_added_denominator,cooking_fats_added_numerator,
#                        cooking_method,date,discomfort_daily,discomfort_descriptor,discomfort_incidental,drink_input_breakout,drink_size_denominator,
#                        drink_size_numerator,drink_tags_breakout,exercise_duration,exercise_type,faeces,flag,flatulence_daily,flatulence_incidental,
#                        food_tags_breakout,lid,location,meal_type,mental_state_mood,photograph,portion_measurement_unit,portion_size,reflux_daily,
#                        reflux_incidental,sleep_notes,sleep_quality,sleep_quantity,time,vomiting_daily,vomiting_incidental,weight):
#     client_data = database.child('LOGS').order_by_child('lid').equal_to(lid).get()
#     if client_data.val():
#         database.child('LOGS').child(lid).update(
#             {'ad_hoc':ad_hoc,'client_drink_input':client_drink_input,'client_food_break_out':client_food_break_out,'client_food_input':client_food_input,
#              'cooking_fats_added_denominator':cooking_fats_added_denominator,'cooking_fats_added_numerator':cooking_fats_added_numerator,'cooking_method':
#              cooking_method,'date':date,'discomfort_daily':discomfort_daily,'discomfort_descriptor':discomfort_descriptor,'discomfort_incidental':discomfort_incidental,
#              'drink_input_breakout':drink_input_breakout,'drink_size_denominator':drink_size_denominator,'drink_size_numerator':drink_size_numerator,
#              'drink_tags_breakout':drink_tags_breakout,'exercise_duration':exercise_duration,'exercise_type':exercise_type,'faeces':faeces,'flag':flag,
#              'flatulence_daily':flatulence_daily,'flatulence_incidental':flatulence_incidental,'food_tags_breakout':food_tags_breakout,'location':location,
#              'meal_type':meal_type,'mental_state_mood':mental_state_mood,'photograph':photograph,'portion_measurement_unit':portion_measurement_unit,
#              'portion_size':portion_size,'reflux_daily':reflux_daily,'reflux_incidental':reflux_incidental,'sleep_notes':sleep_notes,'sleep_quality':sleep_quality,
#              'sleep_quantity':sleep_quantity,'time':time,'vomiting_daily':vomiting_daily,'vomiting_incidental':vomiting_incidental,'weight':weight}
#         )
#         return True
#     else:
#         return False



# def get_logs_data(cid):
#     logs_data = get_client_logs(cid)
#     logs_ad_hoc = []
#     logs_cid = []
#     logs_drink_input = []
#     logs_food_break_out = []
#     logs_food_input = []
#     logs_cooking_fats_added_denominator = []
#     logs_cooking_fats_added_numerator = []
#     logs_cooking_method = []
#     logs_date = []
#     logs_discomfort_daily = []
#     logs_discomfort_incidental = []
#     logs_drink_size_numerator = []
#     logs_drink_input_breakout = []
#     logs_drink_size_denominator = []
#     logs_drink_tags_breakout = []
#     logs_exercise_duration = []
#     logs_exercise_type = []
#     logs_faeces = []
#     logs_flag = []
#     logs_flatulence_daily = []
#     logs_flatulence_incidental = []
#     logs_food_tags_breakout = []
#     logs_lid = []
#     logs_location = []
#     logs_meal_type = []
#     logs_mental_state_mood = []
#     logs_photograph = []
#     logs_portion_measurement_unit = []
#     logs_portion_size = []
#     logs_reflux_daily = []
#     logs_reflux_incidental = []
#     logs_sleep_notes = []
#     logs_sleep_quality = []
#     logs_sleep_quantity = []
#     logs_time = []
#     logs_vomiting_daily = []
#     logs_vomiting_incidental = []
#     logs_weight = []
#     for ele in logs_data:
#         logs_ad_hoc.append(get_value(ele, 'ad_hoc'))
#         logs_cid.append(get_value(ele, 'cid'))
#         logs_drink_input.append(get_value(ele, 'client_drink_input'))
#         logs_food_break_out.append(get_value(ele, 'client_food_break_out'))
#         logs_food_input.append(get_value(ele, 'client_food_input'))
#         logs_cooking_fats_added_denominator.append(get_value(ele, 'cooking_fats_added_denominator'))
#         logs_cooking_fats_added_numerator.append(get_value(ele, 'cooking_fats_added_numerator'))
#         logs_cooking_method.append(get_value(ele, 'cooking_method'))
#         logs_date.append(get_value(ele, 'date'))
#         logs_discomfort_daily.append(get_value(ele, 'discomfort_daily'))
#         logs_discomfort_incidental.append(get_value(ele, 'discomfort_incidental'))
#         logs_drink_size_numerator.append(get_value(ele, 'drink_size_numerator'))
#         logs_drink_input_breakout.append(get_value(ele, 'drink_input_breakout'))
#         logs_drink_size_denominator.append(get_value(ele, 'drink_size_denominator'))
#         logs_drink_tags_breakout.append(get_value(ele, 'drink_tags_breakout'))
#         logs_exercise_duration.append(get_value(ele, 'exercise_duration'))
#         logs_exercise_type.append(get_value(ele, 'exercise_type'))
#         logs_faeces.append(get_value(ele, 'faeces'))
#         logs_flag.append(get_value(ele, 'exercise_type'))
#         logs_flatulence_daily.append(get_value(ele, 'flatulence_daily'))
#         logs_flatulence_incidental.append(get_value(ele, 'flatulence_incidental'))
#         logs_food_tags_breakout.append(get_value(ele, 'food_tags_breakout'))
#         logs_lid.append(get_value(ele, 'lid'))
#         logs_location.append(get_value(ele, 'location'))
#         logs_meal_type.append(get_value(ele, 'meal_type'))
#         logs_mental_state_mood.append(get_value(ele, 'mental_state_mood'))
#         logs_photograph.append(get_value(ele, 'photograph'))
#         logs_portion_measurement_unit.append(get_value(ele, 'portion_measurement_unit'))
#         logs_portion_size.append(get_value(ele, 'portion_size'))
#         logs_reflux_daily.append(get_value(ele, 'reflux_daily'))
#         logs_reflux_incidental.append(get_value(ele, 'reflux_incidental'))
#         logs_sleep_notes.append(get_value(ele, 'sleep_notes'))
#         logs_sleep_quality.append(get_value(ele, 'sleep_quality'))
#         logs_sleep_quantity.append(get_value(ele, 'sleep_quantity'))
#         logs_time.append(get_value(ele, 'time'))
#         logs_vomiting_daily.append(get_value(ele, 'vomiting_daily'))
#         logs_vomiting_incidental.append(get_value(ele, 'vomiting_incidental'))
#         logs_weight.append(get_value(ele, 'weight'))
#
#     return logs_ad_hoc, logs_cid, logs_drink_input, logs_food_break_out, logs_food_input, logs_cooking_fats_added_denominator, \
#            logs_cooking_fats_added_numerator, logs_cooking_method, logs_date, logs_discomfort_daily, logs_discomfort_incidental, \
#            logs_drink_size_numerator, logs_drink_input_breakout, logs_drink_size_denominator, logs_drink_tags_breakout, logs_exercise_duration, \
#            logs_exercise_type, logs_faeces, logs_flag, logs_flatulence_daily, logs_flatulence_incidental, logs_food_tags_breakout, logs_lid, \
#            logs_location, logs_meal_type, logs_mental_state_mood, logs_photograph, logs_portion_measurement_unit, logs_portion_size, logs_reflux_daily, \
#            logs_reflux_incidental, logs_sleep_notes, logs_sleep_quality, logs_sleep_quantity, logs_time, logs_vomiting_daily, logs_vomiting_incidental, \
#            logs_weight
#
#
