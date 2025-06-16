from datetime import datetime

def cadastrar_produto(produto):
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    qtd = int(input("Quantidade disponível: "))
    preco = float(input("Preço do produto: "))
    produto.cadastrar(
        ["nome", "descricao", "quantidade_disponivel", "preco"],
        [nome, descricao, qtd, preco]
    )
    print("Produto cadastrado com sucesso!")

def listar_produtos(produto):
    for i in produto.listar() or []:
        print(i)

def atualizar_produto(produto):
    id_ = int(input("Forneça o id do produto: "))
    i = produto.buscar(id_)
    if not i:
        print("Produto não encontrado ou não existe!")
        return
    nome = input(f"Nome [{i['nome']}]: ") or i['nome']
    descricao = input(f"Descrição [{i['descricao']}]: ") or i['descricao']
    qtd = int(input(f"Quantidade [{i['quantidade_disponivel']}]: ")) or i['quantidade_disponivel']
    preco = float(input(f"Preço [{i['preco']}]: ")) or i['preco']
    produto.atualizar(id_,
                      ["nome", "descricao", "quantidade_disponivel", "preco"],
                      [nome, descricao, qtd, preco]
    )
    print("Produto atualizado com sucesso!")

def deletar_produto(produto):
    id_ = int(input("Forneça o id do produto: "))
    produto.deletar(id_)
    print("Produto deletado com sucesso!")

def realizar_venda(produto, venda):
    id_produto = int(input("Forneça o id do produto: "))
    qtd = int(input("Forneça a quantidade: "))
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    venda.cadastrar(
        ["id_produto", "quantidade_vendida", "data_venda"],
        [id_produto, qtd, data]
    )
    print("Venda realizada com sucesso!")

def listar_vendas(venda):
    for i in venda.listar() or []:
        print(i)

def atualizar_venda(venda):
    id_ = int(input("Forneça o id da venda: "))
    i = venda.buscar(id_)
    if not i:
        print("Venda não encontrada ou não existe!")
        return
    id_produto = int(input(f"id Produto [{i['id_produto']}]") or i['id_produto'])
    qtd = int(input(f"Quantidade [{i['quantidade_vendida']}]") or i['quantidade_vendida'])
    data = input(f"Data [{i['data_venda']}]" or i['data_venda'])
    venda.atualizar(id_,
                    ["id_produto", "quantidade_vendida", "data_venda"],
                    [id_produto, qtd, data]
    )
    print("Venda atualizada com sucesso!")

def deletar_venda(venda):
    id_ = int(input("Forneça o id da venda: "))
    venda.deletar(id_)
    print("Venda deletada com sucesso!")