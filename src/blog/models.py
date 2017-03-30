from __future__ import absolute_import, unicode_literals
# django
from django.db import models
from django.utils import timezone
from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# wagtail
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailsearch import index
# customization
from parts.blocks import BlogStreamBlock
from parts.fields import RelatedLink, CarouselItem
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase



class BlogIndexPage(Page):

    subpage_types = ['blog.BlogPage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        blogs = self.blogs

        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)
        
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
            blogs =  paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        return blogs

BlogIndexPage.content_panels = Page.content_panels

class BlogPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('blog.BlogPage', related_name='carousel_items')


class BlogPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('blog.BlogPage', related_name='related_links')


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('blog.BlogPage', related_name='tagged_items')

class BlogPage(Page):
    
    parent_page_types = ['blog.BlogIndexPage']

    date = models.DateField('post date', default=timezone.now)
    body = StreamField(BlogStreamBlock())
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    @property
    def blog_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last()

BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    StreamFieldPanel('body'),
    InlinePanel('carousel_items', label="Carousel items"),
    InlinePanel('related_links', label="Related links"),
]

BlogPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
    FieldPanel('tags'),
]