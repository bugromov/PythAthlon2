from django.db import models
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
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    datetime_begin = models.DateTimeField("Дата начала", max_length=255)
    datetime_end = models.DateTimeField("Дата окончания", max_length=255)
    # TODO
    # booking_date = models.DateTimeField("Дата бронирования", max_length=255)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return self.meeting_room.name + ': ' + str(self.datetime_begin.strftime("%d.%m.%Y %H:%M")) + '-' + str(self.datetime_end.strftime("%H:%M"))

    def book_the_room(self, dt_begin, dt_end, room):
        self.datetime_begin = dt_begin
        self.datetime_end = dt_end
        self.meeting_room = room
        self.save()

    def get_duration(self):
        return (self.datetime_end - self.datetime_begin).total_seconds() // 60
