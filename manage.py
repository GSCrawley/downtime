#!/usr/bin/env python
# encoding=utf-8

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        from django.core import management  # noqa: WPS433
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:  # noqa: WPS505
            import django  # noqa: WPS433, F401
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and"
                + "available on your PYTHONPATH environment variable? Did you"
                + "forget to activate a virtual environment?",
            )

        raise

    # This allows easy placement of apps within the interior downtime directory.
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, "downtime"))

    management.execute_from_command_line(sys.argv)
