from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# model is: 1 Profile - 1 User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pic is the directory to store the profile pics
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    # __str__ is used to better display the SQL object for easier to read
    def __str__(self):
        return f'{self.user.username} Profile'

# This method that exists in parent class but we are overriding. This Save is called instead when profile is saved
    def save(self):
        print('IN SAVE')
        super().save()  # call the parent class save() function = this is already called when profile is saved
        image = Image.open(self.image.path)
        output_size = (300, 300)
        if image.height > 300 or image.width > 300:
            image.thumbnail(output_size)
            image.save(self.image.path)
