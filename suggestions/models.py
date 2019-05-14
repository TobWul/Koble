from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from authentication.models import Profile
from filters.models import Filter


class Suggestion(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    filters = models.ManyToManyField(Filter, blank=True)
    why_wheelchair_friendly = models.TextField(blank=True)
    additional_information = models.TextField(blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    image = ProcessedImageField(upload_to='gym/',
                                processors=[ResizeToFit(500, 500, False)],
                                format='JPEG',
                                options={'quality': 85},
                                blank=True)

    def __str__(self):
        return self.name

