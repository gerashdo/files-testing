
def edad(num = -1):
    if isinstance(num, str):
        return 'Solo numeros'
    if num < 0:
        return 'No existes'
    if num < 14:
        return 'Eres niño'
    elif num < 18:
        return 'Eres adolescente'
    elif num < 66:
        return 'Eres adulto'
    elif num < 121:
        return 'Eres adulto mayor'
    else:
        return 'Eres Mumm-Ra'