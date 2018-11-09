from django.http import HttpResponse
from django.shortcuts import render
from datetime import *

from .models import (
    FechaReserva,
    Property,
    Reserva
)

def reservas(request):
    return HttpResponse('Listado de Propiedades')


def index(request):
    reserv = Property.objects.all()
    return render(request, 'index.html', {'reservas': reserv})

def res(request):
    reserv = Property.objects.all()
    return render(request, 'res.html', {'reservas': reserv})

def res_param(request):
    if request.method == "POST":
        desde = request.POST.get("desde")
        hasta = request.POST.get("hasta")
        ciudad= request.POST.get("ciudad")

        if desde and hasta:
            fecha_reserva = FechaReserva.objects.filter(fechaReserva__range=(desde, hasta))
        else:
            fecha_reserva = FechaReserva.objects.all()

        reserv = []
        flag = 1
        for reserva_dia in fecha_reserva:
            for prop in reserv:
                if prop.pk == reserva_dia.prop.pk:
                    flag = 0
                    break
            if flag == 1:
                reserv.append(reserva_dia.prop)
            else:
                flag = 1
        if ciudad:
            reserv = filter(lambda obj: obj.city.city == ciudad, reserv)

    return render(request, "res.html", {'reservas': reserv})


def hacer_reserva(request, property_id):
    reserv = Property.objects.get(pk=property_id)
    dates = FechaReserva.objects.filter(prop=property_id, reserva=None)
    return render(request, 'confirmationReserv.html', {'reservas': reserv, 'dates':dates })

def finalizar_reserva (request):
    if request.method == 'POST':
        property_id = request.POST.get('property_id')
        reserv = Property.objects.get(pk=property_id)
        dates_pk = dict(request.POST)['dates']

        booking = Reserva()
        booking.fechaReserva=datetime.now()
        booking.total = reserv.amount * len(dates_pk)
        booking.propiedad = reserv
        booking.save()

        for fecha in dates_pk:
            f = FechaReserva.objects.get(pk=fecha)
            f.reserva = booking
            f.save(force_update=True)

    return render(request, 'index.html')

