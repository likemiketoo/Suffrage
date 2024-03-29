from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

app_name = 'sffrg'
urlpatterns = [
    path('', views.home_screen_view, name="home"),
    path('elections/', views.election_view, name="election"),
    path('elections/<str:election_id>/positions/', views.position_view, name="position"),
    path('positions/<str:position_signed>/candidates/', views.candidate_view, name="candidate"),
    path('candidates/<str:candidate_signed>/vote/', views.vote, name='vote'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

