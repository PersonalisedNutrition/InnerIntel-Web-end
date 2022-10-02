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


def index(request):
    logs_dataset = database.child('logs').get()
    sleepLogs_dataset = database.child('sleepLogs').get()

    # update数据
    # test = database.child('logs').child('0').update({"table_id": "10test"})
    # print(test.val())

    # print(logs_dataset.val()[0])
    # print(sleepLogs_dataset.val())

    context = {
        # 'first_name': first_name,
        # 'last_name': last_name,
        # 'gender': gender,
        # 'ip_address': ip_address
    }
    username = request.get_signed_cookie('username')
    return render(request, 'index.html', {'username': username})


# manipulate database

# check the pwd by email
def check_pwd(input_email, input_pwd):
    user = database.child('Nutritionist').order_by_child('email').equal_to(input_email).get()
    if user.val():
        print(list(user.val().items())[0][1].get('clients_list'))
        return list(user.val().items())[0][1].get('name'), list(user.val().items())[0][1].get('email'), \
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
        username, email, client_list, state = check_pwd(login_email, login_pwd)
        if state:
            # put the login username to cookies
            dic = {'username': username, 'email': email, 'client_list': client_list}
            response = render(request, "index.html", dic)
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


def client(request):
    username = request.get_signed_cookie('username')
    return render(request, 'client.html', {'username': username})


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
            response = render(request, "setting.html", find_info)
            response.set_signed_cookie("email", email)
            return response
        else:
            msg = 'Failed to update'
            return render(request, "setting.html", {'msg': msg})
    else:
        find_info = find_information(email)
        return render(request, 'setting.html', find_info)
