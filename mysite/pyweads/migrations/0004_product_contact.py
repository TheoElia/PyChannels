# Generated by Django 2.1.4 on 2018-12-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyweads', '0003_product_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contact',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
