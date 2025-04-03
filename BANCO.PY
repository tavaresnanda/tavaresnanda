import flet as ft

def main (page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = '400'
    page.window_height = '550'
    page.window_resizable = False
    page.window_maximizable = False
    page.window_center()


    n= ft.TextField (label = 'Nome',autofocus=True)
    btn = ft.CupertinoFilledButton(content=ft.Text('Guardar'),width=500,on_click=True)
   
    btn2=ft.CupertinoFilledButton(content=ft.Text('Pesquisar'),width=115,height=50,on_click=True)
    btn3=ft.CupertinoFilledButton(content=ft.Text('alterar'),width=115,height=50,on_click=True)
    btn4=ft.CupertinoFilledButton(content=ft.Text('Deletar'),width=115,height=50,on_click=True)
    
    
    c= ft.Row([btn2,btn3,btn4])

    cont = ft.Container(bgcolor="#000000",width=500,height=300,border_radius=5)

    page.add(n,btn,cont,c)
ft.app(target=main)
