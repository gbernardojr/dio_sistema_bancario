Saldo = 0.00
Depositos = []
Saques = []
QuantidadeSaques = 0


def depositar(ValorDeposito,/):
  global Saldo, Depositos
  Saldo += ValorDeposito
  Depositos.append(ValorDeposito)
  return "Deposito feito com sucesso."

def sacar(*,ValorSaque): 
  global Saldo, Saques, QuantidadeSaques
  if (valor > 500) :
    retorno = "Valor acima do limite permitido para saque."
  elif (QuantidadeSaques == 3) :
    retorno = "Limite de saques diários atingido."
  else :
    QuantidadeSaques += 1
    Saldo -= valor
    Saques.append(valor)
    retorno = "Saque feito com sucesso."
  return retorno

def extrato():
  global Depositos, Saques, Saldo
  print("*** Extrato ***")
  print("* Depositos *")
  for deposito in Depositos:
    print(f"{deposito:.2f}")
  print("* Saques *")
  for saque in Saques:
    print(f"{saque:.2f}")
  print(f"Saldo: {Saldo:.2f}")


while True:
  print( """ =========================================
                   MENU

      1 - Despositar
      2 - Sacar
      3 - Extrato
      0 - Sair

  ==========================================""")
  opcao = input("digite a opção desejada: ")

  if opcao == "0":
    break
  elif opcao == "1":
    valor = float(input("Valor para Depositar: "))
    print(depositar(valor))
  elif opcao == "2":
    valor = float(input("Valor para Sacar: "))
    print(sacar(ValorSaque=valor))
  elif opcao == "3":
    extrato()
