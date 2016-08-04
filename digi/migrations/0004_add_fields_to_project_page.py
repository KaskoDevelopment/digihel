# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-04 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('digi', '0003_rename_project_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='theme',
        ),
        migrations.AddField(
            model_name='projectpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
