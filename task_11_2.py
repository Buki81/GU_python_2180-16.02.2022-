class Exception:
    @staticmethod
    def dbz(num, num_2):
        try:
            print(num / num_2)
        except ZeroDivisionError:
            print('Ошибка! Деление на 0')


Exception.dbz(1, 0)
