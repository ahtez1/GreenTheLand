# urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from .views import Index, Contact, Signup


urlpatterns = [
    path('', Index, name='home'),
    path('signup/', Signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('contact/', Contact, name='contact'),
]
