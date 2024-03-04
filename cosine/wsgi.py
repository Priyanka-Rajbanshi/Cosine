import os

from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'cosine' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cosine.settings')

# Create a WSGI application.
application = get_wsgi_application()
