from django.shortcuts import render
import pyrebase

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


# inner page jumping
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
def login(request):
    return render(request, 'login.html')