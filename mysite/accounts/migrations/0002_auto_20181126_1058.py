# Generated by Django 2.1 on 2018-11-26 10:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 26, 10, 58, 19, 173886, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reset_token',
            field=models.CharField(default='pbkdf2:sha256:50000$dN0NSbsB$2dc346ebb424132558286ae1a744eade16fe88b6be61063dcceb604a30453d05', max_length=1000),
        ),
        migrations.AlterField(
            model_name='patron',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$A4jz7PQl$9660fa4607cf8ee6817b698bf227540145f25b2121fe17d8f8cefd8b23838b82', max_length=1000),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$W4LBuZ9q$3dd11e30c92f13860044095f08b453b3e757be188e9e6eb6b6fb5af033ea45be', max_length=1000),
        ),
    ]