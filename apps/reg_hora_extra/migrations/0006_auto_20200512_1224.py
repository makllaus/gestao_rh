# Generated by Django 2.1.5 on 2020-05-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_hora_extra', '0005_auto_20200512_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]
