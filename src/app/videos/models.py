from django.db import models
from django.contrib.auth import get_user_model
from app.common.models import CommonModel

User = get_user_model()

class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.BigIntegerField(default=0)
    thumbnail = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='src/storage/', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
