from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your models here.


#
# class People(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     page = models.CharField(max_length=200)
#     date = models.DateField()


# ----------------------------------------------------------------------
# ----------------Many to one---------------
# class Reporter(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)

# class Article(models.Model):
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=20)

# ----------------------------------------------


# -------------Many to many---------------------
#
# class Customer(models.Model):
#     cus_name = models.TextField(max_length=200)
#     cus_email = models.EmailField()
#     cus_mobile = models.TextField(max_length=10)
#
# class Products(models.Model):
#     cus_id = models.ManyToManyField(Customer)
#     pro_name = models.TextField(max_length=20)
#     pro_qty = models.TextField(max_length=200)
#
#
#
#
class Posts(models.Model):
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created = models.DateField()



class Creators(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    language = models.TextField()


class Aricle(models.Model):
    headline = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(Creators,on_delete=models.CASCADE)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline




















