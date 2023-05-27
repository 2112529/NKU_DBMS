from django import forms
from django.shortcuts import render, HttpResponse, redirect

from app_test import models
from app_test.models import Book



def book_info(request):
    book_info=Book.objects.values("book_id","book_title","author","publisher_name","isbn","status")

    return render(request,"book_info.html",{"book_info":book_info})
class ADD_BOOK_ModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ["book_id","book_title", "category_id", "author", "book_copies", "book_pub", "publisher_name", "isbn", "copyright_year", "date_added", "status"]

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


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_title',  'author',  'publisher_name', 'isbn',  'status']
        widgets = {
            'book_title': forms.TextInput(attrs={'class': 'form-control'}),

            'author': forms.TextInput(attrs={'class': 'form-control'}),

            'publisher_name': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),

            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }


def edit_book(request, book_id=None):
    if book_id:
        book = Book.objects.get(book_id=book_id)
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm()

    if request.method == 'POST':
        form = EditBookForm(request.POST)
        if form.is_valid():
            # 从表单中获取更新的数据
            book_title = form.cleaned_data['book_title']
            author = form.cleaned_data['author']
            publisher_name = form.cleaned_data['publisher_name']
            isbn = form.cleaned_data['isbn']
            status = form.cleaned_data['status']

            # 更新数据库中的书籍信息
            if book_id:
                book = Book.objects.get(book_id=book_id)
            else:
                book = Book()

            book.book_title = book_title
            book.author = author
            book.publisher_name = publisher_name
            book.isbn = isbn
            book.status = status
            book.save()

            # 重定向到书籍列表页面或其他页面
            return redirect('/book_info/')

    return render(request, 'edit_book.html', {'form': form, 'book_id': book_id})


def delete_book(request, book_id):
    book = Book.objects.get(book_id=book_id)

    if request.method == 'POST':
        # 删除数据库中的书籍
        book.delete()

        # 重定向到书籍列表页面或其他页面
        return redirect('/book_info/')

    return render(request, 'delete_book.html', {'book': book, 'book_id': book_id})