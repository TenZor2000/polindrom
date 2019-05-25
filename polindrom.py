#создать программу, проверяющую является ли введенная фраза или слово полиндромом

my_word = input("Введите фразу: ")
dlina = len(my_word)

while dlina > 0:
    reverse = my_word[::-1]
    if reverse == my_word:
        print ('Ура! Это полиндром')
    else:
        print('Это НЕ полиндром')
    dlina =-1