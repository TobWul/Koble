from django.db import models
from django.template.defaultfilters import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from filters.models import Filter, NegativeFilter
from reviews.models import Review


class Gym(models.Model):
    name = models.CharField(max_length=400)
    about = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    opening_hours = models.TextField(null=True, blank=True)
    contact_information = models.TextField(null=True, blank=True)
    positive_filter = models.ManyToManyField(Filter, blank=True)
    negative_filter = models.ManyToManyField(NegativeFilter, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Only set the slug when the object is created.
            self.slug = slugify(self.name)  # Does not update to make sure links doesn't get broken
        super(Gym, self).save(*args, **kwargs)


class GymImage(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='gym/',
                                          processors=[ResizeToFit(500, 500, False)],
                                          format='JPEG',
                                          options={'quality': 85})
