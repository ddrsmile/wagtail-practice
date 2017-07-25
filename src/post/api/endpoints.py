from wagtail.api.v2.endpoints import PagesAPIEndpoint

from post.api.pagination import PostPagePageNumberPagination
from post.models import PostPage

class PostPagesAPIEndPoint(PagesAPIEndpoint):
    pagination_class = PostPagePageNumberPagination
    name = 'posts'
    model = PostPage

    listing_default_fields = PagesAPIEndpoint.listing_default_fields + [field.name for field in PostPage.api_fields]

    def get_queryset(self):
        request = self.request

        # Specific the model to PostPage
        queryset = PostPage.objects.all()

        # Get live pages that are not in a private section
        queryset = queryset.public().live()

        # Filter by site
        queryset = queryset.descendant_of(request.site.root_page, inclusive=True)

        return queryset
