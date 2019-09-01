"""expimed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

from apps.login_app.models import User as U
from apps.dashboard_app.models import Patient,Med

class UAdmin(admin.ModelAdmin):
    pass
admin.site.register(U, UAdmin)
  
class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)
class MedAdmin(admin.ModelAdmin):
    pass
admin.site.register(Med, MedAdmin)
  

urlpatterns = [
     url(r'^', include('apps.login_app.urls')),
     url(r'^', include('apps.dashboard_app.urls')),
     url(r'^admin/', admin.site.urls),
]
