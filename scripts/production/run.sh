#!/bin/bash
export DJANGO_ENV=production

# Activate the virtual environment
source myvenv/bin/activate

# Start the Gunicorn server
gunicorn --workers 3 --bind 0.0.0.0:9200 ezclip.wsgi:application