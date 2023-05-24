from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app_test import views
from app_test.views import UserLoginModelForm
from app_test.views import UserLogupModelForm


from app_test.models import Users
from app_test.models import Book



def book_info(request):
    book_info=Book.objects.all()

    return render(request,"book_info.html",{"book_info":book_info})
