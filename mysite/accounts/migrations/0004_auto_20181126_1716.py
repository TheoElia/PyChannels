# Generated by Django 2.1 on 2018-11-26 17:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181126_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 26, 17, 16, 56, 930104, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reset_token',
            field=models.CharField(default='pbkdf2:sha256:50000$r9N8RunJ$13b287ede5e07b7fe3e4c29bc749c7bd483b74ababdd7dca618a47d8f27bbce9', max_length=1000),
        ),
        migrations.AlterField(
            model_name='patron',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$mITbZbQo$03878214bfe98397bacf067138deb263ee029d288ebca88222b0da75c2407aa8', max_length=1000),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$1T18kWI6$1d5070aa2680994352d6af31836e60adbd6d177514069b0439c9ce929afac6a8', max_length=1000),
        ),
    ]
