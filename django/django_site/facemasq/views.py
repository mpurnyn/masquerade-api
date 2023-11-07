from django.http import HttpResponse
from .models import Mask, Photo, Video

def index(request):
    return HttpResponse("Hello, world. You're at the facemasq index.")

def create_mask(request, prompt):
    return HttpResponse("Created a FaceMasq.")

def delete_mask(request, mask_ID):
    return HttpResponse("Deleted the FaceMasq.")

def view_masks(request):
    return Mask.objects.filter(user_ID=request.user)

def create_photo(request):
    return HttpResponse("Created a FaceMasq Photo.")

def create_video(request):
    return HttpResponse("Created a FaceMasq Video.")