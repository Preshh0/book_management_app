from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

class Book(models.Model):

    book_name = models.CharField(max_length=300)
    author = models.ForeignKey(get_user_model(), null = True, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    ISBN = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="photos", max_length=None, null = True)
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title