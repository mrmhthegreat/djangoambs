from django.contrib import admin
from .models import Upload
# Register your models here.
class UploadCusotmize(admin.ModelAdmin):
    list_display=['model_name','uploaded_at']

admin.site.register(Upload,UploadCusotmize)