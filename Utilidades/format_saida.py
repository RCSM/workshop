print("Essa é uma saída simples(também chamado de output)")

print('\n\nSaída em múltiplas linhas :'
    + '\nPrimeira linha'
    + '\nSegunda linha'
    + '\nNão sei se já viu, mas isso aqui é bom pra montar menu kkk')

linha1 = '\n-> Linha 1'
linha2 = '\n-> Linha 2'
linha3 = '\n-> Linha 3'
print('\n\nFormatando saída com valores concatenados na saída : '
    + linha1 + linha2 + linha3)

print('\n\nFormatando saída com variáveis : {}, {}, {}'.format(
    linha1, linha2, linha3
))