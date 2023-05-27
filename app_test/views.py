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

def main(request):
    return render(request,"Outer_welcome.html")

from django.shortcuts import render
from app_test.models import Book

def book_info(request):
    filter_value = request.GET.get('value')  # 获取输入框的值
    books = Book.objects.all()

    if filter_value:
        books = books.filter(status=filter_value)  # 根据输入框的值进行筛选

    context = {
        'book_info': books,
        'filter_value': filter_value  # 将筛选值传递给模板以便显示
    }
    return render(request, 'book_info.html', context)

def add_emp(request):
    return render(request,'add_emp.html')


class ADD_BOOK_ModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ["book_id","book_title", "category_id", "author", "book_copies", "book_pub", "publisher_name", "isbn", "copyright_year", "date_added", "status"]

