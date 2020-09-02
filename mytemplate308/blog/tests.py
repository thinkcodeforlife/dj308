import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Post


class PostModelTests(TestCase):
    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() returns False for posts
        whose created_at date is in the future
        """
        time = timezone.now().date() + datetime.timedelta(days=30)
        future_post = Post(created_at=time)
        self.assertIs(future_post.was_published_recently(), False)