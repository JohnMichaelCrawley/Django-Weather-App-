import os
from import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'wsgi' application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_app.settings')

# Create a WSGI application object from the Django project's settings
application = get_wsgi_application()