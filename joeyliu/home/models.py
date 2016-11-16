from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

# wagtail models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel)

class HomePage(Page):
    pass


HomePage.content_panels = Page.content_panels
