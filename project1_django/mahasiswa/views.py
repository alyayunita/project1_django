from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MahasiswaForm
from .models import Mahasiswa


# ➤ Tambah data
@login_required(login_url='/admin/login/')
def input_mahasiswa(request):
    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa:input_mahasiswa')
    else:
        form = MahasiswaForm()

    semua_mahasiswa = Mahasiswa.objects.all().order_by('id')

    return render(request, 'mahasiswa/input.html', {
        'form': form,
        'semua_mahasiswa': semua_mahasiswa,
        'edit_mode': False,
    })


# ➤ Edit data
@login_required(login_url='/admin/login/')
def edit_mahasiswa(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)

    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mhs)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa:input_mahasiswa')
    else:
        form = MahasiswaForm(instance=mhs)

    return render(request, 'mahasiswa/edit.html', {
        'form': form,
        'edit_mode': True,
    })


# ➤ Hapus data
@login_required(login_url='/admin/login/')
def delete_mahasiswa(request, id):
    mhs = get_object_or_404(Mahasiswa, id=id)
    mhs.delete()
    return redirect('mahasiswa:input_mahasiswa')
