from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# static path
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# using s3 as the storage for media files
# settings of aws authentication, bucket name and domain
AWS_ACCESS_KEY_ID = data["AWS"]["ID"]
AWS_SECRET_ACCESS_KEY = data["AWS"]["KEY"]

AWS_HEADERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = 'joeyliu-webapps'
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

# settings of project name and relatived static and media path
MEDIAFILES_LOCATION = 'joeyliu/media'

MEDIA_URL = "https://{0}/{1}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

# tell boto the place where static files and media files are
DEFAULT_FILE_STORAGE = 'project.settings.custom_path.MediaStorage'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://joeyliu.net'

try:
    from .local import *
except ImportError:
    pass
