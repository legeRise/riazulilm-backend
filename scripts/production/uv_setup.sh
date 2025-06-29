#!/bin/bash
export DJANGO_ENV=production

# Check if virtual environment exists
if [ -d "myvenv" ]; then
  echo "Activating existing virtual environment..."
  source myvenv/bin/activate
else
  echo "Virtual environment not found. Creating a new one..."
  uv venv myvenv  # Create a new virtual environment
  source myvenv/bin/activate  # Activate it
  echo "Installing dependencies..."
  uv pip install -r requirements.txt  # Install dependencies in the new environment
  echo "Dependencies installed successfully."
  echo "Virtual environment setup complete."
fi

# Apply migrations
python manage.py migrate