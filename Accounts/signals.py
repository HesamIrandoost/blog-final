from django.db.models.signals import post_save
from django.dispatch import receiver
from Accounts.models import User, Profile

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """
    Signal for post creating a user which activates when a user being created ONLY
    """
    if created:
        Profile.objects.create(user=instance)