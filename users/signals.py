from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal, receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user = user
            )
        profile = user.profile
        if user.first_name:
            profile.name = user.first_name
        if user.email:
            profile.email = user.email
        profile.save()
            
            


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    profile = instance
    try:
        user = profile.user
        user.delete()
    except:
        pass
    
# @receiver(post_save, sender=Profile)
# def user_update(sender, instance, created, **kwargs):
#     if not created:
#         user = instance.user
#         print(user)
#         if user.first_name and (user.last_name == ''):
#             user.first_name = instance.name
#         elif user.last_name and (user.first_name == ''):
#             user.last_name = instance.name
#         else:
#             first_last_name = instance.name
#             names_list = first_last_name.split()
#             user.first_name = names_list[0]
#             if len(names_list) == 2:
#                 user.last_name = names_list[1]
#         if instance.email:
#             user.email = instance.email
#         user.save()
            

# Signal.connect(post_save, create_profile, sender=User)
# Signal.connect(post_delete, delete_user, sender=Profile)