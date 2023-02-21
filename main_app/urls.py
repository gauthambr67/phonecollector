from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name = 'about'),
path('phones/', views.phones_index, name = 'index'),
path('phones/<int:phone_id>/', views.phones_detail, name='detail'),
path('phones/create/', views.PhoneCreate.as_view(), name='phones_create'),
path('phones/<int:pk>/update/', views.PhoneUpdate.as_view(), name='phones_update'),
path('phones/<int:pk>/delete/', views.PhoneDelete.as_view(), name='phones_delete'),
path('phones/<int:phone_id>/add_charging/', views.add_charging, name='add_charging'),
path('phones/<int:phone_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
path('phones/<int:phone_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),
path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
path('phones/<int:phone_id>/add_photo/', views.add_photo, name='add_photo'),
path('accounts/signup/', views.signup, name='signup'),
]
