def linha(tam=50):
    print('-' * tam)


def Menu():
    print(f'{" CONVERSOR DE TEMPERATURA ":-^50}\n'
          'Escolha a 1ª unidade depois a 2ª unidade:')
    linha(50)
    print('[ 1 ] Celsius [ 2 ] Fahrenheit\n'
          '[ 3 ] Kelvin  [ 4 ] Reaumur')
    linha(50)
    ConversorT(int(input('╠════► Unidade1: ')), int(input('╠════► Unidade2: ')))
    Continuar()


def Texto(txt, tam=0):
    t1 = tam - (len(txt) + 5)
    t2 = "." * t1
    print(t2)


def ConversorT(unidade1, unidade2):
    if unidade1 == 1:
        if unidade2 == 2:
            c = float(input('Temperatura em Celsius: '))
            f = c * (9 / 5) + 32
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
            k = r * (5 / 4) + 273.15
            print(f'Temperatura em Kelvin: {k:.2f}°.')


def Continuar():
    from time import sleep
    linha(50)
    pergunta = str(input('Deseja continuar? [SIM ou NÃO]: ')).upper()[0]
    while True:
        if pergunta in 'S':
            Menu()
        elif pergunta not in 'SN':
            print('\033[31mRESPOSTA INVÁLIDA\033[m')
            pergunta = str(input('Deseja continuar? [SIM ou NÃO]: ')).upper()[0]
        elif pergunta in 'N':
            print('Saindo do Programa...'.center(50))
            sleep(2)
        break


