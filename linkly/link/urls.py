from django.urls import path, include
from . import views

urlpatterns = [
path("create_category/", views.add_category, name="create_category" ),
path("create_link/", views.add_link, name="create_link" ),
path("links/", views.links, name="links" ),




    
]
