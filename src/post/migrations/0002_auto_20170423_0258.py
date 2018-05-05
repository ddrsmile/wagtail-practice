# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-23 02:58
from __future__ import unicode_literals

from django.db import migrations
import parts.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtail.core.fields.StreamField((('markdown', parts.blocks.MarkDownBlock()), ('code', wagtail.core.blocks.StructBlock((('language', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('cpp', 'C++'), ('java', 'Java'), ('python', 'Python'), ('python3', 'Python 3'), ('bash', 'Bash/Shell'), ('javascript', 'Javascript'), ('css', 'CSS'), ('html', 'HTML')], null=False)), ('caption', wagtail.core.blocks.CharBlock(blank=True, nullable=True, required=False)), ('code', parts.blocks.CodeTextBlock())))), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.RichTextBlock()), ('alignment', parts.blocks.ImageFormatChoiceBlock())), icon='image', label='Aligned image')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse')))),
        ),
    ]
