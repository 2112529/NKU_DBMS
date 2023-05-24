from django.shortcuts import render,redirect
from django.http import HttpResponse

from app_test import models


def index_app(req):
    return HttpResponse('welcome to Django Test!')

def html_test(request):
    return render(request,"html_test.html")
def tpl_rule(request):
    name="poker"
    return render(request,'tpl_rule.html',{"name":name})

def something(request):
    print("用户请求的方式: " + request.method)

    # 2.[请求]在URL上传递值, 例如: http://123.249.26.154:5900/something/?n1=1&n2=2
    print(request.GET)

    # 3.[请求]在请求体中提交数据,目前是空值
    print(request.POST)

    return redirect("http://127.0.0.1:8000/tpl_rule/")



from app_test.models import Category
def orm_test(request):
    Category.objects.create(catid='c6',catname="总管")
    return HttpResponse("Hello,World!")



from django import forms

class UserLoginModelForm(forms.ModelForm):
    class Meta:
        model= models.Users
        fields=["username","password"]

class UserLogupModelForm(forms.ModelForm):
    class Meta:
        model= models.Users
        fields=["username","password","firstname","lastname"]



