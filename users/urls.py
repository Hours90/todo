from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import LoginUser, register 
app_name = 'users'
urlpatterns = [
    #path('login/', LoginView.as_view(template_name ='users/login.html'), name='login'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='../../'), name='logout'),
    path('register/', register , name='register'),
    
]

