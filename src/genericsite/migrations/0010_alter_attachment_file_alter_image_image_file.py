# Generated by Django 5.0.6 on 2024-05-18 19:47

import genericsite.common
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("genericsite", "0009_author_date_modified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="file",
            field=models.FileField(
                max_length=255,
                upload_to=genericsite.common.upload_to,
                verbose_name="file",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="image_file",
            field=models.ImageField(
                blank=True,
                height_field="height",
                null=True,
                upload_to=genericsite.common.upload_to,
                verbose_name="image file",
                width_field="width",
            ),
        ),
    ]
