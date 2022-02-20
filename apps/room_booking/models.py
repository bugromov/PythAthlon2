from django.db import models
from django.contrib.auth.models import User
import constants


class MeetingRoom(models.Model):
    name = models.CharField("Название", max_length=100)
    capacity = models.IntegerField("Вместительность", default=1)

    class Meta:
        verbose_name = 'Переговорная комната'
        verbose_name_plural = 'Переговорные комнаты'

    def __str__(self):
        return self.name


class Booking(models.Model):
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE, verbose_name="Комната")
    datetime_begin = models.DateTimeField("Начало", max_length=255)
    datetime_end = models.DateTimeField("Окончание", max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    # TODO
    # booking_date = models.DateTimeField("Дата бронирования", max_length=255)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return self.meeting_room.name + ': ' \
               + str(self.datetime_begin.strftime("%d.%m.%Y %H:%M")) \
               + '-' + str(self.datetime_end.strftime("%H:%M")) + ' (' + str(self.user) + ')'

    def book_the_room(self, dt_begin, dt_end, room):
        self.datetime_begin = dt_begin
        self.datetime_end = dt_end
        self.meeting_room = room
        self.save()

    def get_duration(self):
        return (self.datetime_end - self.datetime_begin).total_seconds() // 60
