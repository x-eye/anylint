#coding=utf-8
from django.conf.urls import patterns, include, url
from apps.repos.views import CreateRepoUrlView, CreateRepoFileView

__author__ = 'x-eye'


urlpatterns = patterns('',
    url(r'url-create', CreateRepoUrlView.as_view()),
    url(r'file-create', CreateRepoFileView.as_view()),
)