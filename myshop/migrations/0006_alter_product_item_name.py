# Generated by Django 3.2.12 on 2022-02-06 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0005_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.item'),
        ),
    ]