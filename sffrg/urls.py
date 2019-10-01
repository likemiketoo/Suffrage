from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views


app_name = 'sffrg'
urlpatterns = [
    path('', views.home_screen_view, name="home"),
    path('elections', views.election_view, name="election"),
    path('election<int:election_id>/candidates', views.candidate_view, name="candidate"),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]