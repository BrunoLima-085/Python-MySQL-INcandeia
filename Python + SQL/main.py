from database import Database
from repositorio import Repositorio
import operacoes

def menu():
    print("\nINcandeia - Gerenciamento")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Atualizar produto")
    print("4. Deletar produto")
    print("5. Realizar venda")
    print("6. Listar vendas")
    print("7. Atualizar venda")
    print("8. Deletar venda")
    print("0. Sair")
    return input("Escolha: ")

def sair():
    print("Saindo...")
    return False

def opcao_invalida():
    print("Opção inválida!")

def main():
    db = Database()
    produto = Repositorio(db, "produto")
    venda = Repositorio(db, "venda")

    opcoes = {
        "1": lambda: operacoes.cadastrar_produto(produto),
        "2": lambda: operacoes.listar_produtos(produto),
        "3": lambda: operacoes.atualizar_produto(produto),
        "4": lambda: operacoes.deletar_produto(produto),
        "5": lambda: operacoes.realizar_venda(produto, venda),
        "6": lambda: operacoes.listar_vendas(venda),
        "7": lambda: operacoes.atualizar_venda(venda),
        "8": lambda: operacoes.deletar_venda(venda),
        "0": sair
    }

    continuar = True
    while continuar:
        escolha = menu()
        funcao = opcoes.get(escolha, opcao_invalida)
        resultado = funcao()
        if resultado is False:
            continuar = False

    db.close()

if __name__ == "__main__":
    main()