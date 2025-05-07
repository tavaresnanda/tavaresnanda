import flet as ft
import pymysql

def main(page: ft.Page):
    page.title = "Exibindo dados"
    page.scroll = True

    #Conexão com banco de dados 
    conexao = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="vendas"
    )
    cursor = conexao.cursor()

    #Consulta sql
    cursor.execute("SELECT IDCARGO, NOMECARGO FROM cargo")
    resultados = cursor.fetchall()

    #Consulta da tabela
    colunas = [
        ft.DataColumn(ft.Text("IDCARGO")),
        ft.DataColumn(ft.Text("NOMECARGO")),
    ]

    linhas =[]
    for linha in resultados:
        linhas.append(
            ft.DataRow(
                cells=[ft.DataCell(ft.Text(str(c))) for c in linha]
            )
        )

    tabela = ft.DataTable(columns=colunas, rows=linhas)

    nome = ft.TextField(label="Digite um Cargo")
    btn = ft.ElevatedButton(text="Salvar")
   

    page.add(nome,btn,tabela)

    cursor.close()
    conexao.close()

ft.app(target=main)
