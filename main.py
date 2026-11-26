from models.agenda import Agenda

def main():

    agenda_manager = Agenda()


    opc = -1
    while opc != "0":
            print("\nMyAgenda")
            print("-"*20+"")

            print("1 - Listar compromissos\n")
            print("2 - Cadastrar novo compromisso\n")
            print("3 - Alterar título e descrição de um compromisso\n")
            print("4 - Alterar as pessoas envolvidas em um compromisso\n")
            print("5 - Excluir uma pessoa em um compromisso\n")
            print("6 - Excluir um compromisso\n")
            print ("0 - Finalizar agenda\n")
            opc = input("Digite a opção desejada: ")

            match opc:
                case "1":
                    agenda_manager.listar_compromissos()
                    input("")

                    
                case "2":
                    agenda_manager.cadastrar_compromisso()
                    input("")

                case "3":
                    agenda_manager.alterar_titulo_descricao_compromisso()
                    input("")
                    
                case "4":
                    agenda_manager.alterar_pessoas_compromisso()
                    input("")


                case "5":
                    agenda_manager.excluir_pessoa_compromisso()
                    input("")

                case "6":
                    agenda_manager.excluir_compromisso()
                    input("")

                case "0":
                    print("Finalizando agenda...")

                case _:
                    print("Essa opção não existe")



if __name__ == '__main__':
    main()
