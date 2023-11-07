from django.urls import path

from . import views

app_name = "facemasq"
urlpatterns = [
    path("", views.index, name="index"),
    path("masks/create", views.create_mask, name="create_mask"),
    path("masks/delete", views.delete_mask, name="delete_mask"),
    path("masks/view", views.view_masks, name="view_masks"),
    path("photo/create", views.create_photo, name="create_photo"),
    path("video/create", views.create_video, name="create_video"),
]