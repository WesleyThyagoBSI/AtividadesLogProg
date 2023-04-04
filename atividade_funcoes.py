# funcao de soma
def Soma():
  n1 = int(input("Digite um numero: "))
  n2 = int(input("Digite outro numero: "))
  soma = n1 + n2
  print("A soma é ", soma)
# funcao de subtracao
def Subtracao():
  n1 = int(input("Digite um numero: "))
  n2 = int(input("Digite outro numero: "))
  subtracao = n1 - n2
  print("A subtracao é ", subtracao)
# funcao de multiplicacao
def Multiplicacao():
  n1 = int(input("Digite um numero: "))
  n2 = int(input("Digite outro numero: "))
  multiplicacao = n1 * n2
  print("A multiplicacao é ", multiplicacao)
# funcao de divisao
def Divisao():
  n1 = int(input("Digite um numero: "))
  n2 = int(input("Digite outro numero: "))
  divisao = n1 / n2
  print("A divisao é ", divisao)
  
# menu
print("="*40)
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("="*40)
#validacao de entrada
while True:
  escolha = int(input("Escolha uma das opções acima: "))
  #condicionais
  if (escolha == 1):
    Soma()
    break
  elif (escolha == 2):
    Subtracao()
    break
  elif (escolha == 3):
    Multiplicacao()
    break
  elif (escolha == 4):
    Divisao()
    break
