# Generated by Django 3.2.12 on 2022-02-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_auto_20220206_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
            ],
        ),
    ]