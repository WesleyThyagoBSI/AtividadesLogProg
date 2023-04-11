# Crie um algoritmo que gere uma lista aleatoria com 10 elementos
# e que selecione pares de numeros não duplicados que somados, deem 8

import random
import time

inicio = time.time()
def Somar(num1, num2):
  return num1+num2

listaNumeros = []
listaPares = []
for x in range(100):
  numeroAleatorio = random.randint(-100, 100)
  listaNumeros.append(numeroAleatorio)


for i in range(len(listaNumeros)):
  for j in range(len(listaNumeros)):
    if (Somar(listaNumeros[i], listaNumeros[j])==10 and ((listaNumeros[i], listaNumeros[j]) not in listaPares) and ((listaNumeros[j], listaNumeros[i]) not in listaPares)):
      listaPares.append((listaNumeros[i], listaNumeros[j]))

fim = time.time()
tempo_execucao = fim-inicio
print(listaNumeros)
print("-"*45)
for y in range(len(listaPares)):
  print(listaPares[y])

print("numeros de pares", len(listaPares))
print('tempo de execucação %.6f segundos' %tempo_execucao)

























      