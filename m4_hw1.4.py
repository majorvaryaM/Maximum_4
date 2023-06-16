# Определитель палиндромов

str_1 = input ('Введите фразу без пробелов с маленькой буквы: ')
def Palindrom_finder(str_1):
    str_2 = str_1[::-1]
    if str_1 == str_2:
        return True
    else: 
        return  False
    
print (Palindrom_finder(str_1))