from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('mahasiswa/input/')),
    path('admin/', admin.site.urls),
    path('mahasiswa/', include('mahasiswa.urls')),
]
