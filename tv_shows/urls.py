from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:show_id>', views.show_info),
    #we are assigning the show_id here in the URL, not the other way around where we're utilizing here
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
    path('shows/<int:show_id>/delete', views.delete),
]