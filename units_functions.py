def inches_to_cm (inches):
    return float (inches) * 2.54

def convert_inches (prompt_msg, msg, error_msg)
    try:
        inches = input (prompt_msg)
        cm = float(inches) * 2.54
        message = msg.format(inches, cm)
        print (message)
    except ValueError:
        print(error_msg)
