from __future__ import absolute_import, unicode_literals
# django
from django.db import models
from django.utils import timezone
#from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import select_template
# wagtail
#from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailsearch import index
# customization
from parts.blocks import PostStreamBlock
from parts.fields import RelatedLink
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase



class PostIndexPage(Page):

    subpage_types = ['post.PostPage']

    def get_context(self, request, *args, **kwargs):
        context = super(PostIndexPage, self).get_context(request)
        posts = self.posts

        tag = request.GET.get('tag')
        if tag:
            posts = posts.filter(tags__name=tag)
        
        page = request.GET.get('page')
        posts = self.get_paginated_posts(page, posts)
        page_range = self.designate_pages_range(posts, posts.paginator)
        context['posts'] = posts
        context['page_range'] = page_range

        return context

    def get_template(self, request, *args, **kwargs):
        default_template = super(PostIndexPage, self).get_template(request)
        return select_template(['post/{}.html'.format(self.slug), default_template])
    
    @property
    def posts(self):
        posts = PostPage.objects.live().descendant_of(self)
        posts = posts.order_by('-date', 'id')
        return posts
    
    def get_paginated_posts(self, page, posts):
        paginator = Paginator(posts, 6)
        try:
            posts =  paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return posts

    def designate_pages_range(self, page, paginator):
        start_index = max(1, page.number - 2)
        end_index = min(start_index + 4, paginator.num_pages)

        start_index = min(start_index, max(end_index - 4, 1))

        page_range = [i for i in range(start_index, end_index + 1)]
        return {'page_range': page_range}

    def get_sitemap_urls(self):
        return [
            {
                'location': self.full_url,
                'lastmod': self.latest_revision_created_at,
                'changefreq': 'weekly',
                'priority': 0.8
            }
        ]

PostIndexPage.content_panels = Page.content_panels

class PostPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('post.PostPage', related_name='related_links')


class PostPageTag(TaggedItemBase):
    content_object = ParentalKey('post.PostPage', related_name='tagged_items')

class PostPage(Page):
    
    parent_page_types = ['post.PostIndexPage']

    date = models.DateField('post date', default=timezone.now)
    body = StreamField(PostStreamBlock())
    tags = ClusterTaggableManager(through=PostPageTag, blank=True)
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
    def post_index(self):
        # Find closest ancestor which is a post index
        return self.get_ancestors().type(PostIndexPage).last()

    @property
    def prev_post(self):
        post = self.get_prev_sibling() or self.get_siblings().last()
        return None if post.id == self.id else post

    @property
    def next_post(self):
        post = self.get_next_sibling() or self.get_siblings().first()
        return None if post.id == self.id else post

    def get_sitemap_urls(self):
        return [
            {
                'location': self.full_url,
                'lastmod': self.latest_revision_created_at,
                'changefreq': 'monthly',
                'priority': 0.5
            }
        ]

PostPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    StreamFieldPanel('body'),
    InlinePanel('related_links', label="Related links"),
]

PostPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
    FieldPanel('tags'),
]