def real_to_euro(reais):
    return float(inches) * 0.29

def convert_reais(prompt_msg, msg, error_msg):
    try:
        reais = input(prompt_msg)
        euros = float(reais) / 0.29
        message = msg.format(reais,real_to_euro)
        print(message)
    except ValueError:
        print(error_msg)
