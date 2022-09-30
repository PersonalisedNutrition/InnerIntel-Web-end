from django.shortcuts import render
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
    return render(request, 'index.html')


# manipulate database

# check the pwd by email
def check_pwd(input_email, input_pwd):
    user = database.child('Users').order_by_child('email').equal_to(input_email).get()
    if user.val():
        return list(user.val().items())[0][1].get('pwd') == input_pwd
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

        if check_pwd(login_email, login_pwd):
            return render(request, 'index.html')
        # if the email and pwd can not match
        else:
            error_msg = 'Wrong email or password'
            return render(request, 'login.html', {'error_msg': error_msg})
    # If the request type is GET, just jump to the login page.
    else:
        return render(request, "login.html", {'error_msg': error_msg})


def client(request):
    return render(request, 'client.html')


def client_data(request):
    return render(request, 'client_data.html')


def client_appointment(request):
    return render(request, 'client_appointment.html')


def client_note(request):
    return render(request, 'client_note.html')


def client_profile(request):
    return render(request, 'client_profile.html')


def message(request):
    return render(request, 'message.html')


def setting(request):
    return render(request, 'setting.html')
