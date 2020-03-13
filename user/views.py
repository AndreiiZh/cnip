from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from urllib3 import request

from .form import SubscriberForm, QuestionForm
from .models import User, Question, ListService, Service
from django.views.generic.list import ListView


# Create your views here.

# class SubscriberView(FormView):
#     model = User
#     form_class = SubscriberForm
#     template_name = 'cnip/landing_cnip.html'
#     success_url = reverse_lazy('user:ok')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# def user_list(request):
#     return render(request, 'cnip/landing_cnip.html', {})

class QuestionView(FormView):
    model = Question
    form_class = QuestionForm
    template_name = 'cnip/question.html'
    success_url = ('http://127.0.0.1:8000/cnip/ok/')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


"""отображение услуг по категориям"""


class ServiceListView(ListView):
    model = ListService

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context['category_list'] = Service.objects.all()
        return context


class ServiceDetailView(DetailView):
    model = ListService


class ListServiceViewId1(ListView):
    model = ListService

    def get_queryset(self):
        return ListService.objects.filter(category__id='1')


class ListServiceViewId2(ListView):
    model = ListService

    def get_queryset(self):
        return ListService.objects.filter(category__id='2')


class ListServiceViewId3(ListView):
    model = ListService

    def get_queryset(self):
        return ListService.objects.filter(category__id='3')


class ListServiceViewId4(ListView):
    model = ListService

    def get_queryset(self):
        return ListService.objects.filter(category__id='4')


class ListServiceViewId5(ListView):
    model = ListService

    def get_queryset(self):
        return ListService.objects.filter(category__id='5')


class ListServiceViewId6(ListView):
    model = ListService

    def get_queryset(self):
        return ListService.objects.filter(category__id='6')
