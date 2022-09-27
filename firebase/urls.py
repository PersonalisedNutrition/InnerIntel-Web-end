
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # redistribute to app fireapp
    path('', include('fireapp.urls')),
    path('inner/', include('fireapp.urls')),
]
