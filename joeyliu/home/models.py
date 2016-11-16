from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

# customized widget models
from widgets.models import CarouselItem

# wagtail models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel)

class HomePage(Page):
    pass

class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('HomePage', related_name='carousel_items')

HomePage.content_panels = Page.content_panels + [
        InlinePanel('carousel_items', label="Carousel items"),
]
