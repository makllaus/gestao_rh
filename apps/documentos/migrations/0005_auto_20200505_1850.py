# Generated by Django 2.1.5 on 2020-05-05 21:50

import apps.documentos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_documento_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(upload_to=apps.documentos.models.user_directory_path),
        ),
    ]