#!/bin/bash
export DJANGO_ENV=local

# Activate the virtual environment
source myvenv/bin/activate

# Run the Django development server
python manage.py runserver 0.0.0.0:8000