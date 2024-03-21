from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubscriptionListView.as_view({'post':'create'}), name='subscription-list')
]