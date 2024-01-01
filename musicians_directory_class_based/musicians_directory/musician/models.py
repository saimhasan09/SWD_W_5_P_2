from django.db import models


# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    instrument_type =[
        ('guitar', 'Guitar'),
        ('piano', 'Piano'),
        ('violin', 'Violin'),
        ('drums', 'Drums'),
    ]
    instrument = models.CharField(max_length=10, choices=instrument_type)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
