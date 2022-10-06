import datetime

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
        return render(request, 'index.html', {'out_client': out_client,"username":username})


# manipulate database

# check the pwd by email
def check_pwd(input_email, input_pwd):
    user = database.child('Nutritionist').order_by_child('email').equal_to(input_email).get()
    if user.val():
        # print(list(user.val().items())[0][1].get('clients_list'))
        return list(user.val().items())[0][1].get('first_name'), \
               list(user.val().items())[0][1].get('last_name'),\
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
            username = first_name+" "+last_name
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
    return render(request, 'client.html', {'username': username, 'client_first_name': client_first_name,
                                           'client_last_name': client_last_name, 'client_gender': client_gender,
                                           'client_weight': client_weight, 'client_height': client_height,
                                           'client_medication': client_medication,
                                           'client_medical_con': client_medical_con,
                                           'client_age': client_age})


def client_data(request):
    username = request.get_signed_cookie('username')
    return render(request, 'client_data.html', {'username': username})


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
            find_info['username'] = first_name+" "+last_name
            response = render(request, "setting.html", find_info)
            response.set_signed_cookie("email", email)
            response.set_signed_cookie("username",find_info['username'])
            return response
        else:
            msg = 'Failed to update'
            return render(request, "setting.html", {'msg': msg, 'username': username})
    else:
        find_info = find_information(email)
        find_info['username'] = username
        return render(request, 'setting.html', find_info)
