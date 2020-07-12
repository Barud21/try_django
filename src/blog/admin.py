from django.contrib import admin

# Register your models here.
from .models import BlogPost

# no. 19 Model to Django Admin
# adding new objects to the blog from shell, getting information
# about objects added in browser
admin.site.register(BlogPost)