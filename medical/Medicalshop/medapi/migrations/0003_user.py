# Generated by Django 2.2.28 on 2023-09-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapi', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
