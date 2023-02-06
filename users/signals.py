# signal fire when an object is saved ... we want to use this when a user is saved
from django.db.models.signals import post_save
from django.contrib.auth.models import User  # import user to act on
# function that gets this signal and does some task
from django.dispatch import receiver
from .models import Profile  # used to create a new profile

# Signal: Signal to fire want Profile to be created for each user


# when user is saved (send=user),send this signal "post_save" that is received by @receiver function(create_profile)
# when a user is created --> creates new profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # where instance is instance of the user that was created
        Profile.objects.create(user=instance)

# when user is saved --> saves profile


def save_profile(sender, instance, created):
    instance.profile.save()
