from django.shortcuts import render
import datetime
def hello(request):
    context = {}
    context['num'] = 1024
    context['name'] = 'Hello Django'
    context['date'] = datetime.datetime.now()
    context['label'] = "<a href='https://www.baidu.com/'>html a标签解析</a>"
    return render(request, 'dashboard.html', context)

# a页面用于测试模板include和继承
def extend(request):
    return render(request, 'a.html', {})