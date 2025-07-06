#!/bin/bash
export DJANGO_ENV=production

# Activate the virtual environment
source /home/habib/riazulilm-backend/myvenv/bin/activate

# Start the Gunicorn server with access logs to stdout
exec gunicorn \
    --workers 2 \
    --bind 0.0.0.0:6600 \
    --access-logfile - \
    riaz_ul_ilm_backend.wsgi:application