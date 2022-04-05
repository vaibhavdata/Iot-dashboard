from django.urls import path,include
from . import views
urlpatterns = [
    path('home',views.home,name='home'),
    path('device/<slug:slug>/', views.device_detail, name='device_detail'),
    path('device_add',views.device_add,name='device_add'),
    path('delete_device/<slug:slug>/',views.delete_device,name='delete_device')
]
