# Generated by Django 2.2.28 on 2023-09-27 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medapi', '0007_medicine_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]