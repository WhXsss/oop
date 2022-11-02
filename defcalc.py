def main():
    print("Это простой калькулятор на Python")

    while True:
        try:
            print("Выберите действие которое хотите сделать:\n"
                "Сложить: +\n"
                "Вычесть: -\n"
                "Умножить: *\n"
                "Поделить: /\n"
                "Выйти: q\n")
            action = input("Действие: ")

            if action == "q":
                print("Выход из программы")
                break

            if action in ('+', '-', '*', '/'):
                x = int(input("x = "))
                y = int(input("y = "))
                if action == '+':
                     print('%.2f + %.2f = %.2f' % (x, y, x+y))
                elif action == '-':
                    print('%.2f - %.2f = %.2f' % (x, y, x-y))
                elif action == '*':
                    print('%.2f * %.2f = %.2f' % (x, y, x*y))
                elif action == '/':
                    if y != 0:
                        print('%.2f / %.2f = %.2f' % (x, y, x/y))
                    else:
                        print("Деление на ноль!")

        except ValueError:
            print('Вы вписали неправильное число, пожалуйста перезапустите и попробуйте еще раз')

if __name__ == '__main__':
        main()