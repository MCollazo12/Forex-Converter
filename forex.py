from valid_codes import currency_codes

def is_valid_code(code):
    """
    Checks to see if the passed in 'code' argument is valid within
    a dictionary list of currency codes.
    
    Returns: 
        bool: True if the code is valid, else False
    """
    return code in currency_codes

def validate_input(from_currency, to_currency, amount):
    """
    Validate the input data for a currency conversion/
    
    Args:
        from_currency (str): The currency code to convert from
        to_currency (str): The currency code to convert to
        amount (str): The amount to be converted
        
    Returns:
        list: A list of error tuples containing the message category and message
    """
    
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