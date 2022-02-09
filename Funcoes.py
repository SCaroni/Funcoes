def Menu():
    print(f'{" CONVERSOR DE TEMPERATURA ":-^50}\n'
          '[ 1 ] Para converter de Celsius.\n'
          '[ 2 ] Para converter de Fahrenheit.\n'
          '[ 3 ] Para converter de Kelvin.\n'
          '[ 4 ] Para converter de Reaumur.\n'
          '[ 5 ] Para sair Programa.')
    print('-'*50)
    pergunta = int(input('╠════► Escolha uma opção: '))
    return pergunta


def ConversorT(unidade1, unidade2):
    """
    -→ Um converso básico de unidades de temperatura
    :param unidade1: (unidade inicial) a ser convertida
    :param unidade2: (unidade final) para qual se converte
    :return: temperatura na unidade desejada
    """
    if unidade1 == 1:
        if unidade2 == 2:
            c = float(input('Temperatura em Celsius: '))
            f = c * (9/5) + 32
            print(f'Temperatura em Fahrenheit: {f:.2f}°.')
        elif unidade2 == 3:
            c = float(input('Temperatura em Celsius: '))
            k = c + 273.15
            print(f'Temperatura em Kelvin: {k:.2f}°.')
        elif unidade2 == 4:
            c = float(input('Temperatura em Celsius: '))
            r = c * (4 / 5)
            print(f'Temperatura em Reaumur: {r:.2f}°.')
    elif unidade1 == 2:
        if unidade2 == 1:
            f = float(input('Temperatura em Fahrenheit: '))
            c = (f - 32) * (5 / 9)
            print(f'Temperatura em Celsius: {c:.2f}°.')
        elif unidade2 == 3:
            f = float(input('Temperatura em Fahrenheit: '))
            k = (f + 459.67) * (5 / 9)
            print(f'Temperatura em Kelvin: {k:.2f}°.')
        elif unidade2 == 4:
            f = float(input('Temperatura em Fahrenheit: '))
            r = (f - 32) * (4 / 9)
            print(f'Temperatura em Reaumur: {r:.2f}°.')
    elif unidade1 == 3:
        if unidade2 == 1:
            k = float(input('Temperatura em Kelvin: '))
            c = k - 273.15
            print(f'Temperatura em Celsius: {c:.2f}°.')
        elif unidade2 == 2:
            k = float(input('Temperatura em Kelvin: '))
            f = k * (9 / 5) - 459.67
            print(f'Temperatura em Fahrenheit: {f:.2f}°.')
        elif unidade2 == 4:
            k = float(input('Temperatura em Kelvin: '))
            r = (k - 273.15) * (4 / 5)
            print(f'Temperatura em Reaumur: {r:.2f}°.')
    elif unidade1 == 4:
        if unidade2 == 1:
            r = float(input('Temperatura em Reaumur: '))
            c = r * (5 / 4)
            print(f'Temperatura em Celsius: {c:.2f}°.')
        elif unidade2 == 2:
            r = float(input('Temperatura em Reaumur: '))
            f = r * (9 / 4) + 32
            print(f'Temperatura em Fahrenheit: {f:.2f}°.')
        elif unidade2 == 3:
            r = float(input('Temperatura em Reaumur: '))
            k = r * (5/4) + 273.15
            print(f'Temperatura em Kelvin: {k:.2f}°.')

