from django.http import HttpRequest, HttpResponse
from typing import Any
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription
from .serializers import SubSerializer


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = ...

    def create(self, request:HttpRequest, *args,**kwargs) -> HttpResponse:
        user_data = SubSerializer(data = request.data)
        user_data.is_valid(raise_exception=True)
        user_data.save(subscriber = request.user)
        return Response(user_data.data, status=status.HTTP_201_CREATED)


class SubscriptionDetail(ModelViewSet):
    def retrieve(self, request:HttpRequest, *args:Any, **kwargs:Any) -> HttpResponse:
        ...

    def destroy(self, request:HttpRequest, *args:Any, **kwargs:Any) -> HttpResponse:
        ...