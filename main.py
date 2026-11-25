from models.agenda import Agenda

def main():
    print("\nMyAgenda")
    print("-"*20+"")

    print("1 - Listar compromissos\n")
    print("2 - Cadastrar novo compromisso\n")
    print("3 - Alterar título e descrição de um compromisso\n")
    print("4 - Alterar as pessoas envolvidas em um compromisso\n")
    print("5 - Excluir uma pessoa em um compromisso\n")
    print("6 - Excluir um compromisso\n")
    opc = input("Digite a opção desejada: ")

    agenda_manager = Agenda()

    match opc:
        case "1":
            print("Selecionou")
            #agenda_manager.listar_compromissos()

            
        case "2":
            print("Selecionou")
            #agenda_manager.cadastrar_compromisso()

        case "3":
            print("Selecionou")
            #agenda_manager.alterar_titulo_descricao_compromisso()
            
        case "4":
            print("Selecionou")
            #agenda_manager.alterar_pessoas_compromisso()


        case "5":
            print("Selecionou")
            #agenda_manager.excluir_pessoa_compromisso()

        case "6":
            print("Selecionou")
            #agenda_manager.excluir_compromisso()


        case _:
            print("Essa opção não existe")



if __name__ == '__main__':
    main()
