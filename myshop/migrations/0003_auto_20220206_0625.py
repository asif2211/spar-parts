# Generated by Django 3.2.12 on 2022-02-06 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20220206_0616'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items',
            new_name='item',
        ),
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
    ]
