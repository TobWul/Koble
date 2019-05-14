from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from filters.models import Filter
from reviews.models import Review


class Gym(models.Model):
    name = models.CharField(max_length=400)
    about = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    opening_hours = models.TextField(null=True, blank=True)
    contact_information = models.TextField(null=True, blank=True)
    positive_filter = models.ManyToManyField(Filter, related_name="positive_filter")
    negative_filter = models.ManyToManyField(Filter, related_name="negative_filter")
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.name


class GymImage(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='gym/',
                                          processors=[ResizeToFit(500, 500, False)],
                                          format='JPEG',
                                          options={'quality': 85})
