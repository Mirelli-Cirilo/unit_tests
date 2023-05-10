def converte_f_para_c(temp):
    """
    Essa função converte fahreinheit para celsius

    Testes:

    >>> converte_f_para_c(32)
    0.0

    >>> converte_f_para_c(-40)
    -40.0

    """
    return 5 * ((temp - 32) / 9)

def converte_c_para_f(temp):
    return temp * (9/5) + 32

if __name__ == '__main__':

    opcao = int(input('Digite 1 Para converter de celsius para fahrenheit\n'
                      'Digite 2 Para converter de fahrenheit para celsius'))
    
    temperatura = float(input('Forneça a temperatura:'))

    match(opcao):
        case 1:
            temperatura_convertida = converte_c_para_f(temperatura)
            print(f'A temperatura convertida é {temperatura_convertida}')
        case 2:
            temperatura_convertida = converte_f_para_c(temperatura)
            print(f'A temperatura convertida é {temperatura_convertida}')    
        case _:
            print('Digite uma opção válida!')
