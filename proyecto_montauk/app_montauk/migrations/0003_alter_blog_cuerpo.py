# Generated by Django 4.0.6 on 2022-08-08 17:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_montauk', '0002_rename_subtítulo_blog_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
