from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # 403报错
import json
# 表单
def search_form(request):
    return render(request, 'search.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    print('request', request)
    # json.dumps用来打印出jsonstr
    # return HttpResponse(json.dumps(request.body))
    print('request.body', request.body)
    return HttpResponse(json.dumps(request.POST))