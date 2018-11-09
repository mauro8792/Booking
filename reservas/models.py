from django.db import models
from django.utils.timezone import now

class City(models.Model):
    city = models.CharField(max_length=200)

    def __unicode__(self):
        return self.city


class Owner(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __unicode__(self):
        return self.lastName + ", " + self.name


class Property(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):
        return self.description + " $" + str(self.amount)


class Reserva(models.Model):
    fechaReserva = models.DateField(auto_now=False, default=now) # fecha en la q se realizo la reerva
    total = models.DecimalField(max_digits=20, decimal_places=2)
    propiedad = models.ForeignKey(Property, on_delete=models.CASCADE)


class FechaReserva(models.Model):
    fechaReserva = models.DateField(null=False)
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, default=None, null=True, blank=True)