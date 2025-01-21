from django.urls import reverse_lazy
from django.views import generic

from users.forms import UserForm

class RegisterView(generic.FormView):
    template_name = 'users/register_user.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
