"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.contrib.staticfiles import staticfiles_urlpatterns
from django.conf.urls import handler404, handler500
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register/", RegistrationView.as_view(success_url='/'), name="registration_page"),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('accounts/reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# urlpatterns += staticfiles_urlpatterns()
handler404 = 'myapp.views.error_404'