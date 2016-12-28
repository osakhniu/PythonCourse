
'''
Creator - Oksana Sakhniuk, 12/16/2016
The source code is a simple text generator that asks the user to input 3 letters: 'v' for vowel, 'c' for consonant
and any other letter. Based on the user's input, the program generates 20 different combinatios of these letters

'''

import random, string

vowels='aeiouy'
consonants='bcdfgjklmnpqrsvwxz'
letters=string.ascii_lowercase

letter_input_1=raw_input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter ")
letter_input_2=raw_input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter ")
letter_input_3=raw_input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter ")

def generator():
    if letter_input_1=='v':
        letter1=random.choice(vowels)
    elif letter_input_1=='c':
        letter1=random.choice(consonants)
    elif letter_input_1=='l':
        letter1=random.choice(letters)
    else:
        letter1=letter_input_1
    if letter_input_2=='v':
        letter2=random.choice(vowels)
    elif letter_input_2=='c':
        letter2=random.choice(consonants)
    elif letter_input_2=='l':
        letter1=random.choice(letters)
    else:
        letter2=letter_input_2
    if letter_input_3=='v':
        letter3=random.choice(vowels)
    elif letter_input_3=='c':
        letter3=random.choice(consonants)
    elif letter_input_3=='l':
        letter3=random.choice(letters)
    else:
        letter3=letter_input_3

    name=letter1+letter2+letter3
    return name

for i in range(20):
    print(generator())
