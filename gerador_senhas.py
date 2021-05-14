from random import choice, randint
from string import ascii_lowercase as a_low, ascii_uppercase as a_up


def random_num():
    num = str(randint(0, 9))
    return num


def random_letter(case):
    lw = list(a_low)
    up = list(a_up)

    str(case).lower()

    if case == "lower":
        alpha = choice(lw)
        return alpha

    if case == "upper":
        alpha = choice(up)
        return alpha


def password_generator():
    password_length = 1
    opt = 0

    print("\033[1;31mCRIADOR DE SENHAS ALEATÓRIAS\033[0;0m")
    print("Para sair digite 253")
    print("A senha terá entre 4 e 25 digitos")

    while password_length != 253:

        if password_length == 253 or opt == 253:
            break

        try:
            password_length = int(input("Qual o tamanho da senha? "))

            print("1 - Somente números")
            print("2 - Letras minúsculas")
            print("3 - Letras maiúsculas")
            print("4 - Maiúsculas e minúsculas")
            opt = int(input("Qual o tamanho da senha? "))

        except (ValueError, NameError, TypeError):
            print("Insira somente números inteiros")

        else:
            if password_length < 4:
                password_length = 4
            elif password_length > 25:
                password_length = 25

            password = ""

            if opt == 1:
                while len(password) <= password_length:
                    num = random_num()
                    password += num

            if opt == 2:
                while len(password) <= password_length:
                    num = random_num()
                    alpha = random_letter("lower")
                    password += num
                    password += alpha

            if opt == 3:
                while len(password) <= password_length:
                    num = random_num()
                    alpha = random_letter("upper")
                    password += alpha
                    password += num

            if opt == 4:
                while len(password) <= password_length:
                    num = random_num()
                    alpha = random_letter("upper")
                    alpha1 = random_letter("lower")
                    password += alpha
                    password += num
                    password += alpha1

            if opt > 4 or opt < 0:
                opt = 4

            print(30 * "=")
            print(f"A sua senha é \033[0;32m{password}\033[0;0m")
            print(30 * "=")

        finally:
            password = ""


password_generator()
