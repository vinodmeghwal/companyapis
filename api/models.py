from django.db import models


# Create your models here.
class CompanyModel(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=50)
    location=models.TextField()
    picture =models.FileField(upload_to='company_pictures/', null=True, blank=True)