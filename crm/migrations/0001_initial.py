# Generated by Django 5.0.9 on 2024-10-17 11:43

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')),
                ('role', models.CharField(choices=[('admin', 'Administrator'), ('moderator', 'Moderator'), ('teacher', "O'qituvchi"), ('student', "O'quvchi")], default='student', max_length=15, verbose_name='Rol')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user/', verbose_name='Rasm')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Foydalanuvchilar',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')),
                ('title', models.CharField(max_length=100, verbose_name='Kurs nomi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Kurs tavsifi')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name="O'qituvchi")),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurslar',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.course', verbose_name='Kurs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': "Ro'yxatdan o'tish",
                'verbose_name_plural': "Ro'yxatdan o'tishlar",
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')),
                ('title', models.CharField(max_length=255, verbose_name='Dars nomi')),
                ('content', models.FileField(blank=True, null=True, upload_to='lesson/', verbose_name="Qo'shimcha fayl")),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.course', verbose_name='Kurs')),
            ],
            options={
                'verbose_name': 'Dars',
                'verbose_name_plural': 'Darslar',
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')),
                ('title', models.CharField(max_length=255, verbose_name='Vazifa nomi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Vazifa tavsifi')),
                ('content', models.FileField(blank=True, null=True, upload_to='assignment/', verbose_name="Qo'shimcha fayl")),
                ('due_date', models.DateTimeField(verbose_name='Topshirish muddati')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.lesson', verbose_name='Dars')),
            ],
            options={
                'verbose_name': 'Vazifa',
                'verbose_name_plural': 'Vazifalar',
            },
        ),
    ]
