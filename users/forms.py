from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, skill, Messages

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'ism',
            'last_name': 'sharif',
            'email': 'email manzilingiz',
            'username': 'username',
            }
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs.update({"class":"input input--text"})
            
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "info", "location", "photo", "bio", "other_skill",\
                  "sochial_github", "sochial_instagram", "sochial_youtube", "sochial_telegram"]
        
        widgets = {
            "other_skill": forms.CheckboxSelectMultiple()
            }
        
        
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs.update({"class":"input input--text"})
            
class SkillForm(ModelForm):
    description = forms.CharField()
    class Meta:
        model = skill
        fields = ["name", "description"]
        
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs.update({"class":"input input--text"})
            
class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ["name", "contact", "message"]
        
        labels = {
            "name":"Ismingizni kiriting",
            "contact":"Telefon raqamingizni kiriting",
            "message":"Xabaringizni yozing"
            }
        
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs.update({"class":"input input--text"})

    
        
        
        