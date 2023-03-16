# exercicio 1.
#declaracao de variaveis
NumerosImpares = []
# estrutura de repetição
while len(NumerosImpares)<10:
  ValorInteiro = int(input("Digite um número inteiro: "))
  if ((ValorInteiro%2)!=0):
    NumerosImpares.append(ValorInteiro)

print("*"*45)
print("Números Impares")
print(NumerosImpares)
print("*"*45)

# exercicio 2.
Nota = int(input("Digite uma nota de 0 a 10: "))

while (Nota<0) or (Nota>10):
  Nota = int(input("[Valor inválido!] Digite novamente uma nota de 0 a 10: "))

print("Valor Válido!")

# exercicio 3.
Usuario = input("Digite um usuário: ")
Senha = input("Digite uma senha: ")

while (Usuario == Senha) or Usuario=="" or Senha=="":
  print(
    "Cadastro Inválido. O usuário tem que ser diferente da senha. Tente novamente: "
  )
  Usuario = input(f"\n Digite um usuário: ")
  Senha = input("Digite uma senha: ")

print(f"Olá, {Usuario}! Seu cadastro foi realizado com sucesso.")
