from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ManufacturerModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Manufacturer.objects.create(name="Test", country="Test country")

    def test_str(self):
        manufacturer = Manufacturer.objects.get(id=1)

        self.assertEqual(str(manufacturer), f"{manufacturer.name} {manufacturer.country}")


class CarModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Manufacturer.objects.create(name="Test", country="Test country")
        manufacturer = Manufacturer.objects.get(id=1)
        Car.objects.create(
            model="Test",
            manufacturer=manufacturer
        )

    def test_str(self):
        car = Car.objects.get(id=1)

        self.assertEqual(str(car), car.model)


class DriverModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(
            username="Test",
            password="Test12345"
        )

    def setUp(self) -> None:

        self.user = get_user_model().objects.get(id=1)

    def test_str(self):

        self.assertEqual(str(self.user),f"{self.user.username} ({self.user.first_name} {self.user.last_name})")

    def test_verbose_name(self):

        self.assertEquals(self.user._meta.verbose_name, "driver")

    def test_verbose_name_plural(self):

        self.assertEquals(self.user._meta.verbose_name_plural, "drivers")

    def test_get_absolute_url(self):

        self.assertEquals(self.user.get_absolute_url(), '/drivers/1/')
