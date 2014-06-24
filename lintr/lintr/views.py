#coding=utf-8
from annoying.decorators import render_to
from apps.repos.views import CreateRepoUrlView, CreateRepoFileView

__author__ = 'x-eye'


@render_to('templates/lintr/index.html')
def index(request):
    url_view = CreateRepoUrlView(request=request, object=None)
    file_view = CreateRepoFileView(request=request, object=None)
    return {
        'url_form': url_view.get_form(url_view.get_form_class()),
        'file_form': file_view.get_form(file_view.get_form_class()),
    }