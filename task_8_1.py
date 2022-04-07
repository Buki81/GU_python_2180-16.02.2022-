import re


def email_parse(email_address):
    pattern = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)')
    result = pattern.match(email_address)
    if not result:
        raise ValueError(f'Неверный адрес почты: {email_address}')
    all_result = pattern.finditer(email_address)
    for res in all_result:
        print(res.groupdict())

email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
