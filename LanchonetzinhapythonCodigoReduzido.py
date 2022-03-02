from time import sleep

produtos = {'nome100': 'Cachorro Quente', 'nome101': 'Bauru Simples', 'nome102': 'Bauru com Ovo',
            'nome103': 'Hamburguer', 'nome104': 'Cheeseburguer', 'nome105': 'Suco', 'nome106': 'Refrigerante'}
precos = {'preço100': 1.20, 'preço101': 1.30, 'preço102': 1.50, 'preço103': 1.20, 'preço104': 1.70, 'preço105': 2.20,
          'preço106': 1.00}

codigos = [100, 101, 102, 103, 104, 105, 106]

soma = 0

contar = {'contar100': 0, 'contar101': 0, 'contar102': 0, 'contar103': 0, 'contar104': 0, 'contar105': 0,
          'contar106': 0}

totcontar = {'totcontar100': 0, 'totcontar101': 0, 'totcontar102': 0, 'totcontar103': 0, 'totcontar104': 0,
             'totcontar105': 0, 'totcontar106': 0}


def menu():
    print('-' * 50)
    print('Especificação         Código            Preço')
    print('-' * 50)
    for codigo in codigos:
        codigostr = str(codigo)
        print(f'{produtos["nome"+codigostr]:<16}        {codigo}', f'           R$ {precos["preço" + codigostr]:.2f}')


while True:
    menu()
    sleep(0.5)
    codigo1 = int(input('Digite o código do produto: '))
    while codigo1 not in codigos:
        print('Código inexistente')
        codigo1 = int(input('Digite o código do produto: '))
    quant = int(input('Digite a quantidade do produto: '))

    for codigo in codigos:
        if codigo == codigo1:
            codigostr = str(codigo)
            soma = soma + (precos['preço'+codigostr] * quant)
            contar['contar' + codigostr] = contar['contar' + codigostr] + (1 * quant)
            totcontar['totcontar' + codigostr] = totcontar['totcontar' + codigostr] + (precos['preço' + codigostr]
                                                                                       * quant)

    op = str(input('Quer continuar adicionando [S/N]? ')).upper().strip()[0]
    while op not in 'SsNn':
        print('Opção inválida !')
        op = str(input('Quer continuar adicionando [S/N]? ')).upper().strip()[0]
    if op in 'N':
        print(f'O resultado da conta foi de R${soma:.2f}')
        for codigo in codigos:
            codigostr = str(codigo)
            if contar['contar' + codigostr] > 1:
                print(f'{contar["contar" + codigostr]:.0f}x {(produtos["nome" + codigostr])} = R$'
                      f'{totcontar["totcontar" + codigostr]:.2f}')
        break
    if op in 'S':
        continue
input()
