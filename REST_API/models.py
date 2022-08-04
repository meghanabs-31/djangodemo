from django.db import models
# Create your models here.
class Employeedetail(models.Model):
    fullname = models.CharField(max_length=20)
    emp_code = models.CharField(max_length=5)
    mobile = models.CharField(max_length=10)
    skill = models.CharField(max_length=200, blank=True)
