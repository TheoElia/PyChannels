# Generated by Django 2.1 on 2018-12-02 19:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20181202_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_online',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 19, 47, 42, 110253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 19, 47, 42, 48359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reset_token',
            field=models.CharField(default='pbkdf2:sha256:50000$XzoxL7mE$95b03a733e2e354c76c4b26043e43eb5ca742f35d614aaa229a3fe1e38fe910a', max_length=1000),
        ),
        migrations.AlterField(
            model_name='patron',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$btSoT7uv$4a9ac6622847a4f678663fbaf8960dc46b62f663d543d0eb391aa86033be9caf', max_length=1000),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$uuKfDKDL$ca25049a473b134bb7d8abc5a160fe593c4582472c670be2fa43a558ae02d060', max_length=1000),
        ),
    ]
