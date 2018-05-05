# django
from django.template.response import TemplateResponse
# wagtail
from wagtail.core.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route


class HomePage(RoutablePageMixin, Page):
    subpage_types = ['post.PostIndexPage']

    @route(r'^$')
    def home(self, request):
        return TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request)
        )

    @route(r'^aboutme/$')
    def aboutme(self, request):
        return TemplateResponse(
            request,
            'home/aboutme_page.html',
            self.get_context(request)
        )

    def get_sitemap_urls(self):
        return [
            {
                'location': self.full_url,
                'lastmod': self.latest_revision_created_at,
                'changefreq': 'monthly',
                'priority': 1
            },
            {
                'location': self.full_url + 'aboutme/',
                'lastmod': self.latest_revision_created_at,
                'changefreq': 'monthly',
                'priority': 0.8
            }
        ]


HomePage.content_panels = Page.content_panels
