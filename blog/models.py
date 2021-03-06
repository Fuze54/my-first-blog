from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    content = RichTextField

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    content = RichTextField

    def approve(self):
        self.approved = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def __str__(self):
        return self.text

