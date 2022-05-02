class MyList:
    @staticmethod
    def nums():
        list_nums = []
        num = input('Введите число: ')
        while num != 'stop':
            if num.isdigit():
                list_nums.append(num)
                num = input('Введите число: ')
            else:
                num = input('Нужно ввести число!: ')
        print(list_nums)


MyList.nums()
