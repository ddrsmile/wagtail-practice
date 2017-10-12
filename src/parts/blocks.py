from __future__ import absolute_import, unicode_literals
# django
from django import forms
from django.utils.safestring import mark_safe
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
# 3rd party
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name
from markdown import markdown
# customization
from parts.widgets import MarkDownWidget, CodeTextWidget

LANGUAGES = ( 
    ('cpp', 'C++'),
    ('java', 'Java'),
    ('python','Python'),
    ('python3', 'Python 3'),
    ('bash', 'Bash/Shell'),
    ('javascript', 'Javascript'),
    ('css', "CSS"),
    ('html', "HTML"),
)

class CodeChoiceBlock(ChoiceBlock):
    def __init__(self, choices=None, default=None, required=True, help_text=None, **kwargs): 
        super(CodeChoiceBlock, self).__init__(choices=choices, 
                                              default=default, 
                                              required=required, 
                                              help_text=help_text, 
                                              **kwargs)
        self.field.widget.attrs.update({'onchange': 'update_code_mode(this)'})

class CodeTextBlock(TextBlock):
    @cached_property
    def field(self):
        field_kwargs = {
            'widget': CodeTextWidget(),
        }
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)

class CodeBlock(StructBlock):
    language = CodeChoiceBlock(choices=LANGUAGES, blank=False, null=False, default='python')
    caption = CharBlock(required=False, blank=True, nullable=True)
    code = CodeTextBlock()

    def render(self, value, *args, **kwargs):
        src = value['code'].strip('\n')
        caption = value['caption'].strip()
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass='codehilite',
            style='xcode',
            noclasses=False,
        )
        render_content = highlight(src, lexer, formatter)
        if caption:
            caption_content = '<div class="code-caption">{}</div>\n'.format(caption)
            render_content = caption_content + render_content

        return mark_safe(render_content)

    class Meta:
        icon="code"

class MarkDownBlock(TextBlock):
    @cached_property
    def field(self):
        field_kwargs = {
            'widget': MarkDownWidget(),
        }
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)
    
    def render_basic(self, value, context=None):
        extensions = ["markdown.extensions.extra", "codehilite"]
        marked_content = markdown(value, extensions=extensions)
        return mark_safe(marked_content)

    class Meta:
        icon = 'edit'

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

class PostStreamBlock(StreamBlock):
    markdown = MarkDownBlock()
    code = CodeBlock()
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    pullquote = PullQuoteBlock()
    document = DocumentChooserBlock(icon="doc-full-inverse")