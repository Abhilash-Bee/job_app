from email.policy import default
from django.db import models
from django.utils.text import slugify


# Create your models here.

class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()

    def __str__(self) -> str:
        return self.state


class JobPost(models.Model):
    type_choices = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Internship', 'Internship'),
    ]

    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    salary = models.IntegerField()
    type = models.CharField(max_length=10, choices=type_choices, default='Full time')
    slug = models.SlugField(max_length=200, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
