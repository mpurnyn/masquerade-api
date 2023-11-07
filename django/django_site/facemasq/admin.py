from django.contrib import admin

# Register your models here.
from .models import Mask, Photo, Video
admin.site.register(Mask)
admin.site.register(Photo)
admin.site.register(Video)