from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from . import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile-detail/', views.ProfileDetailView.as_view(), name='detail'),
    path('personal-info-detail/', views.UserPersonalInfoDetailView.as_view(), name='personal-info'),
    path('profile-edit/', views.ProfileEditView.as_view(), name='edit'),
    path('personal-info-edit/', views.UserPersonalInfoEditView.as_view(), name='personal-info-edit'),
    path('user-delete/', views.UserDeleteView.as_view(), name='delete'),

    path('password-change/', PasswordChangeView.as_view(
        template_name='accounts/password-change-page.html',
        success_url=reverse_lazy("accounts:password-change-done"),
    ), name='password-change'),

    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password-change-done-page.html',
    ), name='password-change-done'),

]