# Generated by Django 2.1.5 on 2020-05-16 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_antiga', '0002_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
