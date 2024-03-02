from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    info = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    sochial_github = models.CharField(max_length=200, null=True, blank=True)
    sochial_telegram = models.CharField(max_length=200, null=True, blank=True)
    sochial_youtube = models.CharField(max_length=200, null=True, blank=True)
    sochial_instagram = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to="profile/", default="profile/default_image.webp")
    other_skill = models.ManyToManyField("other_skill", blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, editable = False)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering=["-created"]
    
class skill(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE, \
                             related_name="profile_skill", null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, editable = False)
    
    def __str__(self):
        return self.name
    
class other_skill(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name
    
class Messages(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    contact = models.CharField(max_length = 200)
    message = models.TextField()
    
    def __str__(self):
        return str(self.user)
    




