from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Phone, Accessory, Photo
from .forms import ChargingForm
import uuid
import boto3
import os
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

@login_required
def add_photo(request, phone_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3= boto3.client("s3")
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind("."):]

    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)

      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"

      Photo.objects.create(url=url, phone_id = phone_id)

    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  
  return redirect('detail', phone_id = phone_id)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def phones_index(request):
    phones = Phone.objects.filter(user=request.user)
    return render(request, 'phones/index.html', {'phones': phones})

@login_required
def phones_detail(request, phone_id):
    phone = Phone.objects.get(id= phone_id)
    id_list = phone.accessories.all().values_list('id')
    accessories_phone_doesnt_have= Accessory.objects.exclude(id__in=id_list)
    charging_form= ChargingForm()
    return render(request, 'phones/detail.html', {
       "phone": phone,
        'charging_form': charging_form, 
        'accessories': accessories_phone_doesnt_have})

class PhoneCreate(LoginRequiredMixin, CreateView):
    model= Phone
    fields = ['make', 'model', 'description', 'screen']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PhoneUpdate(LoginRequiredMixin, UpdateView):
    model = Phone
    fields = ['make', 'model', 'description', 'screen']

class PhoneDelete(DeleteView):
    model= Phone
    success_url = '/phones'


@login_required
def add_charging(request, phone_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = ChargingForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # phone_id FK.
    new_charging = form.save(commit=False)
    new_charging.phone_id = phone_id
    new_charging.save()
  return redirect('detail', phone_id=phone_id)

class AccessoryList(LoginRequiredMixin, ListView):
   model = Accessory

class AccessoryDetail(LoginRequiredMixin, DetailView):
  model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
  model = Accessory
  fields = ['name','color']

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
  model = Accessory
  success_url = '/accessories'

@login_required
def assoc_accessory(request, phone_id, accessory_id):
 
  Phone.objects.get(id=phone_id).accessories.add(accessory_id)
  return redirect('detail', phone_id=phone_id)

@login_required
def unassoc_accessory(request, phone_id, accessory_id):
  
  Phone.objects.get(id=phone_id).accessories.remove(accessory_id)
  return redirect('detail', phone_id=phone_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
  
    form = UserCreationForm(request.POST)
    if form.is_valid():
     
      user = form.save()
    
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
 
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
