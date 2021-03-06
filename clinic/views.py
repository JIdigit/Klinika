from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from .forms import DoctorLoginForm, DoctorRegisterForm, CommentForm, EvaluationForm
from .models import Profile, Clinic, Comments, Ocenka

from googleapiclient import discovery
# from


def get_the_average(pk):
    profile = Profile.objects.get(id=pk)
    all = profile.evaluations.all()
    try:
        total = 0
        for i in all:
            total += i.ocenka
        average = total/len(all)
        return round(average, 2)
    except ZeroDivisionError:
        return 0


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
    model = Profile
    template_name = 'clinic/doctor_list.html'
    context_object_name = 'profiles'


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    comments = profile.comments.filter(active=True)
    new_comment = None
    average = get_the_average(pk)
    if request.method == 'POST':
        evaluation = EvaluationForm(data=request.POST)
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            cd = comment_form.cleaned_data
            if cd['nickname'] == 'Anonymous':
                new_comment = Comments.objects.create(comments=Profile(id=pk),
                                                      text=cd['text'])
            else:
                new_comment = Comments.objects.create(comments=Profile,
                                                      nickname=Profile.first_name,
                                                      text=cd['text'])
            new_comment.save()

        if evaluation.is_valid():
            cd = evaluation.cleaned_data
            Ocenka.objects.create(likes=Profile(id=pk), ocenka=cd['ocenka']).save()
            average = get_the_average(pk)

    else:
        comment_form = CommentForm()
        evaluation = EvaluationForm()

    return render(request, 'clinic/doctor_detail.html', {'comment_form': comment_form,
                                                         'profile': profile,
                                                         'comments': comments,
                                                         'new_comment': new_comment,
                                                         'evaluation_form': evaluation,
                                                         'average': average})


#
# class DoctorDetailView(DetailView):
#     model = Profile
#     template_name = 'clinic/doctor_detail.html'
#     context_object_name = 'doctor'



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
    template_name = 'test.html'





