# django
from django.db import models
from django.utils import timezone
#from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import select_template
# wagtail
#from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.search import index
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

# customization
from parts.blocks import PostStreamBlock
from parts.fields import RelatedLink
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase



class PostIndexPage(Page):

    subpage_types = ['post.PostPage']
    
    @property
    def posts(self):
        posts = PostPage.objects.live().descendant_of(self)
        posts = posts.order_by('-date', 'id')
        return posts

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

    api_fields = [
        APIField('title'),
        APIField('date'),
        APIField('search_description'),
        APIField('feed_image_thumbnail', serializer=ImageRenditionField('width-460', source='feed_image')),
        APIField('tags')
    ]

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