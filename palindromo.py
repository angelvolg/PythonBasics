# -*- coding:utf-8 -*-

def palindrome(word):
    reversed_word = word[::-1]

    if reversed_word.lower()==word.lower():
        return True

    return False



if __name__=='__main__':
    word = str(input('Escribe una palabra: '))

    result=palindrome(word)

    if result is True:
        print('{} sí es un palíndromo.'.format(word))
    else:
        print('{} no es un palíndromo.'.format(word))
