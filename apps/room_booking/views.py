from django.shortcuts import render
from .models import Booking, MeetingRoom
from django.http import Http404, HttpResponseRedirect


def index(request):
    current_bookings = Booking.objects.all
    return render(request, 'room_booking/list.html', {'current_bookings': current_bookings})


def detail(request, booking_id):
    try:
        b = Booking.objects.get(id=booking_id)
    except:
        raise Http404('Бронирование не найдено')
    return render(request, 'room_booking/detail.html', {'booking': b})


def make_booking(request, booking_id):
    b = Booking

