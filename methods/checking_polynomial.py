from methods import Polynomials


# The method implements the verification of the polynomial entered by the user.
# Input data: a polynomial (the data type is a polynomial), the degree (integer) required for this method.
# The output data is a tuple of two values, the first is a Boolean value
# (True - if the polynomial passed the test, False - if the polynomial failed the test);
# the second value is a polynomial with a positive outcome, with a negative error description
def checking(polynomial: Polynomials, power):
    print(polynomial)
    if len(polynomial) != power:
        return False, f'error length polynomial != {power}'
    if polynomial[power] != 1:
        return False, 'error the first coefficient must be equal to one'
    for i in polynomial:
        if i.__class__.__name__ == 'float':
            if not i.is_integer():
                return False, 'error all degrees must be integer'
        elif i.__class__.__name__ == 'complex':
            return False, 'error all degrees must be integer'
    return True, None
