from django.contrib.auth.models import User
from django.shortcuts import render
from .models import OpenDonasi
import json

from django.shortcuts import render
from . import forms

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse

from .forms import OpenDonasiForm
# ======================================================================================


# Create your views here.
@login_required(login_url='/login')
def show_page(request):
    return render(request,'form_buat_donasi.html')


@csrf_exempt
def show_json_user(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.user.username)
        data = OpenDonasi.objects.filter(user=user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else:
        return JsonResponse({'status': 'failed', 'message': 'Method not allowed'})
        
def show_json(request):
    data = OpenDonasi.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def ajax_submit(request):
    form = forms.OpenDonasiForm()
    if (request.method == 'POST'):
        user = request.user
        organization = user.userprofile.organization
        
        data = {}
        form = forms.OpenDonasiForm(request.POST or None)
        if (form.is_valid() & organization):
            tema_kegiatan = form.cleaned_data['tema_kegiatan']
            deskripsi = form.cleaned_data['deskripsi']
            target_donasi = form.cleaned_data['target_donasi']
            new_data = OpenDonasi.objects.create(user=user, pencetus_donasi = user.userprofile.name, username = user.username , tema_kegiatan=tema_kegiatan, target_donasi=target_donasi, total_donasi_terkumpul=0, deskripsi=deskripsi)
            data["tema_kegiatan"] = tema_kegiatan
            data["tanggal_pembuatan"] = new_data.tanggal_pembuatan
            data["deskripsi"] = new_data.deskripsi
            data["pencetus_donasi"] = new_data.pencetus_donasi
            data["target_donasi"] = new_data.target_donasi
            data["total_donasi_terkumpul"] = new_data.total_donasi_terkumpul
            data["pk"] = new_data.pk
            
            new_data.save()
            
        # else:
        #     messages.info(request, 'Untuk dapat membuat forum donasi, akun harus merupakan akun organisasi!!!')
        return JsonResponse(data)
        

def berdonasi(request, id):
    return redirect('berdonasi:show_masukkan_nominal', id=id)


@csrf_exempt
def add_donasi_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_data = OpenDonasi(user=request.user, pencetus_donasi = request.user.userprofile.name, username = request.user.username, tema_kegiatan=data['tema_kegiatan'], target_donasi=int(data['target_donasi']), total_donasi_terkumpul=0, deskripsi=data['deskripsi'])
        new_data.save()
    return JsonResponse({"status" : "success"}, status = 200)

@csrf_exempt
def delate_event(request, pk):
    if request.method == "POST":
        obj = OpenDonasi.objects.filter(id=pk)
        obj.delete()
        return JsonResponse({"status" : "success"}, status = 200)

@csrf_exempt
def edit_event_flutter(request, pk):
    if request.method == "POST":
        data = json.loads(request.body)
        event = OpenDonasi.objects.get(id=pk)
        event.tema_kegiatan = data['tema_kegiatan']
        event.deskripsi = data['deskripsi']
        event.target_donasi = int(data['target_donasi'])
        event.save()
       
        return JsonResponse({"status" : "success"}, status = 200)
