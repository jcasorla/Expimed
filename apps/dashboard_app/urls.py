from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^dash/show$', views.show),
    url(r'^dash/meds_grid$', views.meds_grid),    
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

]