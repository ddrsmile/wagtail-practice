# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0030_index_on_pagerevision_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='post date')),
                ('body', wagtail.wagtailcore.fields.StreamField((('carousel', wagtail.wagtailcore.blocks.StructBlock((('carousel_title', wagtail.wagtailcore.blocks.CharBlock()), ('button', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('arrow', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), ('images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock(required=False)))), icon='image'))))), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(blank=False, choices=[('cpp', 'C++'), ('python', 'Python'), ('java', 'Java')], default='python', null=False)), ('code', wagtail.wagtailcore.blocks.TextBlock()))))))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]