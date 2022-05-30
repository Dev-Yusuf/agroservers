from django.contrib import admin

# Register your models here.
from . models import Profile, Skill, Experience, Message

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Message)

