from django.db import models


# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(null=True)
