from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from Accounts.models import User, Profile
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """
    Signal for post creating a user which activates when a user being created ONLY
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
