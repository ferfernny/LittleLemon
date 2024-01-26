from django.test import TestCase
from .models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .serializers import MenuSerializer
# Create your tests here.
#TestCase class
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
    def test_getall(self):
        url = reverse('menu')
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu_item = Menu.objects.all()
        expected_data = MenuSerializer(menu_item, many=True).data
        
        self.assertEqual(response.data, expected_data)
        