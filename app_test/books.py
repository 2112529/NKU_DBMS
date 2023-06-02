from django import forms
from django.shortcuts import render, HttpResponse, redirect

from app_test import models
from app_test.models import Book, BorrowView,LostBook


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
        fields = ['book_title', 'category_id', 'author',  'publisher_name', 'isbn',  'status']
        widgets = {
            'book_title': forms.TextInput(attrs={'class': 'form-control'}),
            'category_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher_name': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }


from django.db import connection, IntegrityError


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
            category_id=form.cleaned_data['category_id']
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
            book.category_id=category_id
            book.author = author
            book.publisher_name = publisher_name
            book.isbn = isbn
            book.status = status

            try:
                book.save()
                with connection.cursor() as cursor:
                    cursor.callproc('insert_lost_book_plus', [book_id])
                print("Update completed")
            except IntegrityError:
                raise ValueError("Stored procedure violation occurred")
            book.save()
            return redirect('/book_info/')

            # with connection.cursor() as cursor:
            #     cursor.callproc('insert_lost_book_plus', [book_id])
            #
            # # 重定向到书籍列表页面或其他页面
            # return redirect('/book_info/')

    return render(request, 'edit_book.html', {'form': form, 'book_id': book_id})

import pymysql
from pymysql import cursors
from django.db import connection, transaction
def delete_book(request, book_id):
    book = Book.objects.get(book_id=book_id)
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='030523',
        db='library',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    if request.method == 'POST':
        # 删除数据库中的书籍
        #book.delete()
        try:
            # 开始事务
            with conn.cursor() as cursor:
                # 设置事务隔离级别
                cursor.execute('SET TRANSACTION ISOLATION LEVEL SERIALIZABLE')

                # 删除与之相关联的 lost_book 表中的数据
                cursor.execute('''
                        DELETE lost_book
                        FROM lost_book
                        JOIN book ON lost_book.Book_ID = book.book_id
                        WHERE book.book_id = %s
                    ''', (book_id,))

                # 删除与之相关联的 borrowdetails 表中的数据
                cursor.execute('''
                        DELETE borrowdetails
                        FROM borrowdetails
                        JOIN book ON borrowdetails.book_id = book.book_id
                        WHERE book.book_id = %s
                    ''', (book_id,))

                # 删除 book 表中的书籍
                cursor.execute('''
                        DELETE book
                        FROM book
                        WHERE book.book_id = %s
                    ''' , (book_id,))

                # 提交事务
                conn.commit()

                print("书籍删除成功")

        except Exception as e:
            # 发生异常，回滚事务
            conn.rollback()
            print("删除书籍时发生错误:", e)

        finally:
            # 关闭数据库连接
            conn.close()

        # 重定向到书籍列表页面或其他页面
        return redirect('/book_info/')

    return render(request, 'delete_book.html', {'book': book, 'book_id': book_id})

def borrow_info(request):
    filter_value = request.GET.get('value')  # 获取输入框的值
    borrows = BorrowView.objects.all()

    if filter_value:
        borrows = borrows.filter(borrow_status=filter_value)  # 根据输入框的值进行筛选

    context = {
        'borrow_info': borrows,
        'filter_value': filter_value  # 将筛选值传递给模板以便显示
    }
    return render(request, 'borrow_detail_info.html', context)


def lost_book_info(request):
    lost_book_info = LostBook.objects.all()

    return render(request, "lost_book.html", {"lost_book_info": lost_book_info})