from django.contrib import admin
from django.urls import path
from app_test.views import index_app
from app_test import views
from app_test import account
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', index_app),
    path('html_test/',views.html_test),
    path('tpl_rule/',views.tpl_rule),
    path('something/',views.something),
    path('login/',account.login),
    path('logup/',account.logup),
    path('orm_test/',views.orm_test),
    path('book_info/',account.book_info),
]
