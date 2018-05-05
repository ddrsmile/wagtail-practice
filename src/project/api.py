from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.endpoints import ImagesAPIEndpoint
from wagtail.documents.api.v2.endpoints import DocumentsAPIEndpoint

from post.api.endpoints import PostPagesAPIEndPoint

api_router = WagtailAPIRouter('wagtailapi')

# register common models
api_router.register_endpoint('pages', PagesAPIEndpoint)
api_router.register_endpoint('images', ImagesAPIEndpoint)
api_router.register_endpoint('documents', DocumentsAPIEndpoint)

# register app's api
api_router.register_endpoint('posts', PostPagesAPIEndPoint)
