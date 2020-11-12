from django.shortcuts import render
import datetime
def runoob(request):
    context = {}
    context['date'] = datetime.datetime.now()
    return render(request, 'dashboard.html', context)

def hello(request):
    context = {}
    context['date'] = datetime.datetime.now()
    context['label'] = "<a href='https://www.baidu.com/'>html a标签解析</a>"
    return render(request, 'dashboard.html', context)