from django.test import TestCase
from .models import Menu
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializer import MenuSerializer
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
class MenuViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.menu1 = Menu.objects.create(title="Pasta", price=12.50 , inventory=50)
        self.menu2 = Menu.objects.create(title="Pizza", price=15.00 , inventory=50)
        self.menu3 = Menu.objects.create(title="Salad", price=9.00 , inventory=50)

    def test_getall(self):
        # Retrieve all Menu objects through the API
        response = self.client.get(reverse('menu'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Run assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)