from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views

app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(template_name='cnip/landing_cnip.html'), name='cnip'),
    path('ok/', TemplateView.as_view(template_name='cnip/ok.html'), name='ok'),
    path('about/', TemplateView.as_view(template_name='cnip/about.html'), name='about'),
    path('question/', views.QuestionView.as_view(template_name='cnip/question.html'), name='question'),
    url(r'^service/$', views.ServiceListView.as_view(), name='service'),
    url(r'^service/(?P<pk>\d+)$', views.ServiceDetailView.as_view(), name='detail'),
    # path('service/', views.ListServiceView.as_view(template_name='cnip/list_service.html'), name='service'),
    path('service/id1', views.ListServiceViewId1.as_view(template_name='cnip/list_service_id_1.html')),
    path('service/id2', views.ListServiceViewId2.as_view(template_name='cnip/list_service_id_2.html')),
    path('service/id3', views.ListServiceViewId3.as_view(template_name='cnip/list_service_id_3.html')),
    path('service/id4', views.ListServiceViewId4.as_view(template_name='cnip/list_service_id_4.html')),
    path('service/id5', views.ListServiceViewId5.as_view(template_name='cnip/list_service_id_5.html')),
    path('service/id6', views.ListServiceViewId6.as_view(template_name='cnip/list_service_id_6.html')),

]
