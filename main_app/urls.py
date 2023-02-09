from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name = 'about'),
path('phones/', views.phones_index, name = 'index'),
path('phones/<int:phone_id>/', views.phones_detail, name='detail'),
path('phones/create/', views.PhoneCreate.as_view(), name='phones_create'),
path('phones/<int:pk>/update/', views.PhoneUpdate.as_view(), name='phones_update'),
path('phones/<int:pk>/delete/', views.PhoneDelete.as_view(), name='phones_delete')
]
