# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Ingrese 9 dígitos")
class Friend(models.Model):
    first_name = models.CharField("Nombre", max_length=100)
    last_name = models.CharField("Apellidos", max_length=100)
    phone = models.CharField("Teléfono", validators=[phone_regex], max_length=9)
    address = models.CharField("Dirección", max_length=100)
    birthday = models.DateField("Cumpleaños", auto_now=False)

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Amigos"
        verbose_name = "Amigo"

    def __str__(self):
        return "{}-{}".format(self.first_name, self.last_name)