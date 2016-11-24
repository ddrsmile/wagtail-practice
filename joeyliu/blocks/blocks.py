from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

class ImageCarouselBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta():
        icon = 'image'

class ImageCarouselBlockList(blocks.StructBlock):
    carousel_title = blocks.CharBlock()
    button = blocks.BooleanBlock(required=False)
    arrow = blocks.BooleanBlock(required=False)
    images = blocks.ListBlock(ImageCarouselBlock(), icon='image')

    class Meta():
        template="blocks/_carousel.html"
        icon='image'

LANGUAGES = ( 
    ('cpp', 'C++'),
    ('python','Python'),
    ('java', 'Java'),
)

class CodeBlock(blocks.StructBlock):
    language = blocks.ChoiceBlock(choices=LANGUAGES, blank=False, null=False, default='python')
    code = blocks.TextBlock()

    class Meta:
        template="blocks/_code.html"
        icon="code"