import os
from init import create_app

app = create_app()

if __name__ == '__main__':
    # Set Flask environment to production
    os.environ['FLASK_ENV'] = 'production'
    # Run the Flask app
    app.run()
