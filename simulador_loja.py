# Simulador de Loja --------------------------------------------------------

estoque = {
    "notebook": {"valor": 3500.00, "quantidade": 3},
    "smartphone": {"valor": 2400.00, "quantidade": 4},
    "fones de ouvido": {"valor": 150.00, "quantidade": 12},
    "mochila": {"valor": 180.00, "quantidade": 10},
    "monitor": {"valor": 899.90, "quantidade": 5},
    "mouse": {"valor": 99.90, "quantidade": 10},
    "teclado": {"valor": 120.00, "quantidade": 8}
}

carrinho = {}

def adicionar_produto(produto, quantidade):
    if produto in estoque:
        if quantidade <= estoque[produto]["quantidade"]:
            if produto in carrinho:
                carrinho[produto]["quantidade"] += quantidade
                carrinho[produto]["valor"] = carrinho[produto]["quantidade"] * estoque[produto]["valor"]
            else:
                carrinho[produto] = {"quantidade": quantidade, "valor": estoque[produto]["valor"] * quantidade}
            
            estoque[produto]["quantidade"] -= quantidade
            print(f"{quantidade}x {produto.capitalize()} adicionado(s) ao carrinho.")
        else:
            print("Quantidade maior do que disponível no estoque.")
    else:
        print("Produto não encontrado.")

def remover_produto(produto, quantidade):
    if produto in carrinho:
            if quantidade <= carrinho[produto]["quantidade"]:
                carrinho[produto]["quantidade"] -= quantidade
                carrinho[produto]["valor"] = carrinho[produto]["quantidade"] * estoque[produto]["valor"]
                
                print(f"{quantidade}x {produto.capitalize()} removido(s) do carrinho.")
                
                if carrinho[produto]["quantidade"] == 0:
                    del carrinho[produto]
                estoque[produto]["quantidade"] += quantidade
            else:
                print("Inválido. Quantidade maior a quantidade adicionada ao carrinho.")
    else:
        print("Produto não encontrado.")

print("Loja de Informática")

while True:
    print("\nopções: 0= sair / 1= visualizar produtos / 2= adicionar produto/ 3= visualizar carrinho / 4= remover produto")
    try:
        menu = int(input("Digite uma opção: "))
        if menu < 0 or menu > 4:
            raise ValueError
    except ValueError:
        print("Digite uma opção válida.")
    else:
        match menu:
            case 0:
                print("\nFinalizando...")
                break
        
            case 1:
                print("\nProdutos no estoque:")
                for produto, informacao_produto in estoque.items():
                    print(f"{produto.capitalize()}, valor: R${informacao_produto['valor']}, estoque: {informacao_produto['quantidade']}.")
            
            case 2:
                print("\nAdicionar um produto ao carrinho:")
                produto = input("Nome do produto: ").lower().strip()
                while True:
                    try:
                        quantidade = int(input("Quantidade: "))
                        if quantidade <= 0:
                            raise ValueError
                        
                        adicionar_produto(produto, quantidade)
                        break
                    except ValueError:
                        print("Digite uma quantidade válida.")
            
            case 3:
                soma = 0
                print("\nCarrinho:")
                if carrinho:
                    for produto, informacao_produto in carrinho.items():
                        print(f"{informacao_produto['quantidade']}x {produto.capitalize()}, R${informacao_produto['valor']}.")
                        soma += informacao_produto["valor"]
                    print(f"Valor total: {soma:.2f}")
                else:
                    print("Não há produtos no carrinho.")
            
            case 4:
                print("\nRemover um produto do carrinho:")
                if carrinho:
                    produto = input("Nome do produto: ").lower().strip()
                    while True:
                        try:
                            quantidade = int(input("Quantidade: "))
                            if quantidade <= 0:
                                raise ValueError
                            
                            remover_produto(produto, quantidade)
                            break
                        except ValueError:
                            print("Digite uma quantidade válida.")
                else:
                    print("Não há produtos no carrinho.")
