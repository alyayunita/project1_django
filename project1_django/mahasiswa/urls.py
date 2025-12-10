from django.urls import path
from . import views

app_name = 'mahasiswa'   # ← Tetap dipakai

urlpatterns = [
    path('input/', views.input_mahasiswa, name='input_mahasiswa'),
    path('hapus/<int:id>/', views.delete_mahasiswa, name='delete_mahasiswa'),
    path('edit/<int:id>/', views.edit_mahasiswa, name='edit_mahasiswa'),
]
