# Generated by Django 2.2.28 on 2023-09-26 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medapi', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medicines',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]