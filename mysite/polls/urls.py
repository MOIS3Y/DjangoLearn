from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/int/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/int/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/int/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
