# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    category_id = models.IntegerField()
    author = models.CharField(max_length=50)
    book_copies = models.IntegerField()
    book_pub = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=50)
    copyright_year = models.IntegerField()
    date_receive = models.CharField(max_length=20)
    date_added = models.DateTimeField()
    status = models.CharField(max_length=30)
    classname=''

    class Meta:
        managed = False
        db_table = 'book'


class Borrow(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField()
    date_borrow = models.CharField(max_length=100)
    due_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrow'


class Borrowdetails(models.Model):
    borrow_details_id = models.AutoField(primary_key=True)
    book_id = models.IntegerField()
    borrow_id = models.IntegerField()
    borrow_status = models.CharField(max_length=50)
    date_return = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'borrowdetails'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class LostBook(models.Model):
    book_id = models.AutoField(db_column='Book_ID', primary_key=True)  # Field name made lowercase.
    isbn = models.IntegerField(db_column='ISBN')  # Field name made lowercase.
    member_no = models.CharField(db_column='Member_No', max_length=50)  # Field name made lowercase.
    date_lost = models.DateField(db_column='Date Lost')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_find = models.DateField(db_column='Date Find', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_new = models.DateField(db_column='Date New', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'lost_book'


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    year_level = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'member'


class Type(models.Model):
    borrowertype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'

class BorrowView(models.Model):
    borrow_id = models.IntegerField(primary_key=True)
    member_id = models.BigIntegerField()
    date_borrow = models.CharField(max_length=100)
    due_date = models.CharField(max_length=100, blank=True, null=True)
    borrow_details_id = models.IntegerField()
    book_id = models.IntegerField()
    borrow_status = models.CharField(max_length=50)
    date_return = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'borrow_view'
