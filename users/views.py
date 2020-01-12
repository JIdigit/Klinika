from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def user_register(request):
    form = UserCreationForm()
    return render(request, 'account/user_signup.html', {'form': form})
