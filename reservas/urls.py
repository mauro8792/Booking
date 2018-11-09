from django.conf.urls import *
from reservas.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^ver_reservas/$', res, name='ver_reserv'),
    url(r'^ver_reservas/filter/$', res_param, name='res_param'),
    url(r'^hacer_reserva/(?P<property_id>\d+)$', hacer_reserva, name='hacer_reserva'),
    url(r'^finalizar_reserva/$', finalizar_reserva, name='finalizar_reserva'),

]
