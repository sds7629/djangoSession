from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponse, HttpRequest
from django.db.models import Q, F, Prefetch
from .models import Video
from .serializers import VideoSerializer
from typing import Any
from ..comments.models import Comment

class VideoListView(ModelViewSet):
    queryset = (
        Video.objects.annotate(nick=F("user__username"))
        .select_related("user")
        .prefetch_related(
            Prefetch(
                "comments",
                queryset=Comment.objects.annotate(
                    user_name=F("user__username"),
                ),
                to_attr="comments_comment",
            )
        )
    )

    serializer_class = VideoSerializer

    def list(self, request: HttpRequest) -> HttpResponse:
        videos = self.get_queryset()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: HttpRequest) -> HttpResponse:
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        save_data = serializer.save(user=request.user)
        return Response(VideoSerializer(save_data).data, status=status.HTTP_201_CREATED)


class VideoDetailView(ModelViewSet):
    queryset = (
        Video.objects.annotate(nick=F("user__username"))
        .select_related("user")
        .prefetch_related(
            Prefetch(
                "comments",
                queryset=Comment.objects.annotate(
                    user_name=F("user__username"),
                ),
                to_attr="comments_comment",
            )
        )
    )
    serializer_class = VideoSerializer

    def retrieve(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        instance = self.get_object()
        video_data = VideoSerializer(instance)
        return Response(video_data.data, status=status.HTTP_200_OK)

    def update(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        serializer = VideoSerializer(
            self.queryset.get(kwargs["pk"]),
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        update_data = serializer.save()
        return Response(update_data.data, status=status.HTTP_200_OK)

    def destroy(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
