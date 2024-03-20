from rest_framework import serializers
from .models import Video
class VideoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Video
        fields = '__all__'


    def get_user(self,obj:object) -> dict:
        return {'nickname': obj.nick}