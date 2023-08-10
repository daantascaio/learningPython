"""

Conversor de unidades: Desenvolva um programa que converta valores
entre diferentes unidades, como Celsius para Fahrenheit, metros para pés, quilogramas para libras, etc.

"""

# menu onde ele vai escolher qual programa vai ser executado
print("""

                    Bem vindo!
          
        Esee é o ConversorAll, tudo em um!

        Menu:
        [1] Celsius para Fahrenheit
        [2] Metros para Pés
        [3] Quilograma para libras
         """)

def celcius_fahrenheit():
    return

def metros_pes():
    return

def quilograma_libras():
    return

while True:
    
    user_choice = input('Escolha o número que identifica o programa: ')

    if len(user_choice) > 1:
       print('Inice 1 programa de cada vez!')
       continue

    elif user_choice == '1':
        celcius_fahrenheit()

    elif user_choice == '2':
        metros_pes()

    elif user_choice == '3':
        quilograma_libras()

    else:
        print('Escolha uma opção inserida no menu!')
        continue

    break
    