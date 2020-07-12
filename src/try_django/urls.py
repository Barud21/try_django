"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path # url, re_path - regular expression
from blog.views import (
    blog_post_detail_page
)
from .views import (
    home_page,
    about_page,
    contact_page,
    example_page
)

urlpatterns = [
    path('', home_page),
    # path('blog/', blog_post_detail_page),
    path('blog/<str:slug>/', blog_post_detail_page),  # <int:id> - passes additional argument, allows to update the view depending on argument
    # re_path(r'^blog/(?P<slug>\w+)/$', blog_post_detail_page),  # does the what the line above, but uses regular expressions
    re_path(r'^pages?/$', about_page),  #regular expression covers 2 different scenarios, it works for page and pages
    re_path(r'^about/$', about_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
    path('example/', example_page)
]

# no. 24 A new database lookup value