# Generated by Django 5.0.6 on 2024-05-26 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("genericsite", "0010_alter_attachment_file_alter_image_image_file"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "get_latest_by": "date_published",
                "verbose_name": "article",
                "verbose_name_plural": "articles",
            },
        ),
        migrations.CreateModel(
            name="ArticleSeries",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("slug", models.SlugField(verbose_name="slug")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sites.site",
                        verbose_name="site",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="series",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="genericsite.articleseries",
                verbose_name="series",
            ),
        ),
        migrations.AlterOrderWithRespectTo(
            name="article",
            order_with_respect_to="series",
        ),
    ]