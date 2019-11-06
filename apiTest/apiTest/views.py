from django.http import HttpResponse
import json


def hello(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        result = dict()
        result['username'] = username
        print(username)
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    elif request.method == "GET":
        result = dict()
        result['user'] = "hello"
        result['mobileNum'] = "hello"
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')