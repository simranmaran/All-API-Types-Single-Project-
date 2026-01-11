# function based 
from django.db import models
class MovieFBV(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
#class based 
class MovieCBV(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class MovieMixin(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MovieGeneric(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MovieViewSetModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
