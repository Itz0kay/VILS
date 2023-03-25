from django.db import models

# Create your models here.
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.brand), str(instance.name) + filename])

class Content(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    category = models.CharField(max_length=200, blank=False, null=False)
    brand = models.CharField(max_length=200, blank=False, null=False)
    image = models.FileField(upload_to=nameFile, blank=False, null=False)
