import sys


class AlgoritmoSerial:

  def __init__(self, op, qtd):
    self.op = op
    self.qtd = qtd

  def opcaoSelecionada(self, op):
    opcoes = {
        1: self.calcSerial1,
        2: self.calcSerial2,
        3: sys.exit
    }
    opcoes[op]()

  op = 0

  # 1.Crie um algoritmo para imprimir a sequencia de fibonacci,
  # o usuario deverá inserir a quantidade de numeros a serem imprimidos.

  def calcSerial1(self):
    a = 0
    b = 1
    qtd = int(input("Digite" + " o limite a ser calculado\n"))

    def fib(a, b):
      fib = ""
      while a < qtd:
        a, b = b, a + b
        fib += str(a) + " "
      print("\nSerial 1:\n" + fib + "\n")

    fib(a, b)
    op = int(
        input("Selecione:\n" + "1.Imprimir outra sequencia\n" +
              "2.Voltar ao menu principal\n" + "3.Sair\n"))
    if op == 1:
      self.calcSerial1()
    if op == 2:
      self.menuPrincipal()
    if op == 3:
      print("Até Logo!")
      sys.exit()
    return self.menuPrincipal

  # 2. Crie um algoritmo para imprimir a sequencia de
  # numeros de acordo com a logica :
  # 1 6 4 4 7 2 10 0 ...
  # O programa devera solicitar ao
  # usuario a quantidade de numeros
  # a serem imprimidos pelo  algoritmo

  def calcSerial2(self):
    qtd = int(input("Digite" + " a quantidade a ser gerada\n"))
    x, y, z = -2, 8, ""
    for _ in range(qtd):
      x += 3
      y -= 2
      z += str(x) + " "
      z += str(y) + " "
    print("\nSerial 2:\n" + z + "\n")
    op = int(
        input("Selecione:\n" + "1.Imprimir outra sequencia\n" +
              "2.Voltar ao menu principal\n" + "3.Sair\n"))
    if op == 1:
      self.calcSerial2()
    if op == 2:
      self.menuPrincipal()
    if op == 3:
      print("Até Logo!")
      sys.exit()
    return self.menuPrincipal()

  # 3.Crie um menu que solicite ao       usuario selecionar uma opcao ou sair

  def menuPrincipal(self):
    op = 0
    while op < 1 or op > 3:
      op = int(
          input("Digite a opcao desejada:\n" + "1.Imprimir serial 1\n" +
                "2.Imprimir serial 2\n" + "3.Sair\n"))
      if op < 1 or op > 3:
        print("Opção inválida")
      else:
        self.opcaoSelecionada(op)

class Main:

  def __init__(self):
    self.a1 = AlgoritmoSerial(None, None)

  def Iniciar(self):
    self.a1.menuPrincipal()


main = Main()
main.Iniciar()
