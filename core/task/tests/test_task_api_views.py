from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse

from ..api.v1.views import TaskModelViewSet
from account.models import Profile

User = get_user_model()

class TestTaskModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@ex.com", password="string1234")
        self.client = APIClient()
        profile = Profile.objects.get(user = self.user)
        self.profile = profile
    
    
    def test_task_list_unauthorized(self):
        url = reverse("task:api:task_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)