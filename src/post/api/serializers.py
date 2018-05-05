from django.urls import NoReverseMatch
from rest_framework.fields import Field
from wagtail.api.v2.serializers import PageSerializer


class PostPageHtmlUrlField(Field):
    """
    Serializes the "html_url" field for pages.

    Example:
    "html_url": "/blog/blog-post/"
    """
    def get_attribute(self, instance):
        return instance

    def to_representation(self, page):
        try:
            return page.url
        except NoReverseMatch:
            return None


class PostPageSerializer(PageSerializer):
    html_url = PostPageHtmlUrlField(read_only=True)
