
from django.db import models


class ApiCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    location = models.CharField(max_length=40)
    owner_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'api_company'


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


class BiddersInfo(models.Model):
    tender_id = models.CharField(max_length=10)
    info = models.TextField()

    class Meta:
        managed = False
        db_table = 'bidders_info'


class Company(models.Model):
    name = models.TextField()
    location = models.TextField()
    owner_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'company'


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


class Login(models.Model):
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=40)
    usertype = models.CharField(db_column='userType', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'login'


class Product(models.Model):
    name = models.TextField()
    model = models.TextField()
    hourse_power = models.TextField()
    image = models.TextField()
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'product'


class ProductType(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'product_type'


class Registor(models.Model):
    name = models.TextField(db_collation='utf8_general_ci')
    company = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    registor = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'registor'


class Tender(models.Model):
    name = models.TextField(db_collation='utf8_general_ci')
    source = models.TextField(db_collation='utf8_general_ci')
    region = models.CharField(max_length=20)
    tender_no = models.TextField(db_collation='utf8_general_ci')
    type = models.CharField(max_length=10)
    title = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    phone_no = models.TextField(db_collation='utf8_general_ci')
    website = models.TextField(db_collation='utf8_general_ci')
    email = models.TextField(db_collation='utf8_general_ci')
    pobox = models.TextField(db_collation='utf8_general_ci')
    location = models.TextField(db_collation='utf8_general_ci')
    opening_date = models.CharField(max_length=15)
    closing_date = models.CharField(max_length=15)
    submit_date = models.DateTimeField()
    free = models.CharField(max_length=10)
    aprove_id = models.CharField(max_length=10)
    aprove_date = models.DateTimeField()
    auction = models.CharField(max_length=10)
    remove = models.CharField(max_length=10)
    bywhom = models.CharField(db_column='byWhom', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tender'


class TenderAuction(models.Model):
    tender_id = models.TextField()
    borrower = models.TextField(db_collation='utf8_general_ci')
    warranty = models.TextField(db_collation='utf8_general_ci')
    branch = models.TextField(db_collation='utf8_general_ci')
    type = models.TextField(db_collation='utf8_general_ci')
    map_no = models.TextField(db_collation='utf8_general_ci')
    boardnumber = models.TextField(db_collation='utf8_general_ci')
    factory = models.TextField(db_collation='utf8_general_ci')
    model = models.TextField(db_collation='utf8_general_ci')
    period = models.TextField(db_collation='utf8_general_ci')
    motor = models.TextField(db_collation='utf8_general_ci')
    fueltype = models.TextField(db_collation='utf8_general_ci')
    area = models.TextField(db_collation='utf8_general_ci')
    work = models.TextField(db_collation='utf8_general_ci')
    address = models.TextField(db_collation='utf8_general_ci')
    tplace = models.TextField(db_collation='utf8_general_ci')
    start = models.TextField(db_collation='utf8_general_ci')
    watch = models.TextField(db_collation='utf8_general_ci')

    class Meta:
        managed = False
        db_table = 'tender_auction'


class TenderCategoryList(models.Model):
    tender_id = models.CharField(max_length=10)
    tender_type_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tender_category_list'


class TenderCriteria(models.Model):
    tender_id = models.CharField(max_length=10)
    criteria = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tender_criteria'


class TenderList(models.Model):
    tender_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    quantity = models.TextField(db_collation='utf8_general_ci')
    detail = models.CharField(max_length=10)
    sequrity = models.TextField(db_collation='utf8_general_ci')

    class Meta:
        managed = False
        db_table = 'tender_list'


class TenderListDetail(models.Model):
    tender_list_id = models.CharField(max_length=10)
    type = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tender_list_detail'


class TenderNote(models.Model):
    tender_id = models.CharField(max_length=10)
    info = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tender_note'


class TenderPayment(models.Model):
    name = models.CharField(max_length=20)
    payment = models.CharField(max_length=10)
    length = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tender_payment'


class TenderType(models.Model):
    name = models.TextField(db_collation='utf8_general_ci')
    type_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tender_type'


class User(models.Model):
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    status = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    start = models.DateField()
    end = models.DateField()
    tp_type = models.CharField(max_length=10)
    allow = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'


class Work(models.Model):
    name = models.TextField(db_collation='utf8_general_ci')
    source = models.TextField(db_collation='utf8_general_ci')
    region = models.CharField(max_length=20, db_collation='utf8_general_ci')
    type = models.CharField(max_length=10, db_collation='utf8_general_ci')
    title = models.TextField(db_collation='utf8_general_ci', blank=True, null=True)
    company_name = models.TextField(db_collation='utf8_general_ci')
    work_name = models.TextField(db_collation='utf8_general_ci')
    level = models.TextField(db_collation='utf8mb4_general_ci')
    payment = models.TextField(db_collation='utf8_general_ci')
    work_no = models.TextField(db_collation='utf8_general_ci')
    extra_skill = models.TextField(db_collation='utf8_general_ci')
    work_experience = models.TextField(db_collation='utf8_general_ci')
    quantity = models.TextField(db_collation='utf8_general_ci')
    learning_level = models.TextField(db_collation='utf8_general_ci')
    until = models.DateField()
    phone_no = models.TextField(db_collation='utf8_general_ci')
    website = models.TextField(db_collation='utf8_general_ci')
    email = models.TextField(db_collation='utf8_general_ci')
    pobox = models.TextField(db_collation='utf8_general_ci')
    location = models.TextField(db_collation='utf8_general_ci')
    submit_date = models.DateTimeField()
    aprove_id = models.CharField(max_length=10)
    aprove_date = models.DateTimeField()
    remove = models.CharField(max_length=10)
    remove_date = models.DateTimeField()
    remove_id = models.CharField(max_length=10)
    aprove = models.CharField(max_length=10)
    bywhom = models.CharField(db_column='byWhom', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'work'


class WorkCategory(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'work_category'


class WorkCategoryList(models.Model):
    work_id = models.CharField(max_length=10)
    work_type_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'work_category_list'


class WorkCriteria(models.Model):
    work_id = models.CharField(max_length=10)
    criteria = models.TextField(db_collation='utf8_general_ci')

    class Meta:
        managed = False
        db_table = 'work_criteria'


class WorkDetail(models.Model):
    work_id = models.CharField(max_length=10)
    detail = models.TextField()

    class Meta:
        managed = False
        db_table = 'work_detail'


class WorkSubcategory(models.Model):
    category_id = models.CharField(max_length=10)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'work_subcategory'


class WorkerAdmin(models.Model):
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'worker_admin'


class Workers(models.Model):
    company_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    remove = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'workers'