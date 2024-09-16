from django.db import models
from django.conf import settings
# Create your models here.
class Upload(models.Model):
    file=models.FileField(upload_to='uploads')
    model_name=models.CharField(max_length=255)
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.model_name
    def full_path(self) -> str:
        return str(settings.BASE_DIR)+str( self.file.url)