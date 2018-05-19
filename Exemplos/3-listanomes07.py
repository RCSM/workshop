nomes = [
    'Alice','Miguel','Sophia','Arthur','Helena','Bernardo',
    'Valentina','Heitor','Laura','Davi','Isabella','Lorenzo',
    'Manuela','Théo','Júlia','Pedro','Heloísa','Gabriel','Luiza',
    'Enzo','Maria','Luiza','Matheus', 'Rafael', 'Felipe', 'Stefany'
]

print('Lista de nomes : {}'.format(nomes))
novos_nomes = input('Digite os nomes a serem adicionados na lista : ')
novos_nomes = novos_nomes.split()

nomes.extend(novos_nomes)

print('Lista de nomes(após adição) : {}'.format(nomes))

for nome in nomes:
    if nomes.count(nome) > 1:
        nomes.remove(nome)

print('Lista de nomes(após remoção) : {}'.format(nomes))