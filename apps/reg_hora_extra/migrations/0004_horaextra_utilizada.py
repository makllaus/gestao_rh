# Generated by Django 2.1.5 on 2020-05-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_hora_extra', '0003_horaextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='horaextra',
            name='utilizada',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
