from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Phone


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def phones_index(request):
    phones = Phone.objects.all()
    return render(request, 'phones/index.html', {'phones': phones})

def phones_detail(request, phone_id):
    phone = Phone.objects.get(id= phone_id)
    return render(request, 'phones/detail.html', {"phone": phone})

class PhoneCreate(CreateView):
    model= Phone
    fields = '__all__'
    success_url = '/phones/{phone_id}'

class PhoneUpdate(UpdateView):
    model = Phone
    fields = "__all__"

class PhoneDelete(DeleteView):
    model= Phone
    success_url = '/phones'


