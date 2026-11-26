from models.compromisso import Compromisso
from banco.db import get_db
from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId



class Agenda:

    def __init__(self):
        self.compromissos = get_db()["compromissos"]

    def listar_compromissos(self):
        try:
            compromissos = list(self.compromissos.find().sort("titulo", 1))
        except Exception as erro:
            print(f"Erro ao buscar compromissos: {erro}")
            return

        if not compromissos:
            print("Nenhum compromisso cadastrado.")
            return

        print(f"\n=== {len(compromissos)} compromisso(s) ===\n")

        for i, compromisso in enumerate(compromissos, start=1):
            print(f"{i}. {compromisso['titulo']}")
            print(f"   Descrição: {compromisso.get('descricao', '-')}")
            print(f"   Pessoas: {', '.join(compromisso.get('lista_pessoas', [])) or 'ninguém'}")
            print(f"   ID: {compromisso['_id']}")
            print()

    #helper
    def buscar_compromisso_por_id(self):
        self.listar_compromissos()

        id_digitado = input("Digite o ID do compromisso: ")

        try:
            id_digitado = ObjectId(id_digitado)
        except InvalidId:
            print("ID inválido.")
            return None

        try:
            compromisso = self.compromissos.find_one({"_id": id_digitado})
        except Exception as erro:
            print(f"Erro ao buscar compromisso: {erro}")
            return None

        if compromisso is None:
            print("Não existe um compromisso com esse ID.")

        return compromisso

    #helper
    def ler_pessoas(self):
        try:
            qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
        except ValueError:
            print("Quantidade inválida.")
            return None

        pessoas = []
        for i in range(1, qtd_pessoas + 1):
            pessoa_nome = input(f"Digite o nome da {i}ª: ")
            pessoas.append(pessoa_nome)

        return pessoas

    def cadastrar_compromisso(self):
        titulo_compromisso = input("Digite o nome do compromisso: ")
        descricao_compromisso = input("Digite uma descrição: ")

        pessoas = self.ler_pessoas()
        if pessoas is None:
            return

        novo_compromisso = Compromisso(titulo_compromisso, descricao_compromisso, pessoas, datetime.now())

        try:
            resultado = self.compromissos.insert_one({
                "titulo": novo_compromisso.titulo,
                "descricao": novo_compromisso.descricao,
                "lista_pessoas": novo_compromisso.pessoas,
                "data_hora": novo_compromisso.data_horario
            })
            print(f"Compromisso salvo! ID: {resultado.inserted_id}")
        except Exception as erro:
            print(f"Erro ao salvar compromisso: {erro}")

    def alterar_titulo_descricao_compromisso(self):
        compromisso = self.buscar_compromisso_por_id()
        if compromisso is None:
            return

        novo_titulo = input(f"Novo título (atual: {compromisso['titulo']}): ")
        nova_descricao = input(f"Nova descrição (atual: {compromisso.get('descricao', '-')}): ")

        try:
            self.compromissos.update_one(
                {"_id": compromisso["_id"]},
                {"$set": {"titulo": novo_titulo, "descricao": nova_descricao}}
            )
            print("Compromisso atualizado.")
        except Exception as erro:
            print(f"Erro ao atualizar compromisso: {erro}")

    def alterar_pessoas_compromisso(self):
        compromisso = self.buscar_compromisso_por_id()
        if compromisso is None:
            return

        pessoas_atuais = compromisso.get("lista_pessoas", [])
        print(f"Pessoas atuais: {', '.join(pessoas_atuais) or 'ninguém'}")
        print("Informe a nova lista de pessoas.")

        novas_pessoas = self.ler_pessoas()
        if novas_pessoas is None:
            return

        try:
            self.compromissos.update_one(
                {"_id": compromisso["_id"]},
                {"$set": {"lista_pessoas": novas_pessoas}}
            )
            print("Pessoas atualizadas.")
        except Exception as erro:
            print(f"Erro ao atualizar pessoas: {erro}")

    def excluir_pessoa_compromisso(self):
        compromisso = self.buscar_compromisso_por_id()
        if compromisso is None:
            return

        pessoas = compromisso.get("lista_pessoas", [])
        if not pessoas:
            print("Esse compromisso não tem pessoas.")
            return

        for i, pessoa in enumerate(pessoas, start=1):
            print(f"{i}. {pessoa}")

        try:
            numero = int(input("Digite o número da pessoa a excluir: "))
        except ValueError:
            print("Número inválido.")
            return

        if numero < 1 or numero > len(pessoas):
            print("Número inválido.")
            return

        pessoa_removida = pessoas[numero - 1]

        try:
            self.compromissos.update_one(
                {"_id": compromisso["_id"]},
                {"$pull": {"lista_pessoas": pessoa_removida}}
            )
            print(f"'{pessoa_removida}' removido(a) do compromisso.")
        except Exception as erro:
            print(f"Erro ao excluir pessoa: {erro}")

    def excluir_compromisso(self):
        compromisso = self.buscar_compromisso_por_id()
        if compromisso is None:
            return

        confirmar = input(f"Excluir '{compromisso['titulo']}'? (s/n): ").lower()

        if confirmar != "s":
            print("Exclusão cancelada.")
            return

        try:
            self.compromissos.delete_one({"_id": compromisso["_id"]})
            print("Compromisso excluído.")
        except Exception as erro:
            print(f"Erro ao excluir compromisso: {erro}")
