try:
    z = phonenumbers.parse("120012301", None)
except phonenumbers.phonenumberutil.NumberParseException: (0) Missing or invalid default region.:
    print(+)
except phonenumbers.phonenumberutil.NumberParseException: (1) The string supplied did not seem to be a phone number.:
    print(-)


formatter = phonenumbers.AsYouTypeFormatter("RU")
b = "120012301"
try:
    z = phonenumbers.parse(b, None)
    formatter.input_digit(z)
except NumberParseException as e:
    if e.error_type == NumberParseException.INVALID_COUNTRY_CODE:
        z = int(b[1:])
        formatter.input_digit(z)
    elif e.error_type == NumberParseException.NOT_A_NUMBER:
        print("-")         