# Create your models here
from django.db import models
from django.conf import settings

class Mask(models.Model):
    mask_ID = models.AutoField(primary_key=True, editable=False)
    user_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # if user is deleted, delete the mask
    mask_location = models.URLField(max_length=200)
    mask_prompt = models.CharField(max_length=200)
    mask_seed = models.IntegerField(default=0)
    mask_creation_date = models.DateTimeField("date published")
    def __str__(self):
        return self.mask_location
    
class Photo(models.Model):
    photo_ID = models.AutoField(primary_key=True, editable=False)
    user_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # if user is deleted, delete the photo
    mask_ID = models.ForeignKey(Mask, null=True, on_delete=models.SET_NULL) # if source mask is deleted, null the field, do not delete the photo
    src_photo_location = models.URLField(max_length=200)
    photo_location = models.URLField(max_length=200)
    photo_creation_date = models.DateTimeField("date published")
    def __str__(self):
        return self.photo_location
    
class Video(models.Model):
    video_ID = models.AutoField(primary_key=True, editable=False)
    user_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # if user is deleted, delete the video
    mask_ID = models.ForeignKey(Mask, null=True, on_delete=models.SET_NULL) # if source mask is deleted, null the field, do not delete the video
    src_video_location = models.URLField(max_length=200)
    video_location = models.URLField(max_length=200)
    video_creation_date = models.DateTimeField("date published")
    def __str__(self):
        return self.video_location