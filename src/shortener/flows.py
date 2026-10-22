#основная логика сокращения ссылки (создание уникального кода)

SYSTEM = 62
CHARSET = "0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopgrstuvwxyz"

def encode(num: int):
    short_code = []

    while num != 0:
        short_code.append(CHARSET[num % SYSTEM])
        num = num // SYSTEM

    short_code.reverse()
    return "".join(short_code)

def decode(short_code: str):
    decoded_value = []

    number_of_items = len(short_code)

    for s in short_code:
        number_of_items -= 1
        decoded_value.append(CHARSET.index(s) * SYSTEM ** number_of_items)

    return sum(decoded_value)


