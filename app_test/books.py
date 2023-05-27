from django import forms
from django.shortcuts import render, HttpResponse, redirect
from app_test.models import Book
from app_test.views import ADD_BOOK_ModelForm


def book_info(request):
    book_info=Book.objects.values("book_id","book_title","author","publisher_name","isbn","status")

    return render(request,"book_info.html",{"book_info":book_info})

class ADD_BOOK_Form(ADD_BOOK_ModelForm):
    book_id=forms.IntegerField(
        label="Book ID",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=True,
    )
    book_title = forms.CharField(
        label="Book Title",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    category_id = forms.IntegerField(
        label="Category ID",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=True,
    )
    author = forms.CharField(
        label="Author",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    book_copies = forms.IntegerField(
        label="Book Copies",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=True,
    )
    book_pub = forms.CharField(
        label="Book Publication",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    publisher_name = forms.CharField(
        label="Publisher Name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    isbn = forms.CharField(
        label="ISBN",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    copyright_year = forms.IntegerField(
        label="Copyright Year",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=True,
    )
    date_added = forms.DateField(
        label="Date Added",
        widget=forms.DateInput(attrs={"class": "form-control"}),
        required=True,
    )
    status=forms.CharField(
        label="Status",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )


def add_book(request):
    """注册"""
    if request.method == "GET":
        form = ADD_BOOK_ModelForm()
        return render(request, 'add_book.html', {"form": form})

    form = ADD_BOOK_ModelForm(data=request.POST)
    if form.is_valid():

        admin_object = Book.objects.create(**form.cleaned_data)
        # 如果数据库中没有查询到数据
        if not admin_object:
            # 手动抛出错误显示在"password"字段下
            form.add_error("status", "Wrong!!!")
            return render(request, 'add_book.html', {"form": form})
        return render(request,"book_info.html")

    return render(request, 'add_book.html', {"form": form})

def edit_book(request):
    return render(request,"edit_book.html")

def delete_book(request):
    return render(request,"delete_book.html")