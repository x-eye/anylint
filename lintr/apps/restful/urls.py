#coding=utf-8
from .views import code, session_task_status
from django.conf.urls import patterns, include, url

__author__ = 'x-eye'


urlpatterns = patterns('',
    url(r'/code', code),
    url(r'session-task-status', session_task_status)
)