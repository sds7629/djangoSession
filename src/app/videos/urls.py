from django.urls import path
from . import views
urlpatterns = [
    path('video', views.VideoListView.as_view({'get': 'list', 'post': 'create'}), name='video-list'),
    path('video/<int:pk>', views.VideoListView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='video-list')

]