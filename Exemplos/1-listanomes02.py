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

print('Novos nomes adicionados a lista com sucesso')

for nome in nomes:
    print('O nome {} aparece {} vezes nessa lista'.format(
        nome, nomes.count(nome)
))