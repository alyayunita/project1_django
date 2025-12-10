from django.db import models

class Mahasiswa(models.Model):

    JURUSAN_CHOICES = [
        ('Teknik Informatika', 'Teknik Informatika'),
        ('Sistem Informasi', 'Sistem Informasi'),
        ('Teknik Komputer', 'Teknik Komputer'),
        ('Manajemen Informatika', 'Manajemen Informatika'),
    ]

    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=20)
    email = models.EmailField()
    no_hp = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.CharField(max_length=255, blank=True, null=True)

    # ✅ Field jurusan ditambahkan
    jurusan = models.CharField(
        max_length=50,
        choices=JURUSAN_CHOICES,
        default='Teknik Informatika'
    )

    def __str__(self):
        return f"{self.nama} ({self.npm})"
