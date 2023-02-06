from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    # text field is similar to CharField but is unrestricted text.
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# magic/special methods using double underscore(__)
# --> Added this to give more detail to what we are viewing in database via Python shell (eg: "Post: blog1" vs  "Post: Post object(1)")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
