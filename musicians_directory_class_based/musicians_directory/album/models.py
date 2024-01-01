from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=20)
    musician_name = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    rating_choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(choices=rating_choices)

    def __str__(self):
        return self.name