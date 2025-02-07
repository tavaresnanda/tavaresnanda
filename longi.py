
import flet as ft

def main (page: ft.Page):
    page.window_center()
    page.bgcolor = '#0F0F26'
    page.window_width = '500'
    page.window_height = '600'
    page.window_resizable = False
    page.window_maximizable = False
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.padding=50

    c1=ft.Container(
        padding=30,
        bgcolor= '#F2D22E',
        width=450,
        height=500,
        border_radius=10, 
        alignment=ft.alignment.center,

        content= ft.Column([


            ft.Image ( src = f'usuario.png', width = 500, height = 80, fit = ft.ImageFit.CONTAIN),
            ft.TextField ( label = "Usuário"),
            ft.TextField (label = "Senha"),
            ft.FilledTonalButton (text = 'Entrar', width = 500),
            ft.TextButton (text = "Esqueceu a senha?", width = 500),
            ft.TextButton (text = "Não tem conta? Fazer cadastro", width = 500),

        ]) 
    )

    
    page.add(c1)
ft.app(target=main)
