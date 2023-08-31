with open("prova1.txt", "r") as file: #MUDAR O ARQUIVO DE ENTRADA NAS PRIMEIRAS ASPAS
    lines = file.readlines()
    conteudo = '\r'.join(lines)
    clean_content = conteudo.replace('\n', '')
    lista_conteudo = clean_content.split('\r')


def principal():
    for i in range(len(lista_conteudo)):
        if lista_conteudo[i] == 'U':
            print('É uma UNIÃO - U')
            set_1 = set()
            set_str = lista_conteudo[i + 1]
            lista = set_str.split(',')
            for num in lista:
                set_1.add(num)
            print('Conjunto 1:', set_1)

            set_2 = set()
            set_str2 = lista_conteudo[i + 2]
            lista = set_str2.split(',')
            for num in lista:
                set_2.add(num)
            print('Conjunto 2:', set_2)

            print('O conjunto união entre 1 e 2 é: ', set_1.union(set_2), '\n\n')

        elif lista_conteudo[i] == 'I':
            print('É uma INTERSECCAO - I')
            set_1 = set()
            set_str = lista_conteudo[i + 1]
            lista = set_str.split(',')
            for num in lista:
                set_1.add(num)
            print('Conjunto 1:', set_1)

            set_2 = set()
            set_str2 = lista_conteudo[i + 2]
            lista = set_str2.split(',')
            for num in lista:
                set_2.add(num)
            print('Conjunto 2:', set_2)

            print('O conjunto intersecção entre 1 e 2 é: ', set_1.intersection(set_2), '\n\n')

        elif lista_conteudo[i] == 'D':
            print('É uma DIFERENCA - D')
            set_1 = set()
            set_str = lista_conteudo[i + 1]
            lista = set_str.split(',')
            for num in lista:
                set_1.add(num)
            print('Conjunto 1:', set_1)

            set_2 = set()
            set_str2 = lista_conteudo[i + 2]
            lista = set_str2.split(',')
            for num in lista:
                set_2.add(num)
            print('Conjunto 2:', set_2)

            print('O conjunto diferença entre 1 e 2 é: ', set_1.difference(set_2), '\n\n')

        elif lista_conteudo[i] == 'C':
            print('É um PLANO CARTESIANO - C')
            set_1 = set()
            set_str = lista_conteudo[i + 1]
            lista = set_str.split(',')
            for num in lista:
                set_1.add(num)
            print('Conjunto 1:', set_1)

            set_2 = set()
            set_str2 = lista_conteudo[i + 2]
            lista = set_str2.split(',')
            for num in lista:
                set_2.add(num)
            print('Conjunto 2:', set_2)

            set_cartesiano = set()

            for i in set_1:
                for j in set_2:
                    x = (i, j)
                    set_cartesiano.add(x)

            print("O plano cartesiano é:", set_cartesiano, '\n\n')


principal()
