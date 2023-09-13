from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=120)
    location = models.CharField(max_length=70)
    date = models.CharField(max_length=120)
    description = models.TextField(max_length=120)
    def __str__(self):
        return self.event_title

class Eventappl(models.Model) :
    full_name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    number=models.IntegerField()
    event = models.ForeignKey('Event',on_delete=models.CASCADE)


