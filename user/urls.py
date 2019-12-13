from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.SubscriberView.as_view()),
    path('ok/', TemplateView.as_view(template_name='cnip/ok.html'), name='ok'),
    path('about/', TemplateView.as_view(template_name='cnip/about.html'), name='about'),

]
