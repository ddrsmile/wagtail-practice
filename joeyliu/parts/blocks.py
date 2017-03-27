from __future__ import absolute_import, unicode_literals

# django
from django import forms
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.forms import Media, widgets
from django.utils.functional import cached_property

# wagtail
from wagtail.wagtailcore.blocks import (TextBlock, 
                                        StructBlock, 
                                        StreamBlock, 
                                        FieldBlock, 
                                        CharBlock, 
                                        RichTextBlock, 
                                        RawHTMLBlock, 
                                        ChoiceBlock)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

# external
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

LANGUAGES = ( 
    ('cpp', 'C++'),
    ('python','Python'),
    ('python3', 'Python 3'),
    ('java', 'Java'),
    ('bash', 'Bash/Shell'),
    ('html', 'HTML'),
)

class CodeBlock(StructBlock):
    language = ChoiceBlock(choices=LANGUAGES, blank=False, null=False, default='python')
    code = TextBlock()

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass='code-hightlight',
            style='tango',
            noclasses=False,
        )
        return mark_safe(highlight(src, lexer, formatter))

    class Meta:
        # template="parts/blocks/code.html"
        icon="code"

class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"

class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))

class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), ('full', 'Full width'),
    ))

class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()

class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"

class BlogStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    code = CodeBlock()
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    pullquote = PullQuoteBlock()
    aligned_html = AlignedHTMLBlock(icon="code", label='Raw HTML')
    document = DocumentChooserBlock(icon="doc-full-inverse")