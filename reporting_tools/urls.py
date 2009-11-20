from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^orders_report/$', 'reporting_tools.views.orders_report', name='orders_report'),
    url(r'^products_report/$', 'reporting_tools.views.products_report', name='products_report'),
)