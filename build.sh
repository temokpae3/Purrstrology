#!/bin/bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a Procfile (replace `app.py` with your main Python file)
echo "web: python run.py" > Procfile

# Initialize a Git repository (if not already initialized)
git init

# Add all files to Git
git add .

# Commit changes
git commit -m "Initial commit"

# Create a new Heroku app (replace `your-app-name` with your preferred app name)
heroku create your-app-name

# Push code to Heroku
git push heroku master

# Open the deployed app in the default web browser
heroku open
