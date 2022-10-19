from django.db import models
from django.utils.text import slugify


# Create your models here.

class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    salary = models.IntegerField()
    slug = models.SlugField(max_length=200, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.title} with {self.salary}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
