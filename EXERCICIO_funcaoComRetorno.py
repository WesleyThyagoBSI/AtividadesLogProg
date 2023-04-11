# Crie um algoritmo que gere uma lista aleatoria com 10 elementos
# e que selecione pares de numeros não duplicados que somados, deem 8

# import random
# import time

# inicio = time.time()
# def Somar(num1, num2):
#   return num1+num2

# listaNumeros = []
# listaPares = []
# for x in range(100):
#   numeroAleatorio = random.randint(-100, 100)
#   listaNumeros.append(numeroAleatorio)


# for i in range(len(listaNumeros)):
#   for j in range(len(listaNumeros)):
#     if (Somar(listaNumeros[i], listaNumeros[j])==10 and ((listaNumeros[i], listaNumeros[j]) not in listaPares) and ((listaNumeros[j], listaNumeros[i]) not in listaPares)):
#       listaPares.append((listaNumeros[i], listaNumeros[j]))

# fim = time.time()
# tempo_execucao = fim-inicio
# print(listaNumeros)
# print("-"*45)
# print(listaPares)
# print("-"*45)
# print('tempo de execucação %.6f segundos' %tempo_execucao)



import random

def ParouImpar(numero):
  if ((numero%2)==0):
    return "par."
  else:
    return "impar"

listaNumeros = []
for i in range(10):
  aleatorio = random.randint(1,100)
  listaNumeros.append(aleatorio)  

print("Array gerado: ")
print(listaNumeros)
print("="*45)
for j in range(len(listaNumeros)):
  print(f"O {listaNumeros[j]} é {ParouImpar(listaNumeros[j])}")


























      