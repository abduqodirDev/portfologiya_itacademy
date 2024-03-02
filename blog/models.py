from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(Profile, related_name="project_profile", on_delete = models.SET_NULL, blank=True, null=True)
    title=models.CharField(max_length=250)
    description=models.TextField(null=True, blank=True)
    demo_link=models.CharField(max_length=250, blank=True, null=True)
    source_link=models.CharField(max_length=250, null=True, blank=True)
    photo=models.ImageField(default="default.jpg", upload_to="images/")
    created=models.DateTimeField(auto_now_add=True)
    vote_count=models.IntegerField(default=0)
    vote_ratio=models.IntegerField(default=0)
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tag=models.ManyToManyField('Tag', blank=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.SET_NULL, blank=True, null=True)
    VOTE_TYPE=(
        ("+", "Ijobiy"),
        ("-", "Salbiy")
        )
    body=models.TextField(default='')
    value=models.CharField(max_length=20, choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    project=models.ForeignKey(Project, on_delete=models.CASCADE, 
                              related_name="project_review") 
    
    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name=models.CharField(max_length=250)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.CharField(max_length = 300)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.project)
    
    class Meta:
        ordering=["-created"]





