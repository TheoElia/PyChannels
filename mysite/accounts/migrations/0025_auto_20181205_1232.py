# Generated by Django 2.1.4 on 2018-12-05 12:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20181205_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 5, 12, 32, 34, 500020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 5, 12, 32, 34, 501946, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reset_token',
            field=models.CharField(default='pbkdf2:sha1:1000$LcaBJasG$c0b48f12bad995e5245503a511c4692aee09f0f7', max_length=1000),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/static/accounts/uploads'),
        ),
        migrations.AlterField(
            model_name='patron',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha1:1000$zHogt4ju$763c2a0f95f1c579f98d85ed8baad1996347b801', max_length=1000),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha1:1000$yrgPIIU4$b8a805af0e3682f2afa3f8c8469c4abd3195b27b', max_length=1000),
        ),
    ]
