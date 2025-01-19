from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    short_description = models.TextField()
    criteria = models.TextField()
   
    organizer = models.CharField(max_length=100)
    contact_email = models.EmailField()
    max_attendees = models.PositiveIntegerField()
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return self.name