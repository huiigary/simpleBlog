from django.contrib import admin
from .models import Post  # Post is the model we want to register

# Register your models here.
admin.site.register(Post)
