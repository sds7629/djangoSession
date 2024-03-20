import pytest
import requests
from rest_framework.views import APIView
from rest_framework.test import APITestCase
from django.urls import reverse


local = 'http://127.0.0.1:8000'

class APITest(APIView):
    def get(self,request):
        ...
@pytest.mark.django_db
class VideoTest:
    def test_비디오가져오기(self) -> None:
        res = requests.get(reverse('video-list'))
        res.raise_for_status()
        assert res.status_code == 200
        video_list = res.json()
        assert video_list['title'] == '뉴튜브'

    def test_비디오생성하기(self):...
    def test_비디오업데이트(self):...
    def test_비디오삭제(self):...