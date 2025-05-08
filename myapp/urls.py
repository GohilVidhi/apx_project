"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('test', test.as_view()),

    path('service/', service_view.as_view()),
    path('service/<int:id>/', service_view.as_view()),

    path('service_item/', service_item_view.as_view()),
    path('service_item/<int:id>/', service_item_view.as_view()),
    path('service_item/service_id/<int:service_id>/', service_item_view.as_view()),

    path('blog/', blog_view.as_view()),
    path('blog/<int:id>/', blog_view.as_view()),
    path('blog/blog_id/<int:blog_id>/', blog_view.as_view()),

    path('nft_barriers/', nft_barriers_view.as_view()),
    path('nft_barriers/<int:id>/', nft_barriers_view.as_view()),

    path('contact_us/', contact_us_view.as_view()),
    path('contact_us/<int:id>/', contact_us_view.as_view()),

    path('berries_structure/', berries_structure_view.as_view()),
    path('berries_structure/<int:id>/', berries_structure_view.as_view()),

    path('admin_login/', admin_login_view.as_view()),
    path('admin_login/<int:id>/', admin_login_view.as_view()),

    path('ad/', ad_view.as_view()),
    path('ad/<int:id>/', ad_view.as_view()),

    path('user/', user_view.as_view()),
    path('user/<str:id>/', user_view.as_view()),

    path('token/', token_view.as_view()),
    path('token/<str:id>/', token_view.as_view()),

    path('blog_categories/', blog_categories_view.as_view()),
    path('blog_categories/<int:id>/', blog_categories_view.as_view()),


    path('grower/', grower_view.as_view()),
    path('grower/<int:id>/', grower_view.as_view()),
    
    path('certifications/', certifications_view.as_view()),
    path('certifications/<int:id>/', certifications_view.as_view()),
    
    path('utility_tags/', utility_tags_view.as_view()),
    path('utility_tags/<int:id>/', utility_tags_view.as_view()),
    
    path('berry_types/', berry_types_view.as_view()),
    path('berry_types/<str:id>/', berry_types_view.as_view()),    

    path('berry_batch/', berry_batch_view.as_view()),
    path('berry_batch/<int:id>/', berry_batch_view.as_view()),   
]
