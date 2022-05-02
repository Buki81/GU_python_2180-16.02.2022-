class Date:
    @staticmethod
    def date_base(instant):
        d = instant.split('-')
        return f"День: {int(d[0])} \n" \
               f"Месяц: {int(d[1])} \n" \
               f"Год: {int(d[2])}"

    @classmethod
    def date_str(cls, instant):
        d = instant.split('-')
        if len(d[2]) == 4 and 1 <= int(d[1]) <= 12 and 1 <= int(d[0]) <= 31:
            return f"------------------------ \n" \
                   f"День: {int(d[0])} \n" \
                   f"Месяц: {int(d[1])} \n" \
                   f"Год: {int(d[2])}"
        else:
            return ('Неверно установлена дата.')


print(Date.date_base("30-01-2020"))
print(Date.date_str("25-08-2022"))
