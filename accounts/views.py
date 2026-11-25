from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


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


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'
    http_method_names = ["get", "post", "options"]
    next_page = reverse_lazy("common:home")