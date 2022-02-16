from django.db import models
import constants


class Component(models.Model):
    name = models.CharField("Название", max_length=255)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    component = models.CharField("Компонент", max_length=2, choices=constants.COMPONENTS)

    def __str__(self):
        return self.name

