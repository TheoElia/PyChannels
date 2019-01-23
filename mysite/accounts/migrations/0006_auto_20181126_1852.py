# Generated by Django 2.1 on 2018-11-26 18:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181126_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 26, 18, 52, 58, 395349, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reset_token',
            field=models.CharField(default='pbkdf2:sha256:50000$XRpGAEov$640fd73ccabe0a2d4fe6ef3184cc57be439f841a2b6d7fad943d6fb1c84338a5', max_length=1000),
        ),
        migrations.AlterField(
            model_name='patron',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$TwpmumFX$56070ce12b56605afad06cec20bf9bd235899d81b39cf2337081443ebd5972b3', max_length=1000),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$0zt6V6ze$2b651278f66bbe9b84c882b191fcb59a04679a3e8ceed4b408595bd9acf5f301', max_length=1000),
        ),
    ]