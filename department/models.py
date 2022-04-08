from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=150)
    department_desc = models.CharField(max_length=500)
    
