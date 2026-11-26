from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, ProfileEditForm, UserPersonalInfoEditForm, UserDeleteForm
from .models import Profile

UserModel = get_user_model()


class RegisterView(UserPassesTestMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('common:home')

    def test_func(self) -> bool:
        return not self.request.user.is_authenticated


    def form_invalid(self, form):
        result = super().form_valid(form)
        login(
            self.request,
            self.object,
            backend="accounts.backends.EmailBackend",
        )

        return result


class CustomLoginView(UserPassesTestMixin, LoginView):
    template_name = 'accounts/login.html'

    def test_func(self) -> bool:
        return not self.request.user.is_authenticated


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'
    http_method_names = ["get", "post", "options"]
    next_page = reverse_lazy("common:home")


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-detail-page.html'

    def get_object(self, queryset = None):
        return UserModel.objects.select_related(
            'profile'
        ).get(pk=self.request.user.pk)


class UserPersonalInfoDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/personal-info-detail-page.html'

    def get_object(self, queryset = None):
        return self.request.user


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit-page.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('accounts:detail')

    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)


class UserPersonalInfoEditView(UpdateView):
    model = UserModel
    template_name = 'accounts/personal-info-edit-page.html'
    form_class = UserPersonalInfoEditForm
    success_url = reverse_lazy('accounts:personal-info')

    def get_object(self, queryset = None):
        return self.request.user


class UserDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/user-delete-page.html'
    form_class = UserDeleteForm
    success_url = reverse_lazy('common:home')

    def get_object(self, queryset = None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def get_initial(self) -> dict:
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)
