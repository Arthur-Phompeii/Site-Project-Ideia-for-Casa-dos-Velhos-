# Estrutura de dados para representar vendas
vendas = [
 {"id": 1, "produto": "Notebook", "preco": 3500.00, "categoria": "Eletrônicos"},
 {"id": 2, "produto": "Mouse", "preco": 50.00, "categoria": "Acessórios"}, 
 {"id": 3, "produto": "Teclado", "preco": 150.00, "categoria": "Acessórios"}, 
 {"id": 4, "produto": "Monitor", "preco": 800.00, "categoria": "Eletrônicos"}, 
 {"id": 5, "produto": "Webcam", "preco": 200.00, "categoria": "Acessórios"}
]

def categorias_vendidas(lista_vendas):
    """Retorna conjunto de categorias únicas."""
    return {venda["categoria"] for venda in lista_vendas}

def vendas_por_categoria(lista_vendas):
    """Agrupa vendas por categoria."""
    resultado = {}
    for venda in lista_vendas:
        cat = venda["categoria"]
        if cat not in resultado:
            resultado[cat] = []
        resultado[cat].append(venda)
    return resultado

def produto_mais_caro(lista_vendas):
    """Encontra o produto com maior preço."""
    if not lista_vendas:
        return None
    return max(lista_vendas, key=lambda v: v["preco"])

# Usando as funções
categorias = categorias_vendidas(vendas)
print(f"Categorias: {categorias}")  # {'Eletrônicos', 'Acessórios'}

por_categoria = vendas_por_categoria(vendas)
print(f"Produtos em Eletrônicos: {len(por_categoria['Eletrônicos'])}")

caro = produto_mais_caro(vendas)
print(f"Produto mais caro: {caro['produto']} - R${caro['preco']:.2f}")

"""Calculo de média com tratamento de erros"""
def obter_media_vendas(vendas):
    """Calcula média de preços com validação."""
    if not vendas or not isinstance(vendas, list):
        raise ValueError("Lista de vendas inválida")
    
    precos = [v.get("preco", 0) for v in vendas if isinstance(v, dict)]
    
    if not precos:
        return 0
    
    return sum(precos) / len(precos)

# Uso seguro

try:
    media = obter_media_vendas(vendas)
    print(f"Média: R${media:.2f}")
except ValueError as e:
    print(f"Erro: {e}")