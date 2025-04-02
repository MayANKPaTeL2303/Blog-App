from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.apps import apps

User = get_user_model()  #Dynamically fetch the user model

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile = apps.get_model('users', 'Profile') 
        Profile.objects.create(user=instance)
