# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LostBook(models.Model):
    book_id = models.AutoField(db_column='Book_ID', primary_key=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=50)  # Field name made lowercase.
    member_no = models.BigIntegerField(db_column='Member_No')  # Field name made lowercase.
    date_lost = models.DateField(db_column='Date Lost')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_find = models.DateField(db_column='Date Find', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_new = models.DateField(db_column='Date New', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

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
