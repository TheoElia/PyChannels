# Generated by Django 2.1.5 on 2019-01-20 17:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20190113_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 20, 17, 32, 3, 272341, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 20, 17, 32, 3, 372105, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reset_token',
            field=models.CharField(default='pbkdf2:sha256:50000$vTTJR2N4$bf70f865449a73d76be51cc46c8d2aca1472440a90e98f5ec98e3a91ea4179cf', max_length=1000),
        ),
        migrations.AlterField(
            model_name='patron',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$37o7eo99$670a33ad4f2cf29144b9492e669c40359fe049208779447338a7d58a684b7b7f', max_length=1000),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$pttLK0KU$611c8c4023b1eff47ee790168e490aad9a0336662c2430e42cb5e7c77d9e0cec', max_length=1000),
        ),
    ]
