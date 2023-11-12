# Create your models here
from django.db import models
from django.conf import settings

class Mask(models.Model):
    mask_ID = models.primaryKey(primary_key=True, editable=False)
    user_ID = models.foreignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, required=True)
    mask_location = models.URLField(max_length=200, required=True)
    mask_prompt = models.CharField(max_length=200, required=True)
    mask_seed = models.IntegerField(default=0, required=True)
    mask_creation_date = models.DateTimeField("date published")
    def __str__(self):
        return self.cloudstorageID
    
class Photo(models.Model):
    photo_ID = models.PrimaryKey(primary_key=True, editable=False)
    user_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, required=True)
    mask_ID = models.ForeignKey(Mask, required=True)
    src_photo_location = models.URLField(max_length=200, required=True)
    photo_location = models.URLField(max_length=200, required=True)
    photo_creation_date = models.DateTimeField("date published")
    def __str__(self):
        return self.cloudstorageID
    
class Video(models.Model):
    video_ID = models.PrimaryKey(primary_key=True, editable=False)
    user_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, required=True)
    mask_ID = models.ForeignKey(Mask, required=True)
    src_video_location = models.URLField(max_length=200, required=True)
    video_location = models.URLField(max_length=200, required=True)
    video_creation_date = models.DateTimeField("date published")
    def __str__(self):
        return self.cloudstorageID