from django.db import models

# Create your models here.

class Ebook(models.Model):
    title=models.CharField(max_length=100)
    rating=models.FloatField()
    video=models.CharField(max_length=3000)
    des=models.CharField(max_length=2000,default="asdfghjklertyuiopzxcvbnm")

    def __str__(self):
        return self.title

class cartitems(models.Model):
    des=models.CharField(max_length=4000,null=True)
    title=models.CharField(max_length=60,null=True)
    price=models.FloatField(null=True)

class searchitem(models.Model):
    title=models.CharField(max_length=100,null=True)
    rating=models.FloatField(null=True)
    video=models.CharField(max_length=3000,null=True)
    des=models.CharField(max_length=20,null=True)