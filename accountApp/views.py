from django.shortcuts import render
# def account(request):
#     return render(request,'account.html')
# Create your views here.

#coding:utf-8

from django.shortcuts import render, HttpResponse, redirect

def account(request):

    error_msg = ''

    if request.method == "POST":

        user = request.POST.get('user', None) #避免提交空，时异常

        user = user.strip() #用户输入末尾有空格是去空格

        pwd = request.POST.get('pwd', None)

        if user == "root" and pwd == "123":

            print('user=' + user, 'pwd=' + pwd)

            return redirect("/home?user=")

        else:

            error_msg = "账号或者密码不对"

            print('user='+user, 'pwd='+pwd)

    return render(request, 'account.html',{'error_msg': error_msg})

 

def index(request):

    print (request.GET.items)

    return HttpResponse("welcome ..")