"""

Calculadora simples: Crie uma calculadora que permita ao usuário realizar operações básicas de adição, subtração, multiplicação e divisão.

"""
import os
# pedir para o usuário escolher qual opeção ele quer fazer if + elif - elif * elif /
# tratar o dado recebido pelo usuário
# input usuário número da direita, lembrando ele que a ordem de digitação do número pode afetar o resultado do calculo
# input usuario número da esquerda
# tratar o input dos números
# fazer a operação e exibir o resultado
# exibir um menu para que o usuário selecione qual operação fazer ou se ele deseja encerrar a calculadora 

print("""\t
       
      |-------------------------|
      |Bem-vindo! Boas contas :)|
      |-------------------------|

      \n""")

def realiza_conta(operador, numero_direito, numero_esquerdo):

      if operador == '+':
            return numero_direito + numero_esquerdo
      
      elif operador == '-':
            return numero_direito - numero_esquerdo
      
      elif operador == '*':
            return numero_direito * numero_esquerdo
      
      elif operador == '/':
            return numero_direito / numero_esquerdo


def recebe_operador():
      operadores_permitidos = ['-', '+', '*', '/']

      os.system('cls')

      while True:
            operador = input('Digite [+] para somar, [-] para subtrair, [*] para multiplicar, [/] para dividir: ')

            if len(operador) == 1 and operador in operadores_permitidos:
                  return operador
                  
            else:
                  os.system('cls')
                  print('Digite apenas o operador que deseja!')
                  continue
      

def recebe_numero_direito():

      while True:
            try:
                  numero = float(input('Digite o primeiro número: '))
                  return numero
            
            except ValueError:
                  print('🔢 Digite apenas numeros e lembre-se de utilizar o [.] para definir um número decimal. 🔢')
                  continue
      


def recebe_numero_esquerdo():

      while True:
            try:
                  numero = float(input('Digite o segundo número: '))
                  return numero
            
            except ValueError:
                  print('🔢 Digite apenas numeros e lembre-se de utilizar o [.] para definir um número decimal. 🔢')
                  continue


while True:
      iniciar_sair_calculadora = input('Digite [i] para iniciar: ')

      if iniciar_sair_calculadora.strip().lower() == 'i':

            os.system('cls')
            print('Carregando...🧠\n \n')
            print(round(realiza_conta(recebe_operador(), recebe_numero_direito(), recebe_numero_esquerdo()), 2))

      else:
            print('Digite apenas a letra dentro de []!')
            continue





