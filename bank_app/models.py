from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()


    def __str__(self):
        return self.name


class Team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()


    def __str__(self):
        return self.name



class Register(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    password=models.TextField()
    Cpassword=models.TextField()



    def __str__(self):
        return self.name


class Login(models.Model):

    email = models.EmailField(max_length=250)
    password = models.TextField()


    def __str__(self):
        return self.name


class Logout(models.Model):
    email = models.EmailField(max_length=250)
    password = models.TextField()

    def __str__(self):
        return self.name