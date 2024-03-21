from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = "__all__"

    def get_user(self, obj: object) -> dict:
        return {"nickname": obj.nick}

    def get_comments(self, obj: object) -> list:
        comments = []
        for comment in obj.comments_comment:
            comments.append(
                {
                    'pk': comment.pk,
                    'text': comment.text,
                    'author': comment.username,
                }
            )
        return comments

    # def to_representation(self, instance):
    #     comments = []
    #     for comment in instance.to_comments:
    #         comments.append(
    #             {
    #                 'id': comment.id,
    #                 'text': comment.text,
    #                 'writer': comment.username
    #             }
    #         )
    #     repr = {
    #         "pk": instance.pk,
    #         "streamer": {
    #             "nickname": instance.nick,
    #         },
    #         "title": instance.title,
    #         "description": instance.description,
    #         "link": instance.link,
    #         'category': instance.category,
    #         'views_count': instance.views_count,
    #         'reviews': comments
    #     }
    #     return repr
