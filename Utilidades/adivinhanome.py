from random import randint

nomes = [
    'Alice','Miguel','Sophia','Arthur','Helena','Bernardo',
    'Valentina','Heitor','Laura','Davi','Isabella','Lorenzo',
    'Manuela','Théo','Júlia','Pedro','Heloísa','Gabriel','Luiza',
    'Enzo','Maria','Luiza','Matheus', 'Rafael', 'Felipe', 'Stefany'
]


def add_nome(nome):
    nomes.append(nome)


def add_nomes(nomes):
    nomes.extend(nomes)


def rm_nome(nome):
    nomes.remove(nome)


def rm_primeiro_nome():
    nomes.pop()


def mostra_nomes_ordem_rev():
    print('Lista de nomes na ordem reverse : {}'.format(nomes[::-1]))


def mostra_nomes():
    print('Lista de nomes : {}'.format(nomes))
    # Funciona da mesma forma usando nomes[::] ou nomes[0, len(nomes), 1]


def jogo():
    nome_sorteado = nomes[randint(0, len(nomes)+1)]
    palpite = input('Adivinhe o nome que acabou de ser sorteado(ou digite N para encerrar) : ')
    while nome_sorteado != palpite:
        if palpite == 'N':
            break
            return # Apenas para sair do loop
        else:
            nome_sorteado = nomes[randint(0, len(nomes)+1)]
            palpite = input('Adivinhe o nome que acabou de ser sorteado(ou digite N para encerrar) : ')
    print('Mas já? Bom chute hehe')


def menu():
    opcao = input('-- Menu --'
                + '1. Adicionar nome'
                + '2. Adicionar mais de um nome'
                + '3. Remover um nome'
                + '4. Remover o primeiro nome'
                + '5. Jogar "Adivinhação de nome"'
                + '6. Encerrar'
                + 'Digite o número de opção desejada')
    if opcao == 1:
        nome = input('Digite o nome a ser inserido : ')
        add_nome(nome)
        mostra_nomes()
    elif opcao == 2:
        nomes = input('Digite os nomes a serem inseridos : ')
        add_nomes(nomes)
        mostra_nomes()
    elif opcao == 3:
        nome = input('Digite o nome a ser removido : ')
        add_nome(nome)
        mostra_nomes()
    elif opcao == 4:
        rm_primeiro_nome()
        mostra_nomes()
    elif opcao == 5:
        jogo()
    else:
        return False
    return True


def main():
    flag = True
    while flag:
        flag = menu()
#       jogo()

if __name__ == "__main__":
    main()