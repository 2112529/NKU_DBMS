from django.contrib import admin
from django.urls import path
from app_test.views import index_app
from app_test import views
from app_test import account
from app_test import books
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', index_app),
    path('html_test/',views.html_test),
    path('tpl_rule/',views.tpl_rule),
    path('something/',views.something),
    path('login/',account.login),
    path('logup/',account.logup),
    path('orm_test/',views.orm_test),
    path('book_info/',views.book_info),
    path('mem_info/',account.mem_info),
    path('main/',views.main),
    path('add_emp/',views.add_emp),
    path('add_book/',books.add_book),
    path('edit_book/<int:book_id>/', books.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', books.delete_book, name='delete_book'),



]
