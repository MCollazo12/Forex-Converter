from valid_codes import currency_codes

def is_valid_code(code):
    return code in currency_codes

def validate_input(from_currency, to_currency, amount):
    errors = []
    
    if not is_valid_code(from_currency):
        errors.append(('error', f"Not a valid code: {from_currency}"))
    if not is_valid_code(to_currency):
        errors.append(('error', f"Not a valid code: {to_currency}"))
    try:
        amount = float(amount)
        if amount <= 0:
            errors.append(('error', "Not a valid amount."))
    except ValueError:
            errors.append(('error', "Invalid amount. Please enter a valid number."))
            
    return errors