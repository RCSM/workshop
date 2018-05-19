# E SE eu só quiser adicionar um novo nome se ele for iniciado em uma letra específica?
# Digamoz, K?

nomes = [
    'Alice','Miguel','Sophia','Arthur','Helena','Bernardo',
    'Valentina','Heitor','Laura','Davi','Isabella','Lorenzo',
    'Manuela','Théo','Júlia','Pedro','Heloísa','Gabriel','Luiza',
    'Enzo','Maria','Luiza','Matheus', 'Rafael', 'Felipe', 'Stefany'
]

print('Lista de nomes : {}'.format(nomes))
novo_nome = input('Digite um nome a ser adicionado na lista : ')

if not novo_nome in nomes:
    nomes.append(novo_nome)
else:
    print('Oops. Esse nome já existe na lista')