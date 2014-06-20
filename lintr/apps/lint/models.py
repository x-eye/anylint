from django.db import models
from django.conf import settings

_ = settings.GETTEXT

# Create your models here.


class FileType(models.Model):
    """File type lint model.

    Define means to handle different types of files
    """

    title = models.CharField(max_length=64)
    match = models.CharField(max_length=255)


class Lint(models.Model):
    """Particular lint descriptor"""

    title = models.CharField(max_length=64)
    command_template = models.TextField()


class LintSettings(models.Model):
    """Settings for file type and it's lint"""

    lint = models.ForeignKey(Lint)
    file_type = models.ForeignKey(FileType)
    options = models.TextField()

    class Meta:
        verbose_name_plural = _('Lint settings')

    def lint(self, filename):
        """Start lint procedure for file"""
        raise NotImplemented

