# ALAN KELVIN DE LIMA SANTOS
# WESLEY THYAGO DA SILVA SANTOS

import random

numero_aleatorio = random.randint(1, 100) # criando um numero aleatorio
print("Nível 1: três chances \nNível 2: cinco chances \nNível 3: oito chances")
print("*"*45)
chances = 0
while True: # validacao da entrada no nivel do jogo
  escolha_nivel = int(input("Escolha o nível do jogo [1, 2 ou 3]:"))
  print(escolha_nivel)
  if (escolha_nivel == 1 or escolha_nivel == 2 or escolha_nivel == 3):
    if (escolha_nivel == 1):
      chances = 3
    elif (escolha_nivel == 2):
      chances = 5
    elif (escolha_nivel == 3):
      chances = 8 
    break

acertou = 0
for loop in range(chances):
    chute = int(input(f"\n\nQual seu chute ({loop+1}/{chances})?: "))
    if (chute < numero_aleatorio):
      print("\nSeu chute foi menor que o número aleatório!")
    elif (chute > numero_aleatorio):
      print("\nSeu chute foi maior que o número aleatório!")
    elif (chute == numero_aleatorio):
      acertou += 1
      print("\nParabéns, você acertou o número secreto.")
      break
if (acertou == 0):
  print("\n\nInfelizmente, as suas chances acabaram!")


