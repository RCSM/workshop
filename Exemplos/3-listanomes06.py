nomes = [
    'Alice','Miguel','Sophia','Arthur','Helena','Bernardo',
    'Valentina','Heitor','Laura','Davi','Isabella','Lorenzo',
    'Manuela','Théo','Júlia','Pedro','Heloísa','Gabriel','Luiza',
    'Enzo','Maria','Luiza','Matheus', 'Rafael', 'Felipe', 'Stefany'
]

print('Lista de nomes : {}'.format(nomes))
novos_nomes = input('Digite os nomes a serem adicionados na lista : ')
novos_nomes = novos_nomes.split()

for nome in novos_nomes:
    if not nome in nomes:
        nomes.append(nome)
    else:
        print('Oops. O nome {} já existe na lista'.format(nome))

print('Lista de nomes(após adição) : {}'.format(nomes))