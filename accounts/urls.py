from django.contrib.auth.views import LoginView
from . import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

]