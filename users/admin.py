from django.contrib import admin
from .models import Profile

# Registers the Profile model to the admin site for visibility (/admin url)
admin.site.register(Profile)
