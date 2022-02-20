from django.db import models
import constants
from django.contrib.auth.models import User


class Component(models.Model):
    name = models.CharField("Название", max_length=255)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    component = models.CharField("Компонент", max_length=2, choices=constants.COMPONENTS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'

    def __str__(self):
        return self.name

