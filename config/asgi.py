# encoding=utf-8

import os
import sys

from django.core.asgi import get_asgi_application

# This allows easy placement of apps within the interior downtime directory.
app_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir),
)
sys.path.append(os.path.join(app_path, "downtime"))
# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_asgi process. To fix this, use
# mod_asgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

# This application object is used by any ASGI server configured to use this
# file. This includes Django's development server, if the ASGI_APPLICATION
# setting points here.
application = get_asgi_application()
