from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^sales_report/$', 'reporting_tools.views.sales_report', name='sales_report'),
)