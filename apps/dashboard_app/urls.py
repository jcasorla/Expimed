from django.conf.urls import url, include
from django.contrib import admin
from . import views
# from django.conf.urls import handler404

# handler404 = 'dashboard_app.views.bad_request'

urlpatterns = [
    url(r'^dash/show$', views.show),
    url(r'^dash/meds_grid$', views.meds_grid),
    url(r'^dash/cat_grid$', views.cat_grid), 
    # url(r'^dash/calendar$', views.calendar),
    url(r'^dash/new_patient$', views.new_patient),
    url(r'^dash/insert_patient$', views.insert_patient),
    url(r'^dash/patient/(?P<my_val>\d+)$', views.patient_view),
    url(r'^dash/patient/(?P<my_val>\d+)/edit$', views.patient_edit),
    url(r'^dash/patient/(?P<my_val>\d+)/update$', views.patient_update),
    url(r'^dash/patient/(?P<my_val>\d+)/del$', views.patient_del),
    url(r'^dash/patient/(?P<user_id>\d+)/presc_med/(?P<med_id>\d+)$', views.presc_med),
    url(r'^dash/patient/(?P<user_id>\d+)/unpresc_med/(?P<med_id>\d+)$', views.unpresc_med),
    url(r'^dash/patient/(?P<user_id>\d+)/unpresc_med2/(?P<med_id>\d+)$', views.unpresc_med2),
    url(r'^dash/new_med$', views.new_med),
    url(r'^dash/insert_med$', views.insert_med),
    url(r'^dash/med/(?P<my_val>\d+)$', views.med_view),
    url(r'^dash/med/(?P<my_val>\d+)/del$', views.med_del),
    url(r'^dash/med/(?P<my_val>\d+)/edit$', views.med_edit),
    url(r'^dash/med/(?P<my_val>\d+)/update$', views.med_update),
    url(r'^dash/new_cat$', views.new_cat),
    url(r'^dash/insert_cat$', views.insert_cat),
    url(r'^dash/cat/(?P<my_val>\d+)$', views.cat_view),
    # url(r'^dash/cat/(?P<my_val>\d+)/del$', views.cat_del),
    url(r'^dash/cat/(?P<my_val>\d+)/edit$', views.cat_edit),
    url(r'^dash/cat/(?P<my_val>\d+)/update$', views.cat_update),
    # url(r'^(dash.*)/$', views.bad_request),
    url(r'.*/$', views.bad_request),

]