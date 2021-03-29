from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    #context = {}
    #return render(request,'hello.html',context)
    return HttpResponse("<h1>你好，zhzh</h1>")

def hellozhzh(request):
    context = {}    # 创建需要传给模板的变量的数组，哦，不对，这个叫字典。
    context['hello'] = 'hello zhzh !'
    return render(request,'hellozhzh.html',context) # 将hellozhzh.html这个页面渲染出来。
