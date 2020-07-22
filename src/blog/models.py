from django.conf import settings
from django.db import models

# Create your models here.


User = settings.AUTH_USER_MODEL
class BlogPost(models.Model):   # blogpost_set->queryset; after creating new model, make sure it is in the apps (settings.py) and type in terminal "python manage.py makemigrations" and "python manage.py migrate"
    # id = models.IntegerField()    # primary key (pk)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)       # hello world -> hello-world
    content = models.TextField(null=True, blank=True)
