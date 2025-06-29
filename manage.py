#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
load_dotenv()


def main():
    """Run administrative tasks."""
    # Get the environment (defaults to 'local' if not set)
    ENVIRONMENT = os.getenv('DJANGO_ENV', 'local')

    # Set the correct settings module based on the environment
    if ENVIRONMENT == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'riaz_ul_ilm_backend.settings.production')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'riaz_ul_ilm_backend.settings.local')
        
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
