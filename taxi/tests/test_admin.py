from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

INDEX_URL = reverse("taxi:index")


class DriverAdminTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.admin = get_user_model().objects.create_superuser(
            username="Test", password="Test12345"
        )

        self.client.force_login(self.admin)

        self.user = get_user_model().objects.create_user(
            username="Test123",
            password="Test12345",
            license_number="KV12345",
        )

    def test_license_number_listed(self):
        url = f"{INDEX_URL}admin/taxi/driver/"
        response = self.client.get(url)

        self.assertContains(response, self.user.license_number)

    def test_license_number_in_update_page(self):
        url = f"{INDEX_URL}admin/taxi/driver/2/change/"
        response = self.client.get(url)

        self.assertContains(response, self.user.license_number)

    def test_license_number_in_create_page(self):
        url = f"{INDEX_URL}admin/taxi/driver/add/"
        response = self.client.get(url)

        self.assertContains(response, "License number:")
