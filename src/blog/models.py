from django.db import models

# Create your models here.

class BlogPost(models.Model):   # after creating new model, make sure it is in the apps (settings.py) and type in terminal "python manage.py makemigrations" and "python manage.py migrate"
    # id = models.IntegerField()    # primary key (pk)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)       # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

# no. 19 Model to Django Admin