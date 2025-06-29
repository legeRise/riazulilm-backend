#!/bin/bash
export DJANGO_ENV=production

# Activate the virtual environment
source myvenv/bin/activate

# Start the Gunicorn server
gunicorn --workers 2 --bind 0.0.0.0:6600 riaz_ul_ilm_backend.wsgi:application