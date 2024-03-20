import pytest
import requests
from django.contrib.auth import get_user_model

User = get_user_model()

local = 'http://127.0.0.1:8000'
@pytest.mark
class UserTest:
    def tests_유저생성(self):
        res = requests.post(f'{local}/api/v1/users')
