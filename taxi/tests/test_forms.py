from django.contrib.auth import get_user_model
from django.test import TestCase
from taxi.forms import DriverCreationForm, DriverUpdatingForm


class DriverCreationFormTest(TestCase):
    def test_driver_creation_form_with_first_name_last_name_and_license_number(self):
        form_data = {
            "username": "new_driver",
            "password1": "Driver123password",
            "password2": "Driver123password",
            "first_name": "first_test",
            "last_name": "last_test",
            "license_number": "KVP12234",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class DriverUpdatingFormTest(TestCase):
    def test_license_number_validation(self):
        form_data_checked = {"license_number": "KVP12345"}
        form_data_less_then_8_digits = {"license_number": "as21235"}
        form_data_first_3_not_capital = {"license_number": "abs21235"}
        form_data_last_5_not_numbers = {"license_number": "ABS123a"}

        form = DriverUpdatingForm(data=form_data_checked)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data_checked)

        form = DriverUpdatingForm(data=form_data_less_then_8_digits)
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(form, "License must have 8 digits.")

        form = DriverUpdatingForm(data=form_data_first_3_not_capital)
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(form, "First 3 characters must be capital letters.")

        form = DriverUpdatingForm(data=form_data_last_5_not_numbers)
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(form, "Last 5 characters must be numbers.")
