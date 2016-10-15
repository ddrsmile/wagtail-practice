from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# using s3 as the storage of static and media files
import csv
# settings of aws authentication, bucket name and domain
AWS_PEM = csv.reader(open('/usr/local/etc/aws_credentials.csv'), delimiter=',')
AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY = next(AWS_PEM)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

AWS_STORAGE_BUCKET_NAME = 'joeyliu-webapps'
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

# settings of project name and relatived static and media path
STATICFILES_LOCATION = 'joeyliu/static'
MEDIAFILES_LOCATION = 'joeyliu/media'

STATIC_URL = "https://{0}/{1}/".format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "https://{0}/{1}/".format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

# tell boto the place where static files and media files are
STATICFILES_STORAGE = 'project.settings.custom_path.StaticStorage'
DEFAULT_FILE_STORAGE = 'project.settings.custom_path.MediaStorage'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://joeyliu.me'

try:
    from .local import *
except ImportError:
    pass
