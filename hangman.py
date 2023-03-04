import random
from os import name, system


def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def selecionapalvra():
    frutas = ['uva', 'banana', 'morango', 'abacate', 'laranja', 'abacaxi', 'amora', 'acerola',
               'cereja', 'goiaba', 'jabuticaba', 'jaca', 'kiwi',
               'melancia', 'pera', 'pitaya', 'tangerina', 'caju', 'graviola',
               'ameixa', 'cacau', 'coco', 'groselha', 'jenipapo', 'lima',
               'pitanga', 'seriguela']
    item = random.choice(frutas)
    return item

def find_index(lista, letra):
    return [index for index, value in enumerate(lista) if value == letra]

estagios = [
"""
-------------
|           |
|
|
|
|
|
|
-
"""
,

"""
-------------
|           |
|           O
|
|
|
|
|
-
"""
,
"""
-------------
|           |
|           O
|           |
|           |
|
|
|
-
"""
,
"""
-------------
|           |
|           O
|          \\|/
|           |
|
|
|
-
"""
,
"""
-------------
|           |
|           O
|          \\|/
|           |
|          /
|
|
-
"""
,
"""
-------------
|           |
|           O
|          \\|/
|           |
|          / \\
|
|
-
"""

]
limpa_tela()
palavra = selecionapalvra()
letra_errada = []
letra_certa = ["_" for x in palavra]
chances = 0
print("Bem vindo ao jogo da forca!")
print("Adivinhe a palavra abaixo:")
while chances < 5:
    print("Palavra: "," ".join(letra_certa))
    print("Letras erradas:", " ".join(letra_errada))
    letra = input("Digite uma letra: ").lower()
    if(letra in palavra):
        for i in (find_index(palavra, letra)):
            letra_certa[i] = letra
    else:
        letra_errada.append(letra)
        chances += 1
    #print(f"Chances restantes: {6 - chances}")
    print(estagios[chances])
    print("\n-------------------------------------------------\n")
    if(list(palavra) == letra_certa):
        print("Parabéns! Você ganhou! A palavra era:", palavra)
        break
if(chances >= 5):
    print("Você perdeu! Suas tentativas acabaram! A palavra era:", palavra, "  :( ")

