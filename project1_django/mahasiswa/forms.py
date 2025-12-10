# ...existing code...
from django import forms
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
    JURUSAN_CHOICES = [
        ('Teknik Informatika', 'Teknik Informatika'),
        ('Sistem Informasi', 'Sistem Informasi'),
        ('Teknik Komputer', 'Teknik Komputer'),
        ('Manajemen Informatika', 'Manajemen Informatika'),
    ]

    jurusan = forms.ChoiceField(
        choices=JURUSAN_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Jurusan"
    )

    class Meta:
        model = Mahasiswa
        fields = ['nama', 'npm', 'email', 'no_hp', 'alamat', 'jurusan']  # ← jurusan ditambahkan

        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama mahasiswa'
            }),
            'npm': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan NPM'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan email mahasiswa'
            }),
            'no_hp': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nomor HP'
            }),
            'alamat': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan alamat',
                'rows': 3
            }),
        }

        labels = {
            'nama': 'Nama Lengkap',
            'npm': 'NPM',
            'email': 'Email',
            'no_hp': 'No. HP', # untuk tambahkan tabel
            'alamat': 'Alamat',
            'jurusan': 'Jurusan',
        }
