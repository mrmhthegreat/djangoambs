from django.contrib import admin
from .models import Uploads
# Register your models here.
class UploadCusotmize(admin.ModelAdmin):
    list_display=['model_name','uploaded_at']

admin.site.register(Uploads,UploadCusotmize)