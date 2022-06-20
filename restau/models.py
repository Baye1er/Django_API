from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
from django.urls import reverse


class Restau(models.Model):
    restau_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, blank=True)
    zip_code = models.IntegerField(blank=False, default=0)
    website = models.URLField(max_length=420, blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\221?\d{9,10}$')], max_length=10, blank=True)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=254, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.restau_name}, {self.city}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
