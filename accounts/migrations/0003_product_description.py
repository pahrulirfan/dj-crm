# Generated by Django 3.1.7 on 2021-03-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
