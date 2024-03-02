from django.contrib import admin
from .models import Profile, skill, other_skill, Messages
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "info", "user", "created"]
    list_filter = ["created"]
    search_fields = ["name", "info", "bio"]
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "contact"]


# admin.site.register(Profile)
admin.site.register(skill)
admin.site.register(other_skill)
admin.site.register(Messages, MessageAdmin)