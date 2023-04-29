from django.urls import path, include
from . import views

urlpatterns = [
path("create_category/", views.add_category, name="create_category" ),
path("edit_category/<int:pk>/", views.edit_category, name="edit_category" ),
path("delete_category/<int:pk>/", views.delete_category, name="delete_category" ),

path("create_link/", views.add_link, name="create_link" ),
path("delete_link/<int:pk>/", views.delete_link, name="delete_link" ),
path("edit_link/<int:pk>/", views.edit_link, name="edit_link" ),


path("links/", views.links, name="links" ),
path("categories/", views.categories, name="categories" ),





    
]
