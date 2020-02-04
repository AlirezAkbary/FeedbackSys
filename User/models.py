from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    FirstName = models.CharField(null=False, blank=False, max_length=100)
    LastName = models.CharField(null=False, blank=False, max_length=100)
    class Meta:
        abstract = True

    def __str__(self):
        return self.user.username


