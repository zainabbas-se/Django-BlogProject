from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=True)

    def __str__(self):
        user_username = self.user.username if self.user else "No User"
        return f"{self.title} by {user_username}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        user_first_name = self.user.first_name if self.user else "Anonymous"
        return f"{self.user.first_name} - {self.blog.id}"
