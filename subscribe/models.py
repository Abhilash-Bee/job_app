from django.db import models

# Create your models here.
class Subscribe(models.Model):
    SUBSCRIBE_OPTION = [
        ('M', 'Monthly'),
        ('W', 'Weekly'),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    option = models.CharField(max_length=2, default='M', choices=SUBSCRIBE_OPTION)

    def __str__(self) -> str:
        return self.email