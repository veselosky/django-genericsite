# Generated by Django 4.2.10 on 2024-04-21 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("genericsite", "0007_alter_article_options_alter_homepage_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="slug",
            field=models.SlugField(
                default="", help_text="e.g. 'samuel-clemens'", verbose_name="slug"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="article",
            name="date_modified",
            field=models.DateTimeField(
                blank=True,
                help_text="Time of last significant editorial update",
                null=True,
                verbose_name="date modified",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="date_published",
            field=models.DateTimeField(
                blank=True,
                help_text="Must be non-blank and in the past for page to be 'live'",
                null=True,
                verbose_name="date published",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="expires",
            field=models.DateTimeField(
                blank=True,
                help_text="Must be blank or in the future for page to be 'live'",
                null=True,
                verbose_name="expiration date",
            ),
        ),
        migrations.AlterField(
            model_name="attachment",
            name="custom_copyright_holder",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="custom copyright holder"
            ),
        ),
        migrations.AlterField(
            model_name="attachment",
            name="date_created",
            field=models.DateTimeField(
                blank=True,
                help_text="When the work was originally created.",
                null=True,
                verbose_name="date created",
            ),
        ),
        migrations.AlterField(
            model_name="attachment",
            name="upload_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="when uploaded"
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="date_modified",
            field=models.DateTimeField(
                blank=True,
                help_text="Time of last significant editorial update",
                null=True,
                verbose_name="date modified",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="date_published",
            field=models.DateTimeField(
                blank=True,
                help_text="Must be non-blank and in the past for page to be 'live'",
                null=True,
                verbose_name="date published",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="expires",
            field=models.DateTimeField(
                blank=True,
                help_text="Must be blank or in the future for page to be 'live'",
                null=True,
                verbose_name="expiration date",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="custom_copyright_holder",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="custom copyright holder"
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="date_created",
            field=models.DateTimeField(
                blank=True,
                help_text="When the work was originally created.",
                null=True,
                verbose_name="date created",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="height",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="height"
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="upload_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="when uploaded"
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="width",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="width"
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="date_modified",
            field=models.DateTimeField(
                blank=True,
                help_text="Time of last significant editorial update",
                null=True,
                verbose_name="date modified",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="date_published",
            field=models.DateTimeField(
                blank=True,
                help_text="Must be non-blank and in the past for page to be 'live'",
                null=True,
                verbose_name="date published",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="expires",
            field=models.DateTimeField(
                blank=True,
                help_text="Must be blank or in the future for page to be 'live'",
                null=True,
                verbose_name="expiration date",
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="date_modified",
            field=models.DateTimeField(
                blank=True,
                help_text="Time of last significant editorial update",
                null=True,
                verbose_name="date modified",
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="date_published",
            field=models.DateTimeField(
                blank=True,
                help_text="Must be non-blank and in the past for page to be 'live'",
                null=True,
                verbose_name="date published",
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="expires",
            field=models.DateTimeField(
                blank=True,
                help_text="Must be blank or in the future for page to be 'live'",
                null=True,
                verbose_name="expiration date",
            ),
        ),
    ]
