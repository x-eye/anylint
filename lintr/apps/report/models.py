from django.db import models
from django.conf import settings

# Create your models here.


class Report(models.Model):
    """Lint report log stored persistently"""

    created = models.DateTimeField(auto_now_add=True)
    contents = models.FileField(upload_to=settings.REPORTS_ROOT)