nomes = [
    'Alice','Miguel','Sophia','Arthur','Helena','Bernardo',
    'Valentina','Heitor','Laura','Davi','Isabella','Lorenzo',
    'Manuela','Théo','Júlia','Pedro','Heloísa','Gabriel','Luiza',
    'Enzo','Maria','Luiza','Matheus', 'Rafael', 'Felipe', 'Stefany'
]

print('Lista de nomes : {}'.format(nomes))
novo_nome = input('Digite os nomes a serem adicionados na lista : ')

nomes.append(novo_nome)

print('Novo nome adicionado a lista com sucesso')