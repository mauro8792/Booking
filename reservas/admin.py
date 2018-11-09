from django.contrib import admin
from .models import City, Owner, Property, Reserva, FechaReserva

admin.site.register(City)
admin.site.register(Owner)

admin.site.register(FechaReserva)
# Register your models here.


class FechaReserva_InLine(admin.TabularInline):
    model = FechaReserva
    fk_name = 'prop'
    extra = 0
    exclude = ['reserva']


class PropertyAdmin(admin.ModelAdmin):
    inlines = [FechaReserva_InLine, ]


admin.site.register(Property, PropertyAdmin)
admin.site.register(Reserva)