def jogar():
    print('===== JOGO DA FORCA ATUALIZADO 1.0 2.0 3.0 ====')

    palavra_escolhida = input("DIGITE A PALAVRA A SER ENCONTRADA:  ")
    tamanho_da_palavra = len(palavra_escolhida)
    lista = []
    comparacao_palavra = []
    errou = 1
    rodadas = tamanho_da_palavra + int(tamanho_da_palavra*0.7)

    for _ in range(0,tamanho_da_palavra):
        lista.append('_')
        comparacao_palavra.append('_')

    while True:
        index = 0
        print(f'Indice de acerto da palavra >> {lista}')
        print(f'Rodada número >> {errou}/{rodadas}')
        chute = input(' DIGITE UMA LETRA:  ')
        chute = chute.strip()

        for letra in palavra_escolhida:
            comparacao_palavra[index] = letra.upper()

            if chute.upper() == letra.upper():
                print(f' Encontrou a letra "{chute.upper()}" na posicao {index}')
                lista[index]  = letra.upper()

            index += 1

        if errou == rodadas:
            print(f'Indice de acerto da palavra >> {lista}')
            print(f' Essa foi a rodada {errou}/{rodadas}, vc PERDEU!')
            break
        errou += 1

        if lista == comparacao_palavra:
            print(f'Indice de acerto da palavra >> {lista}')
            print('VOCE VENCEU! ')
            break



if __name__ == '__main__':
    jogar()
