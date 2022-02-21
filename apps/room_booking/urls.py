from django.urls import path

from . import views

app_name = 'room_booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:booking_id>/', views.detail, name='detail'),
    path('add_booking/', views.add_booking, name='add_booking'),
]
