from django.db import models
from ..common.models import CommonModel
from django.contrib.auth import get_user_model


class Comment(CommonModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    content = models.ForeignKey("videos.Video", on_delete=models.CASCADE, related_name="comments")
