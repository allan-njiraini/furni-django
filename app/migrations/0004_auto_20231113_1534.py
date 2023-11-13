# Generated by Django 3.2.21 on 2023-11-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_chair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chair',
            name='image',
            field=models.ImageField(upload_to='products/Products'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='image',
            field=models.ImageField(upload_to='products/staff/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/Product/'),
        ),
    ]