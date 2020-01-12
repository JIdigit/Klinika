from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import DoctorLoginForm, DoctorRegisterForm
from .models import Doctor, Clinic


class HomePageView(TemplateView):
    template_name = 'clinic/home.html'


class ClinicsListView(ListView):
    model = Clinic
    template_name = 'clinic/clinics.html'
    context_object_name = 'clinics'


class ClinicDetailView(DetailView):
    model = Clinic
    template_name = 'clinic/clinic_detail_view.html'
    context_object_name = 'clinic_details'


class DoctorListView(ListView):
    model = Doctor
    template_name = 'clinic/doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'clinic/doctor_detail.html'
    context_object_name = 'doctor'



def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'clinic/home.html', {'user': user})

    else:
        form = DoctorLoginForm()

    return render(request, 'account/login.html', {'form': form})


def doctor_logout(request):
    logout(request)
    return render(request, 'clinic/home.html')


def doctor_register(request):
    if request.method == 'POST':
        user_form = DoctorRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            cd = user_form.cleaned_data
            new_user.set_password(cd['password'])
            new_user.save()
            login(request, new_user)
            return render(request, 'clinic/home.html')
    else:
        user_form = DoctorRegisterForm()

    return render(request, 'account/register.html', {'form': user_form})

class Test(TemplateView):
    template_name = 'elements.html'



