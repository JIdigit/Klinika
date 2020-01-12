from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('test/', Test.as_view(), name='test'),
    path('', HomePageView.as_view(), name='home'),
    path('login/', doctor_login, name='doctor_login'),
    path('logout/', doctor_logout, name='logout'),
    path('register/', doctor_register, name='register'),
    path('clinics_list/', ClinicsListView.as_view(), name='clinics_list_view'),
    path('<int:pk>/clinic_detail/', ClinicDetailView.as_view(), name='clinic_detail_view'),
    path('doctor-list/', DoctorListView.as_view(), name='doctor_list'),
    path('<int:pk>/doctor_detail/', DoctorDetailView.as_view(), name='doctor_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)