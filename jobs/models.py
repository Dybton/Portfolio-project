from django.db import models

# Create your models here.


class Job(models.Model):  # The models.Model is something we have to pass in fro mthe import, a django thing
    # we can find different fieldtypes in the django documentation
    image = models.ImageField(upload_to='images/')
    # In the upload to field, we decide where we want it saved
    summary = models.CharField(max_length=200)
