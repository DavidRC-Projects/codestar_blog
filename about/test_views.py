from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm
from blog.models import Post
from django.contrib.auth.models import User

class AboutViewTestCase(TestCase):
    def setUp(self):
        self.about = About.objects.create(
            title='Test About',
            content='This is the about page content.'
        )
        self.user = User.objects.create_user(username="myUsername", password="myPassword")
        self.post = Post.objects.create(
            title="Blog Post",
            slug="blog",
            author=self.user,
            content="Test content"
        )

    def test_about_page_with_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.about.content)
        self.assertIn('collaborate_form', response.context)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'post_detail', args=['blog']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about:about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)