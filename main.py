#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


class ConvertMorse(object):
    # diccionario del alfabeto normal
    normalAlphabet = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }

    # diccionario caracteres  morse
    morseAlphabet = dict((v, k) for (k, v) in normalAlphabet.items())

    def __init__(self):
        self.initial()

    def initial(self):
        opt = 0
        while int(opt) != 3:
            print('Seleccione la opcion deseada:')
            print('1) traducir codigo morse :')
            print('2) traducir texto a  codigo morse :')
            print('3) Cerrar :')

            opt = input("Opcion:  ")

            try:

                if int(opt) == 1:

                    morse_code = input("Ingrese codigo morse a traducir:  ")
                    print('-' * 20)
                    alpha = self.morse_to_alphabet(morse_code)

                    print("ASCII:  " + alpha)
                    print('-' * 20)
                elif int(opt) == 2:

                    text = input('Ingrese el texto a convertir : ')
                    print('-' * 20)
                    morse = self.alpha_to_morse(text)
                    print('Codigo morse: ' + morse)
                    print('-' * 20)

                elif int(opt) == 3:
                    print('Terminando Ejecucion')
                    sys.exit(0)
            except ValueError:
                opt = 0
                print('Solo se aceptan numeoros')


    def morse_to_alphabet(self,morse_code):
        words = morse_code.split('   ')
        decode_message= ""
        for word in words:
            decode_message +=" " + self.decode_word(word)
        return decode_message

    def alpha_to_morse(self, text=''):
        """
        metodo para convertir texto ascii a código morse
        :param text:
        :return:
        """
        words= text.upper().split(' ')
        encode_message = ""
        for word in words:
            encode_message += "   "+ self.encode_word(word)
        return encode_message

    def encode_word(self,word):
        """
        Metodo para convertir de una palabra del alfabeto a código morse
        :param word:
        :return:
        """
        word_morse =""
        for char in word:
            if char in self.normalAlphabet:
                word_morse += " " + self.normalAlphabet[char]
            else:
                word_morse+= " "+"</NE>"
        return word_morse

    def decode_word(self,word):
        """
        Método para convertir de código morse-alfabeto normal
        :param word:
        :return:
        """
        normal_word = ""
        for char in word.split(' '):
            if char in self.morseAlphabet:
                normal_word += self.morseAlphabet[char]
        return normal_word


test = ConvertMorse()



