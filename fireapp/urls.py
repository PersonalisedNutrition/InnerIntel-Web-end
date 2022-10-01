from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('client/', views.client, name='client'),
    path('client/appointment/', views.client_appointment, name='client_appointment'),
    path('client/data/', views.client_data, name='client_data'),
    path('client/note/', views.client_note, name='client_note'),
    path('client/profile/', views.client_profile, name='client_profile'),
    path('message/', views.message, name='message'),
    path('setting/', views.setting, name='setting'),

    # urls in Login Page
    path('login/user/', views.login, name='login_user'),
    path('setting/user/', views.setting, name='setting_user'),

]
