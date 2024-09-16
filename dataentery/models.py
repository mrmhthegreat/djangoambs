from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.CharField(max_length=5,unique=True,primary_key=True)
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    def __str__(self) -> str:
        return self.name
    