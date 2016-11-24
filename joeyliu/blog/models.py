from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils import timezone
from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey

# wagtail models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks

from blocks.blocks import ImageCarouselBlockList, CodeBlock

class BlogPage(Page):
    
    parent_page_types = ['blog.BlogIndexPage']

    date = models.DateField('post date', default=timezone.now)
    body = StreamField([
        ('carousel', ImageCarouselBlockList()),
        ('code', CodeBlock()),
        ])

BlogPage.content_panels = Page.content_panels + [
    StreamFieldPanel('body')
]

class BlogIndexPage(Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogPage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        blogs = self.blogs
        page = request.GET.get('page')
        blogs = self.get_paginated_blogs(page, blogs)
        context['blogs'] = blogs
        return context
    
    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date', 'id')
        return blogs
    
    def get_paginated_blogs(self, page, blogs):
        paginator = Paginator(blogs, 6)
        try:
            products =  paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        return products

BlogIndexPage.content_panels = Page.content_panels