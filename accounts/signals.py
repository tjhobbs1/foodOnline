from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_reciever(sender, instance, created, **kwargs):
    # Create User Profile
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile is created.')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if not exist.
            UserProfile.objects.create(user=instance)
            print('Profile did not exist, one was created')
        print("user is updated")


def pre_save_profile_reciever(sender, instance, **kwargs):
    pass
    #post_save.connect(post_save_create_profile_reciever, sender=User)
