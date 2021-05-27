from django.test import TestCase
from .models import Post


class TestPost(TestCase):

    def setUp(self) -> None:
        self.post = Post.objects.create(title='django', author='django', slug='django')

    def test_post_model(self):
        self.assertEqual(str(self.post), 'django')

    def test_naive(self):
        self.assertTrue(True)
