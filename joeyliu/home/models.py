from __future__ import absolute_import, unicode_literals

from django.db import models
from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey

# wagtail models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks

class HomePage(RoutablePageMixin, Page):
    
    """
    carousel = StreamField([
        ('carousel',blocks.ListBlock(ImageCarouselBlock(), template="blocks/_carousel.html", icon='image')),
    ])
    """

    @route(r'^$')
    def home(self, request):
        return TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request)
        )
    
    @route(r'^portfolio/$')
    def portfolio(self, request):
        return TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request)
        )
    
    @route(r'^coding/$')
    def coding(self, request):
        return TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request)
        )
    
    @route(r'^resume/$')
    def resume(self, request):
        return TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request)
        )
    
    @route(r'^aboutme/$')
    def aboutme(self, request):
        return TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request)
        )

HomePage.content_panels = Page.content_panels