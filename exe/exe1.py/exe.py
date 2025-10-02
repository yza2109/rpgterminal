loja_frutas = {
      'maca': 2.40,
      'banana': 3.60,
      'uva': 7.60,
  }

# função get: método usado para acessar o valor em um dicionário
preco_uva = loja_frutas.get('uva',{})
print('uva:', preco_uva)

# função update: método usado para atualizar os valores do dicionário
loja_frutas.update({'uva': 8.90, 'tomate': 10})
print(loja_frutas, '#tomate adicionado')

loja_frutas.pop('tomate')
print(loja_frutas, '#tomate removido')

for chave, valor in loja_frutas.items():
  print(f'key: {chave}: value: {valor}')


