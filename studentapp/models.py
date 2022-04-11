from django.db import models

# Create your models h
class studentmanagement(models.Model):
    rollno=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    fees=models.CharField(max_length=50)
    edit=models.CharField(max_length=50)
    delete=models.CharField(max_length=50)
