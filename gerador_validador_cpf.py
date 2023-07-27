import random
import re


# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
# cpf_enviado_usuario = '74682489070'.replace('.', '').replace('-', '')         USANDO O method .replace
# cpf_enviado_usuario = re.sub(r'[^0-9]', '', '746.....824....,^´890-------70saidhasod') # USANDO expressões regulares


while True:

    #Gerador do CPF
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    # print(cpf_gerado_pelo_calculo)

    # Validador do primeiro dígito do CPF                                                    
    nove_digitos = cpf_gerado_pelo_calculo[:9]
    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)

    # Validador do segundo dígito do CPF 
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo_validador = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_gerado_pelo_calculo == cpf_gerado_pelo_calculo_validador:
        print(f'{cpf_gerado_pelo_calculo} é válido')
    else:
        print('CPF inválido')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break
    
