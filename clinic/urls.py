from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', doctor_login, name='doctor_login'),
    path('logout/', doctor_logout, name='logout'),
    path('register/', doctor_register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)