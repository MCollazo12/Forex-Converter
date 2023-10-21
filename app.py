from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from valid_codes import currency_codes
from forex import validate_input
import requests

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'secretkey'
toolbar = DebugToolbarExtension(app)


ACCESS_KEY = 'f06a721a0225939cd799aaea33618173'
API_URL = 'http://api.exchangerate.host/convert'

@app.route('/')
def smee():
    """
    Render the home page.
    
    Returns:
        rendered template: HTML content for the home page.
    """
    
    return render_template('index.html')
    
    
@app.route('/convert',methods=["POST"])
def convert():
    """
    Handles the currency conversion form submission. It takes the
    user's input, validates it, and displays either the correct
    conversion or an error message.
    
    Returns: 
        rendered template: HTML content for the page with flashed messages
    """
    
    from_currency = request.form.get('from_currency').upper()
    to_currency = request.form.get('to_currency').upper()
    amount = request.form.get('amount')
    
    errors = validate_input(from_currency, to_currency, amount)
    
    if errors:
        for category, message in errors:
            flash(message, category)
        
    if not errors:
        external_api_url = f"{API_URL}?access_key={ACCESS_KEY}&from={from_currency}&to={to_currency}&amount={amount}" 
        res = requests.get(external_api_url)
        data = res.json()
    
        if 'result' in data:
            converted_amt = data['result']
            currency_sign = currency_codes[to_currency]
            result_msg = f"The result is: {currency_sign}{converted_amt: .2f}"
        
            flash(result_msg, 'success')

    return render_template('index.html')
