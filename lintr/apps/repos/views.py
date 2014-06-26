#coding=utf-8
import os
import shutil
from django.conf import settings
from django.views.generic.edit import CreateView
from .models import Repository
from tasks.prepare.archive import unpack, ArchiveFormatError


class CreateRepoView(CreateView):
    model = Repository

    def _create_repo(self):
        """Create a repo on its place"""
        path = os.path.join(settings.REPOSITORY_STORAGE_ROOT, str(self.object.pk))
        os.makedirs(path)
        self.object.clone = path
        self.object.save()

    def populate_repo(self):
        raise NotImplemented

    def form_valid(self, form):
        response = super(CreateRepoView, self).form_valid(form)
        self._create_repo()
        self.populate_repo()
        return response


class CreateRepoUrlView(CreateRepoView):

    fields = 'url',
    success_url = '/'

    def populate_repo(self):
        pass


class CreateRepoFileView(CreateRepoView):

    fields = 'file',
    success_url = '/'

    def populate_repo(self):
        path = os.path.join(settings.REPOSITORY_STORAGE_ROOT, str(self.object.pk))

        # try to unpack incoming file if it is an archive or copy to the destination folder otherwise
        try:
            unpack(self.object.file.path, path)
        except ArchiveFormatError:
            shutil.copy(self.object.file.path, path)