'''
# Challenge:
# Challenge:
ATM machines allow 4 or 6 digit PIN codes and
PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

Create a function to validate whether an input string is a valid pin.

# Examples:
validate_pin("1234")   -->  True
validate_pin("12345")  -->  False
validate_pin("a234")   -->  False
'''

def valid_pin(pin):
    valid_nums = ["1","2","3","4","5","6","7","8","9","0"]
    pin.split()
    if len(pin) == 4 or len(pin) == 6:
        for char in pin:
            if char in valid_nums:
                continue
            else:
                print("false")
                return False
        else:
            print("true")
            return True
    else:
        print("false")
        return False







valid_pin("b23456")