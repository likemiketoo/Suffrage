from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = 'sffrg'
urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]