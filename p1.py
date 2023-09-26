import string

pas = input('Введите пароль: ')

tU = any([1 if i in string.ascii_uppercase else 0 for i in pas])
tL = any([1 if i in string.ascii_lowercase else 0 for i in pas])
tD = any([1 if i in string.digits else 0 for i in pas])
tSS = any([1 if i in string.punctuation else 0 for i in pas])

length = len(pas)

if length >= 8 and tU == True and tL == True and tD == True and tSS == True:
    print('Действительный пароль')
else:
    print('Пароль не соответствует требованиям')
    