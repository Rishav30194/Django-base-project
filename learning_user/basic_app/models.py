from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adittional details
    portfolio_site = models.URLField(blank = True)
    user_profile_photo = models.ImageField(upload_to = 'profile_picture',blank = True)

    #def __str__():
    #    return self.user.username
