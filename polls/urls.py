from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('polls/', views.PollListView.as_view(), name='poll_list'),
    path('polls/create/', views.poll_create, name='poll_create'),
    path('polls/<int:pk>/', views.PollDetailView.as_view(), name='poll_detail'),
    path('polls/<int:pk>/update/', views.poll_update, name='poll_update'),
    path('polls/<int:pk>/delete/', views.poll_delete, name='poll_delete'),
    path('polls/<int:poll_id>/vote/', views.vote, name='vote'),
    path('polls/<int:pk>/results/', views.PollResultsView.as_view(), name='poll_results'),
]