# Generated by Django 2.1 on 2018-12-02 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20181202_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 21, 1, 18, 910918, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 21, 1, 18, 961816, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reset_token',
            field=models.CharField(default='pbkdf2:sha256:50000$fpJvujJR$c84d31a773db9d1aa02f266cb298cb73ff6ceaedf5f323a4f82480417c43e7ff', max_length=1000),
        ),
        migrations.AlterField(
            model_name='patron',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$b4TOdrGP$aef71866681d4b01766d2d3b0bc86d0d427b042c774e3c2504575bb7d134be31', max_length=1000),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$rccn6IsN$1aa412487432c337413213cb27e92af882567ce1045530b58746b0a6cba8debd', max_length=1000),
        ),
    ]
