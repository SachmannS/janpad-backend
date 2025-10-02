import sys, os

# Add project path
project_home = '/home/username/backend'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'janpad.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
