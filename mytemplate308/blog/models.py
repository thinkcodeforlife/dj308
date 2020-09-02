from django.db import models

import datetime
from django.utils import timezone

### BLOG MODELS ###

class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.CharField(max_length=5000)
    # TODO: this field must be datetime field!
    created_at = models.DateField(auto_now=True)
    # TODO: this field must be renamed to updated_at
    published = models.DateField(auto_now_add=True)
    # user = models.ForeignKey('User', on_delete=models.CASCADE())

    def __str__(self):
        return f"Post title:{self.title}"

    def was_published_recently(self):
        # return self.created_at >= timezone.now().date() - datetime.timedelta(days=1)
        # Fixing the bug -> got from testcase! (test_was_published_recently_with_future_post)
        now = timezone.now()
        return now.date() - datetime.timedelta(days=1) <= self.created_at <= now.date()