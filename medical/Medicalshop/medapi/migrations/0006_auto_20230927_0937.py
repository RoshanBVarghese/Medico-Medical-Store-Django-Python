# Generated by Django 2.2.28 on 2023-09-27 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medapi', '0005_medicines_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medicines',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
