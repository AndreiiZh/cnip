from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .form import SubscriberForm
from .models import User


# Create your views here.

class SubscriberView(FormView):
    model = User
    form_class = SubscriberForm
    template_name = 'cnip/landing_cnip.html'
    success_url = reverse_lazy('user:ok')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def user_list(request):
#     return render(request, 'cnip/landing_cnip.html', {})
