from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('common:home')

    def form_invalid(self, form):
        result = super().form_valid(form)
        login(
            self.request,
            self.object,
            backend="accounts.backends.EmailBackend",
        )

        return result