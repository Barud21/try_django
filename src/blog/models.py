from django.db import models

# Create your models here.

class BlogPost(models.Model):   # after creating new model, make sure it is in the apps (settings.py) and type in terminal "python manage.py makemigrations"
    # id = models.IntegerField()    # primary key (pk)
    title = models.TextField()
    slug = models.SlugField()       # hello world -> hello-world
    content = models.TextField(null=True, blank=True)

# no. 19 Model to Django Admin