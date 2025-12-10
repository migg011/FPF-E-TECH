# Crie a função calcular_custo_total que aceita
# um custo fixo obrigatório e utiliza *args para
# receber os custos de itens variáveis.
# A função deve retornar o valor total somado.

def calcular_custo_total(custo_fixo, *items_comprados):

    total_itens = 0

    for item in items_comprados:
        total_itens += item

    valor_total = custo_fixo + total_itens

    return valor_total

valor_total_pedido = calcular_custo_total(25.0, 10.0, 25.00, 5.0)
print(f"Custo total do pedido: {valor_total_pedido}")
