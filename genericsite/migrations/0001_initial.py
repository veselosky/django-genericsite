# Generated by Django 4.0.5 on 2022-07-09 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('status', models.CharField(choices=[('withheld', 'Draft (withheld)'), ('usable', 'Publish (usable)'), ('cancelled', 'Unpublish (cancelled)')], db_index=True, default='usable', max_length=50, verbose_name='status')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('base_template', models.CharField(default='base.html', max_length=255, verbose_name='base template')),
                ('content_template', models.CharField(default='genericsite/article_detail.html', max_length=255, verbose_name='content body template')),
                ('body', tinymce.models.HTMLField(blank=True, verbose_name='body content')),
                ('published_time', models.DateTimeField(blank=True, db_index=True, help_text="Must be non-blank and in the past for page to be 'live'", null=True, verbose_name='published time')),
                ('modified_time', models.DateTimeField(blank=True, db_index=True, help_text='Time of last significant editorial update', null=True, verbose_name='modified time')),
                ('expiration_time', models.DateTimeField(blank=True, db_index=True, help_text="Must be blank or in the future for page to be 'live'", null=True, verbose_name='expiration time')),
                ('type', models.CharField(default='website', help_text='Open Graph type, see https://ogp.me', max_length=50, verbose_name='opengraph type')),
                ('seo_title', models.CharField(blank=True, max_length=255, verbose_name='SEO title override')),
                ('seo_description', models.CharField(blank=True, max_length=255, verbose_name='SEO description override')),
                ('custom_copyright_notice', tinymce.models.HTMLField(blank=True, help_text='include a pair of curly braces {} where you want the year inserted', verbose_name='custom copyright notice')),
                ('custom_icon', models.CharField(blank=True, help_text='<a href=https://icons.getbootstrap.com/#icons target=iconlist>icon list</a>', max_length=50, verbose_name='custom icon')),
                ('locale', models.CharField(default='en_US', max_length=10, verbose_name='locale')),
                ('images', models.ManyToManyField(blank=True, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='images')),
                ('og_image', filer.fields.image.FilerImageField(blank=True, help_text='Image for social sharing', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL)),
                ('site', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sites.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'section',
                'verbose_name_plural': 'sections',
                'ordering': ['-published_time'],
                'get_latest_by': 'published_time',
                'abstract': False,
                'unique_together': {('site', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('status', models.CharField(choices=[('withheld', 'Draft (withheld)'), ('usable', 'Publish (usable)'), ('cancelled', 'Unpublish (cancelled)')], db_index=True, default='usable', max_length=50, verbose_name='status')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('base_template', models.CharField(default='base.html', max_length=255, verbose_name='base template')),
                ('content_template', models.CharField(default='genericsite/article_detail.html', max_length=255, verbose_name='content body template')),
                ('body', tinymce.models.HTMLField(blank=True, verbose_name='body content')),
                ('published_time', models.DateTimeField(blank=True, db_index=True, help_text="Must be non-blank and in the past for page to be 'live'", null=True, verbose_name='published time')),
                ('modified_time', models.DateTimeField(blank=True, db_index=True, help_text='Time of last significant editorial update', null=True, verbose_name='modified time')),
                ('expiration_time', models.DateTimeField(blank=True, db_index=True, help_text="Must be blank or in the future for page to be 'live'", null=True, verbose_name='expiration time')),
                ('type', models.CharField(default='website', help_text='Open Graph type, see https://ogp.me', max_length=50, verbose_name='opengraph type')),
                ('seo_title', models.CharField(blank=True, max_length=255, verbose_name='SEO title override')),
                ('seo_description', models.CharField(blank=True, max_length=255, verbose_name='SEO description override')),
                ('custom_copyright_notice', tinymce.models.HTMLField(blank=True, help_text='include a pair of curly braces {} where you want the year inserted', verbose_name='custom copyright notice')),
                ('custom_icon', models.CharField(blank=True, help_text='<a href=https://icons.getbootstrap.com/#icons target=iconlist>icon list</a>', max_length=50, verbose_name='custom icon')),
                ('locale', models.CharField(default='en_US', max_length=10, verbose_name='locale')),
                ('admin_name', models.CharField(help_text='Name used in the admin to distinguish from other home pages', max_length=255, verbose_name='admin name')),
                ('images', models.ManyToManyField(blank=True, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='images')),
                ('og_image', filer.fields.image.FilerImageField(blank=True, help_text='Image for social sharing', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL)),
                ('site', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sites.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'home page',
                'verbose_name_plural': 'home pages',
                'ordering': ['-published_time'],
                'get_latest_by': 'published_time',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteVar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('value', models.TextField(verbose_name='value')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vars', to='sites.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'sitevar',
                'verbose_name_plural': 'sitevars',
                'base_manager_name': 'objects',
                'unique_together': {('site', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('status', models.CharField(choices=[('withheld', 'Draft (withheld)'), ('usable', 'Publish (usable)'), ('cancelled', 'Unpublish (cancelled)')], db_index=True, default='usable', max_length=50, verbose_name='status')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('base_template', models.CharField(default='base.html', max_length=255, verbose_name='base template')),
                ('content_template', models.CharField(default='genericsite/article_detail.html', max_length=255, verbose_name='content body template')),
                ('body', tinymce.models.HTMLField(blank=True, verbose_name='body content')),
                ('published_time', models.DateTimeField(blank=True, db_index=True, help_text="Must be non-blank and in the past for page to be 'live'", null=True, verbose_name='published time')),
                ('modified_time', models.DateTimeField(blank=True, db_index=True, help_text='Time of last significant editorial update', null=True, verbose_name='modified time')),
                ('expiration_time', models.DateTimeField(blank=True, db_index=True, help_text="Must be blank or in the future for page to be 'live'", null=True, verbose_name='expiration time')),
                ('type', models.CharField(default='website', help_text='Open Graph type, see https://ogp.me', max_length=50, verbose_name='opengraph type')),
                ('seo_title', models.CharField(blank=True, max_length=255, verbose_name='SEO title override')),
                ('seo_description', models.CharField(blank=True, max_length=255, verbose_name='SEO description override')),
                ('custom_copyright_notice', tinymce.models.HTMLField(blank=True, help_text='include a pair of curly braces {} where you want the year inserted', verbose_name='custom copyright notice')),
                ('custom_icon', models.CharField(blank=True, help_text='<a href=https://icons.getbootstrap.com/#icons target=iconlist>icon list</a>', max_length=50, verbose_name='custom icon')),
                ('locale', models.CharField(default='en_US', max_length=10, verbose_name='locale')),
                ('images', models.ManyToManyField(blank=True, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='images')),
                ('og_image', filer.fields.image.FilerImageField(blank=True, help_text='Image for social sharing', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL)),
                ('site', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sites.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
                'ordering': ['-published_time'],
                'get_latest_by': 'published_time',
                'abstract': False,
                'unique_together': {('site', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('status', models.CharField(choices=[('withheld', 'Draft (withheld)'), ('usable', 'Publish (usable)'), ('cancelled', 'Unpublish (cancelled)')], db_index=True, default='usable', max_length=50, verbose_name='status')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('base_template', models.CharField(default='base.html', max_length=255, verbose_name='base template')),
                ('content_template', models.CharField(default='genericsite/article_detail.html', max_length=255, verbose_name='content body template')),
                ('body', tinymce.models.HTMLField(blank=True, verbose_name='body content')),
                ('published_time', models.DateTimeField(blank=True, db_index=True, help_text="Must be non-blank and in the past for page to be 'live'", null=True, verbose_name='published time')),
                ('modified_time', models.DateTimeField(blank=True, db_index=True, help_text='Time of last significant editorial update', null=True, verbose_name='modified time')),
                ('expiration_time', models.DateTimeField(blank=True, db_index=True, help_text="Must be blank or in the future for page to be 'live'", null=True, verbose_name='expiration time')),
                ('seo_title', models.CharField(blank=True, max_length=255, verbose_name='SEO title override')),
                ('seo_description', models.CharField(blank=True, max_length=255, verbose_name='SEO description override')),
                ('custom_copyright_notice', tinymce.models.HTMLField(blank=True, help_text='include a pair of curly braces {} where you want the year inserted', verbose_name='custom copyright notice')),
                ('custom_icon', models.CharField(blank=True, help_text='<a href=https://icons.getbootstrap.com/#icons target=iconlist>icon list</a>', max_length=50, verbose_name='custom icon')),
                ('locale', models.CharField(default='en_US', max_length=10, verbose_name='locale')),
                ('type', models.CharField(default='article', help_text='Open Graph type, see https://ogp.me', max_length=50, verbose_name='type')),
                ('author_display_name', models.CharField(blank=True, help_text="e.g. 'Dr. Samuel Clemens, Phd.'", max_length=255, verbose_name='author name, as displayed')),
                ('author_profile_url', models.URLField(blank=True, max_length=255, verbose_name='author URL')),
                ('images', models.ManyToManyField(blank=True, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='images')),
                ('og_image', filer.fields.image.FilerImageField(blank=True, help_text='Image for social sharing', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='genericsite.section', verbose_name='section')),
                ('site', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sites.site', verbose_name='site')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'article page',
                'verbose_name_plural': 'article pages',
                'ordering': ['-published_time'],
                'get_latest_by': 'published_time',
                'abstract': False,
                'unique_together': {('site', 'section', 'slug')},
            },
        ),
    ]
