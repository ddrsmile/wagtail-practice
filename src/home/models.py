from __future__ import absolute_import, unicode_literals
# django
from django.template.response import TemplateResponse
# wagtail
from wagtail.wagtailcore.models import Page
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route

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

HomePage.content_panels = Page.content_panels
