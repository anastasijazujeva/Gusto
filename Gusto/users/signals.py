from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver

# function that assigns additional profile information from the Profile table (image, country, city, bio)
# to a user once it is created
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

# save the pofile when the user is saved
@receiver(post_save, sender = User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()