import flet as ft

def main (page: ft.Page):
    page.window_center()
    page.bgcolor = '#120f26'
    page.window_width = '1000'
    page.window_height = '600'
    page.window_resizable = False
    page.window_maximizable = False
    
    c1= ft.Row([
        ft.Container(
        padding=30,
        bgcolor='#ffffff',
        width=450,
        height=540,
        border_radius= 5,
        content= ft.Column([
        
        ft.Text("Faça seu Login", size= 35), 
        ft.TextField (label= "E-mail", icon= ft.icons.ACCOUNT_BOX),
        ft.TextField (label= "Senha", icon= ft.icons.PASSWORD),
        ft.FilledTonalButton (text = 'Entrar', width = 250,height=50),
        ft.TextButton (text = "Esqueceu a senha?", width = 500),
        ft.TextButton (text = "Não tem conta? Fazer cadastro", width = 500),


        ], alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        spacing= 30
        )
        ),
         ft.Image ( src = 'programador.png', width = 500, height = 200, fit = ft.ImageFit.CONTAIN)
        ]
        )

    
     
    page.add(c1)
ft.app(target=main)
