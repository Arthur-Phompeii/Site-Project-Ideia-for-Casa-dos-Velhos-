# Dicionário
# estoque = {}
# usuarios = {
#    "user1": {
#        "nome": "Arthur",
#        "idade": 22
#    },
#    "user2": {
#        "nome": "Maria",
#        "idade": 30
#    }
# }

# Lista
# estoque = []
# usuarios = [
#    {
#        "nome": "Arthur",
#        "idade": 22
#    },
#    {
#        "nome": "Maria",
#        "idade": 30
#    }
# ]

estoque = [
    {
        "nome": str("Produto 1"),
        "quantidade": int(5),
        "preco": float(1080.76),
    },
    {
        "nome": str("Produto 2"),
        "quantidade": int(10),
        "preco": float(67.67),
    },
    {
        "nome": str("Produto 3"),
        "quantidade": int(37),
        "preco": float(0.97),
    },
]

# MENU

while True:
    try:
        # Menu
        print("=" * 35)
        print("1 - Visualizar Estoque Atual")
        print("2 - Registrar Entrada de Produto")
        print("3 - Registrar Saida de Produto")
        print("4 - Sair do Sistema")
        opcao_menu = abs(int(input("\nEscolha uma opcao: ")))

        # Submenus

        if opcao_menu == 1:
            print("=" * 35)
            for produtos in estoque:
                print("-")
                print("Nome:", produtos["nome"])
                print("Quantidade:", produtos["quantidade"])
                print(f"Preço: R${produtos["preco"]}")
            input("-\nPressione Enter para voltar ao Menu")

        elif opcao_menu == 2:
            print("=" * 35)
            nome_produto = input("Digite o nome do produto: ")
            produto_cadastrado = False
            for produtos in estoque:
                if (
                    produtos["nome"] == nome_produto
                ):  # Procura por toda a lista pelo nome digitado no input
                    produto_cadastrado = True
                    print(
                        f"Produto encontrado! Quantidade em estoque: {produtos['quantidade']} unidades."
                    )
                    while (
                        True
                    ):  # Loop para que o programa não seja encerrado caso haja informação errada no input
                        try:
                            entrada = abs(int(input("Quantidade de Entrada: ")))
                            produtos["quantidade"] += entrada
                            print(
                                f"{entrada} unidades foram adcionadas ao estoque de {produtos['nome']}, novo estoque é de {produtos['quantidade']} unidades."
                            )
                            break
                        except ValueError:
                            print("Digite apenas números inteiros!")
            if not produto_cadastrado:
                print(
                    "Produto não Cadastrado!"
                )  # Adicionar jeito de não voltar ao Menu

        elif opcao_menu == 3:
            print("=" * 35)
            nome_produto = input("Digite o nome do produto: ")
            produto_cadastrado = False
            for produtos in estoque:
                if (
                    produtos["nome"] == nome_produto
                ):  # Procura por toda a lista pelo nome digitado no input
                    produto_cadastrado = True
                    print(
                        f"Produto encontrado! Quantidade em estoque: {produtos['quantidade']} unidades."
                    )
                    while (
                        True
                    ):  # Loop para que o programa não seja encerrado caso haja informação errada no input
                        try:
                            saida = abs(int(input("Quantidade a vender: ")))
                            if (
                                saida > produtos["quantidade"]
                            ):  # Verifica disponibilidade de estoque antes de  realizar a saída do estoque
                                print(
                                    f"Quantidade em estoque é insuficiente para venda. Venda até {produtos['quantidade']} unidades ou digite 0 para cancelar a venda."
                                )
                            else:
                                produtos["quantidade"] -= saida
                                print(
                                    f"{saida} unidades foram retiradas do estoque de {produtos['nome']}"
                                )
                                break

                        except ValueError:
                            print("Digite apenas números inteiros!")
            if not produto_cadastrado:
                print(
                    "Produto não Cadastrado!"
                )  # Adicionar jeito de não voltar ao Menu

        elif opcao_menu == 4:
            print("=" * 35)
            print("Programa encerrado")
            print("=" * 35)
            break

        # Tratamento de erros
        else:
            print("Digite apenas os dígitos referentes às opções!")
    except ValueError:
        print("Digite apenas os dígitos referentes às opções!")
