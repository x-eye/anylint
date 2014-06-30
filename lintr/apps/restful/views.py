#coding=utf-8
from annoying.decorators import ajax_request
from django.http.response import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


__author__ = 'x-eye'


@csrf_exempt
@ajax_request
def code(request):
    # todo:
    # validate url
    if request.method == "POST":
        return {"request_id": 1}
    else:
        return HttpResponseNotAllowed(['POST'])

# todo: in task
# git clone
# classify

@csrf_exempt
@ajax_request
def session_task_status(request):
    """
    Possible stages::

        - initial: client just entered the site
        - clear: no tasks requested
        - registering: passed URL IS BEING registered and classified
        - classified: passed URL HAS BEEN registered and classified
        - configured: automatic settings has been manually adjusted
        - processing: code lint in progress
        - ready: code lint is complete, results available by URL
    """
    # todo: state checker
    # return current state for session
    # return intermediate results
    return {
        'stage': request.session.setdefault('stage', 'initial')
    }