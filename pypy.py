class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}"

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        contato = Contato(nome, telefone)
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado com sucesso.")

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} excluído com sucesso.")
                return
        print(f"Contato {nome} não encontrado na agenda.")

    def editar_contato(self, nome, novo_nome, novo_telefone):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.nome = novo_nome
                contato.telefone = novo_telefone
                print(f"Contato {nome} editado com sucesso.")
                return
        print(f"Contato {nome} não encontrado na agenda.")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia")
        else:
            print("Lista de Contatos:")
            for contato in self.contatos:
                print(contato)

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nSelecione uma opção:")
    print("1. Adicionar contato")
    print("2. Excluir contato")
    print("3. Editar contato")
    print("4. Listar contatos")
    print("5. Sair")

    escolha = input("Digite o número da opção desejada: ")
    return escolha

# Exemplo de utilização
agenda = Agenda()

while True:
    escolha = exibir_menu()

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda.adicionar_contato(nome, telefone)
    elif escolha == "2":
        nome = input("Digite o nome do contato que deseja excluir: ")
        agenda.excluir_contato(nome)
    elif escolha == "3":
        nome = input("Digite o nome do contato que deseja editar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        agenda.editar_contato(nome, novo_nome, novo_telefone)
    elif escolha == "4":
        agenda.listar_contatos()
    elif escolha == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
