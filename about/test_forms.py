from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test User',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_invalid_without_name(self):
        form = CollaborateForm({
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form name is missing")

    def test_form_is_invalid_without_email(self):
        form = CollaborateForm({
            'name': 'Test User',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form email is missing")

    def test_message_is_required(self):
        form = CollaborateForm({
            'name': 'Test User',
            'email': 'test@test.com'
        })
        self.assertFalse(form.is_valid(), msg="Form message is missing")