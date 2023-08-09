from teste import Teste

objeto_da_classe_teste = Teste(True, False)

objeto2 = Teste('está limpo', 'está sujo')
print(f'o objeto {objeto2.sujo}')

objeto3 = Teste(1, 2)
print(f'o valor de limpo é {objeto3.limpo}')
print(f'o valor de sujo é {objeto3.sujo}')

print(objeto_da_classe_teste.limpo)
print(objeto_da_classe_teste.sujo)