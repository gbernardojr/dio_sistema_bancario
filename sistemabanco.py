Saldo = 0.00
Depositos = []
Saques = []
QuantidadeSaques = 0

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
    Saldo += valor
    Depositos.append(valor)
  elif opcao == "2":
    valor = float(input("Valor para Sacar: "))
    if (valor > 500) :
      print("Valor acima do limite permitido para saque.")
    elif (QuantidadeSaques == 3) :
      print("Limite de saques diários atingido.")
    else :
      QuantidadeSaques += 1
      Saldo -= valor
      Saques.append(valor)
  elif opcao == "3":
    print("*** Extrato ***")
    print("* Depositos *")
    for deposito in Depositos:
      print(f"{deposito:.2f}")
    print("* Saques *")
    for saque in Saques:
      print(f"{saque:.2f}")
    print(f"Saldo: {Saldo:.2f}")
