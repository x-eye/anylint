from django.contrib import admin

# Register your models here.
from .models import FileType, Lint, LintSettings

admin.site.register(FileType)
admin.site.register(Lint)
admin.site.register(LintSettings)