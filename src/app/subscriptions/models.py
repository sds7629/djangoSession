from django.db import models
from ..common.models import CommonModel
from django.conf import settings

class Subscription(CommonModel):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'subscribers')