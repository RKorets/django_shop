# Generated by Django 4.1 on 2022-08-21 11:30

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('yumyum', '0007_alter_category_update_at_last_news_viewsuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='update_at_last_news',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 21, 11, 30, 3, 522740)),
        ),
        migrations.CreateModel(
            name='CustomUserRegistration',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='yumyum.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
