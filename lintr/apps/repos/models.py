from django.db import models
from django.conf import settings

_ = settings.GETTEXT

# Create your models here.


class Repository(models.Model):
    """
    Repository information storage
    """

    url = models.URLField(_('Source repository URL'))
    clone = models.FilePathField(_('Repository clone root'), null=True, blank=True,
                                 path=settings.REPOSITORY_STORAGE_ROOT,
                                 allow_files=False, allow_folders=True)

    class Meta:
        verbose_name_plural = _('Repositories')
