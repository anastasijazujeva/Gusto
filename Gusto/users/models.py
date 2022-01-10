from django.db import models
from django.contrib.auth.models import User

# Profile table in the database
class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(default = '/profile_img/default_profile.jpg', upload_to = 'profile_img')
    bio = models.TextField(blank = True)
    city = models.CharField(max_length=100, blank = True)
    country = models.CharField(max_length=100, blank = True)

    # display username in a list of profiles in the table
    def __str__(self):
        return self.user.username
