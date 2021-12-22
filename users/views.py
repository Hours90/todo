from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

from .forms import MyLoginForm, MyRegisterForm

class LoginUser(LoginView):
    template_name = 'users/login.html'  # your template
    form_class = MyLoginForm # your form
    

def register(request):
    form = MyRegisterForm()

    if request.method == 'POST':
        form = MyRegisterForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('users:login')
    return render(request,'users/register.html', {'form': form})
