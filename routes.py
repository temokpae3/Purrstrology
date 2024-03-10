from flask import Blueprint, flash, redirect, render_template, request, url_for, send_file
from datetime import datetime

main = Blueprint('main', __name__)

# Dictionary mapping zodiac signs to kitty names
zodiac_kitty_mapping = {
    'aries': 'The Aries Kitty',
    'taurus': 'The Taurus Kitty',
    'gemini': 'The Gemini Kitty',
    'cancer': 'The Cancer Kitty',
    'leo': 'The Leo Kitty',
    'virgo': 'The Virgo Kitty',
    'libra': 'The Libra Kitty',
    'scorpio': 'The Scorpio Kitty',
    'sagittarius': 'The Sagittarius Kitty',
    'capricorn': 'The Capricorn Kitty',
    'aquarius': 'The Aquarius Kitty',
    'pisces': 'The Pisces Kitty'
}

# Function to determine the zodiac sign based on the birthdate
def get_zodiac_sign(birthdate):
    month_day = birthdate.strftime('%m-%d')
    if '03-21' <= month_day <= '04-19':
        return 'aries'
    elif '04-20' <= month_day <= '05-20':
        return 'taurus'
    elif '05-21' <= month_day <= '06-20':
        return 'gemini'
    elif '06-21' <= month_day <= '07-22':
        return 'cancer'
    elif '07-23' <= month_day <= '08-22':
        return 'leo'
    elif '08-23' <= month_day <= '09-22':
        return 'virgo'
    elif '09-23' <= month_day <= '10-22':
        return 'libra'
    elif '10-23' <= month_day <= '11-21':
        return 'scorpio'
    elif '11-22' <= month_day <= '12-21':
        return 'sagittarius'
    elif '12-22' <= month_day <= '01-20':
        return 'capricorn'
    elif '01-21' <= month_day <= '02-19':
        return 'aquarius'
    elif '02-20' <= month_day <= '03-20':
        return 'pisces'
    # Add conditions for other zodiac signs
    else:
        return 'Unknown'
    
# Function to display image based on zodiac sign
def determine_image_filename(birthdate):
    # Convert birthdate string to a datetime object
    month_day = birthdate.strftime('%m-%d')
    
    # Logic to determine the image filename based on the birthdate

    if '03-21' <= month_day <= '04-19':
        return 'static/img/cat1.jpg'
    elif '04-20' <= month_day <= '05-20':
        return 'static/img/cat2.jpg'
    elif '05-21' <= month_day <= '06-20':
        return 'static/img/cat3.jpg'
    elif '06-21' <= month_day <= '07-22':
        return 'static/img/cat4.jpg'
    elif '07-23' <= month_day <= '08-22':
        return 'static/img/cat5.jpg'
    elif '08-23' <= month_day <= '09-22':
        return 'static/img/cat6.jpg'
    elif '09-23' <= month_day <= '10-22':
        return 'static/img/cat7.jpg'
    elif '10-23' <= month_day <= '11-21':
        return 'static/img/cat8.jpg'
    elif '11-22' <= month_day <= '12-21':
        return 'static/img/cat9.jpg'
    elif '12-22' <= month_day <= '01-20':
        return 'static/img/cat10.jpg'
    elif '01-21' <= month_day <= '02-19':
        return 'static/img/cat11.jpg'
    elif '02-20' <= month_day <= '03-20':
        return 'static/img/cat12.jpg'

    # If the birthdate doesn't match any specific condition, return a default image
    return 'img/default_cat.jpg'  # Assuming you have a default image to show

def determine_image_url(birthdate):
    # Convert birthdate string to a datetime object
    month_day = birthdate.strftime('%m-%d')
    
    # Logic to determine the image filename based on the birthdate

    if '03-21' <= month_day <= '04-19':
        return 'https://www.instagram.com/p/CY_4tnVLtj0/?epik=dj0yJnU9bFI2VzZFM1BiVlhSYW03WDFhSVJCZkFZbUVzN1VoYUgmcD0wJm49NGt6SDBqODBOYTlpWU9wOWRnWlAzQSZ0PUFBQUFBR1h0U3g4&img_index=3'
    elif '04-20' <= month_day <= '05-20':
        return 'https://www.instagram.com/p/CY_4tnVLtj0/?epik=dj0yJnU9bFI2VzZFM1BiVlhSYW03WDFhSVJCZkFZbUVzN1VoYUgmcD0wJm49NGt6SDBqODBOYTlpWU9wOWRnWlAzQSZ0PUFBQUFBR1h0U3g4&img_index=4'
    elif '05-21' <= month_day <= '06-20':
        return 'https://www.instagram.com/p/CY_4tnVLtj0/?epik=dj0yJnU9bFI2VzZFM1BiVlhSYW03WDFhSVJCZkFZbUVzN1VoYUgmcD0wJm49NGt6SDBqODBOYTlpWU9wOWRnWlAzQSZ0PUFBQUFBR1h0U3g4&img_index=5'
    elif '06-21' <= month_day <= '07-22':
        return 'https://www.instagram.com/p/CY_4tnVLtj0/?epik=dj0yJnU9bFI2VzZFM1BiVlhSYW03WDFhSVJCZkFZbUVzN1VoYUgmcD0wJm49NGt6SDBqODBOYTlpWU9wOWRnWlAzQSZ0PUFBQUFBR1h0U3g4&img_index=6'
    elif '07-23' <= month_day <= '08-22':
        return 'https://www.instagram.com/p/CZAXWXhp4bZ/?epik=dj0yJnU9UTQycG5rOUl1NFNVSk5ycTVqNS1pRmlFb3R6bUYtdGomcD0wJm49WkVVS0NjUFBfMXFTSkx0Vzh1eXlaZyZ0PUFBQUFBR1h0U2Zn&img_index=1'
    elif '08-23' <= month_day <= '09-22':
        return 'https://www.instagram.com/p/CZAXWXhp4bZ/?epik=dj0yJnU9UTQycG5rOUl1NFNVSk5ycTVqNS1pRmlFb3R6bUYtdGomcD0wJm49WkVVS0NjUFBfMXFTSkx0Vzh1eXlaZyZ0PUFBQUFBR1h0U2Zn&img_index=2'
    elif '09-23' <= month_day <= '10-22':
        return 'https://www.instagram.com/p/CZAXWXhp4bZ/?epik=dj0yJnU9UTQycG5rOUl1NFNVSk5ycTVqNS1pRmlFb3R6bUYtdGomcD0wJm49WkVVS0NjUFBfMXFTSkx0Vzh1eXlaZyZ0PUFBQUFBR1h0U2Zn&img_index=3'
    elif '10-23' <= month_day <= '11-21':
        return 'https://www.instagram.com/p/CZAXWXhp4bZ/?epik=dj0yJnU9UTQycG5rOUl1NFNVSk5ycTVqNS1pRmlFb3R6bUYtdGomcD0wJm49WkVVS0NjUFBfMXFTSkx0Vzh1eXlaZyZ0PUFBQUFBR1h0U2Zn&img_index=4'
    elif '11-22' <= month_day <= '12-21':
        return 'https://www.instagram.com/p/CZAXWXhp4bZ/?epik=dj0yJnU9UTQycG5rOUl1NFNVSk5ycTVqNS1pRmlFb3R6bUYtdGomcD0wJm49WkVVS0NjUFBfMXFTSkx0Vzh1eXlaZyZ0PUFBQUFBR1h0U2Zn&img_index=5'
    elif '12-22' <= month_day <= '01-20':
        return 'https://www.instagram.com/p/CZAXWXhp4bZ/?epik=dj0yJnU9UTQycG5rOUl1NFNVSk5ycTVqNS1pRmlFb3R6bUYtdGomcD0wJm49WkVVS0NjUFBfMXFTSkx0Vzh1eXlaZyZ0PUFBQUFBR1h0U2Zn&img_index=6'
    elif '01-21' <= month_day <= '02-19':
        return 'https://www.instagram.com/p/CY_4tnVLtj0/?epik=dj0yJnU9bFI2VzZFM1BiVlhSYW03WDFhSVJCZkFZbUVzN1VoYUgmcD0wJm49NGt6SDBqODBOYTlpWU9wOWRnWlAzQSZ0PUFBQUFBR1h0U3g4&img_index=1'
    elif '02-20' <= month_day <= '03-20':
        return 'https://www.instagram.com/p/CY_4tnVLtj0/?epik=dj0yJnU9bFI2VzZFM1BiVlhSYW03WDFhSVJCZkFZbUVzN1VoYUgmcD0wJm49NGt6SDBqODBOYTlpWU9wOWRnWlAzQSZ0PUFBQUFBR1h0U3g4&img_index=2'

    # If the birthdate doesn't match any specific condition, return a default image
    return '#'  # Assuming you have a default image to show

@main.route('/')
def index():
    return render_template('index.html', active_page='index')

@main.route('/details')
def details():
    return render_template('details.html')

@main.route('/cat_profiles')
def cat_profiles():
    return render_template('cat_profiles.html', active_page='cat_profiles')

@main.route('/adoption_success', methods=['POST'])
def adoption_success():
    # Get form data
    name = request.form.get('name')
    birthdate = request.form.get('birthdate')

    # Validate form data
    if not name or not birthdate:
        # If any field is missing, redirect back to the details page with a warning message
        flash('Please fill out all fields to adopt a zodiac kitty', 'warning')
        return redirect(url_for('main.details'))

    try:
        # Attempt to parse birthdate string into a datetime object
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    except ValueError:
        # If the birthdate string is not in the correct format, redirect back to the details page with a warning message
        flash('Please enter a valid birthdate in the format YYYY-MM-DD', 'warning')
        return redirect(url_for('main.details'))

    # Determine the zodiac sign based on the birthdate
    astro_sign = get_zodiac_sign(birthdate)

    # Logic to determine the image filename based on the birthdate
    image_path = determine_image_filename(birthdate)

    # Get the kitty name based on the zodiac sign
    kitty_name = zodiac_kitty_mapping.get(astro_sign)

    url_path = determine_image_url(birthdate)

    # Render the adoption_success template with data
    return render_template('adoption_success.html', name=name, kitty_name=kitty_name, image_path=image_path, url_path=url_path)

@main.route('/download_image')
def download_image():
    # Extract the image path from the query parameter
    image_path = request.args.get('image_path')

    # Check if image_path is provided
    if not image_path:
        return "Image path is missing in the request."

    # Send the file for download
    return send_file(image_path, as_attachment=True)