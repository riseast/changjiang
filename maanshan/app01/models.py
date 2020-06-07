from django.db import models

# Create your models here.

class app01_emp(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()


class ebook(models.Model):
    id=models.AutoField(primary_key=True)
    tile=models.CharField(max_length=20,unique=True)
    pub_date=models.DateField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    publish=models.CharField(max_length=32)