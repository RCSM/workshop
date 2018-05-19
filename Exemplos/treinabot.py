"""
Operações de adição em dicionário de forma genérica

:param dict: objeto no qual o dado vai ser adicionado
:param chave: chave para o novo valor a ser adicionado
:param valor: valor referente a chave adicionada

:return: dicionário com o novo par adicionado
"""
def add_cmd(comandos, palavra_chave, comando):
    comandos[palavra_chave] = comando
    return comando


def add_frase_especifica(frases, palavra_chave, nova_frase):
    frases[palavra_chave] = nova_frase
    return frases


def add_frase(frases_genericas, frase):
    """
    Operação de adição de itens em lista de falas genéricas

    :param falas_genéricas: lista na qual fala vai ser adicionada
    :param fala: fala que vai ser adicionada a lista

    :return: lista com novo item adicionado
    """
    frases_genericas.append(frase)
    return frases_genericas