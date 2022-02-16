from django.urls import path

from . import views

app_name = 'room_booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:booking_id>/', views.detail, name='detail'),
    path('<int:booking_id>/make_booking', views.make_booking, name='make_booking'),
]