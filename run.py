import os
from init import create_app

# Set the FLASK_ENV environment variable to "production"
os.environ['FLASK_ENV'] = 'production'

# Create the Flask app
app = create_app()

if __name__ == '__main__':
    # Run the Flask app
    app.run()
