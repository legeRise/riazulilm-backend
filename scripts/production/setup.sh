#!/bin/bash
export DJANGO_ENV=production

# Check if virtual environment exists
if [ -d "myvenv" ]; then
  echo "Activating existing virtual environment..."
  source myvenv/bin/activate
else
  echo "Virtual environment not found. Creating a new one..."
  python3 -m venv myvenv  # Create a new virtual environment
  source myvenv/bin/activate  # Activate it
  echo "Installing dependencies..."
  pip install -r requirements.txt  # Install dependencies in the new environment
fi

# Apply migrations
python manage.py migrate