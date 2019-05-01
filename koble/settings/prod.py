from koble.settings.settings import *

DEBUG = False

# HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
#
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
#
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_S3_REGION_NAME = 'eu-north-1'
# AWS_S3_HOST = 's3.eu-north-1.amazonaws.com'
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_S3_ADDRESSING_STYLE = 'path'
# S3_USE_SIGV4 = True