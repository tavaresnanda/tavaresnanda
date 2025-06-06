import flet as ft

def main (page: ft.Page):
    page.window_center()
    page.bgcolor = '#4169E1'
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
        
        ft.Text("Faça seu login", size= 35), 
        ft.TextField (label= "E-mail", icon= ft.icons.ACCOUNT_BOX),
        ft.TextField (label= "Senha", icon= ft.icons.PASSWORD),
        ft.FilledTonalButton (text = 'Entrar', width = 300,height=40,style=ft.ButtonStyle(bgcolor='#4169E1',color='#ffffff'),on_click=lambda e:entrar(e)),
        ft.TextButton (text = "Esqueceu a senha?", width = 500),
        ft.TextButton (text = "Não tem conta? Fazer cadastro", width = 500),


        ], alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        spacing= 30
        )
        ),
         ft.Container(
        width=450,
        height=540,
        border_radius= 5,
        padding=30,
         content= ft.Column ([  
        ft.Image (src=f'codificacao.png',
        width = 200, height = 200,
        fit = ft.ImageFit.CONTAIN),
        ft.Text('A melhor experiência de login\n que você já teve na vida.',
        size=20, 
        color='#ffffff')
    ],alignment=ft.MainAxisAlignment.CENTER,
       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=40
    )
    )
     ])
    #teladecadastro
    

    c2= ft.Row([
        ft.Container(
        padding=30,
        bgcolor='#ffffff',
        width=950,
        height=250,
        border_radius= 5,
        content= ft.Column([
       
        ft.Text('Dados do usuário:',size= 35), 
        ft.Row([
        ft.TextField (label= "CPF",width=240,height=40,border_radius=10),
        ft.TextField (label= "Nome completo", width=300,height=40,border_radius=10),
        ft.TextField (label= "Data de nascimento", width=230,height=40,border_radius=10),
        ]),
        ft.Row([
        ft.TextField (label= "Nome da mãe",width=300,height=40,border_radius=10),
        ]),
    ft.Column([
        ft.CupertinoFilledButton(text='Salvar',on_click=lambda e: salvar (e),width=220,height=46,)
    
    ])
    ])

    ),
    ])


    
    c3= ft.Row([
        ft.Container(
        padding=30,
        bgcolor='#ffffff',
        width=950,
        height=250,
        border_radius= 5,
        content= ft.Column([

            ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice",width = 500)),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                    ],
                ),
            ],
        ),
         ],alignment=ft.MainAxisAlignment.CENTER,
       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=40)
        )
             ])




    
    cadastro=ft.Column([
       ft.CupertinoFilledButton(text='Voltar',on_click=lambda e: voltar (e))
    
    ])
    
    

    def entrar(e:ft.ControlEvent):

        page.remove(c1)
        page.add(cadastro)

    def voltar(e:ft.ControlEvent):
        
        page.remove(cadastro)
        page.add(c1)

    def salvar(e:ft.ControlEvent):
        
        page.salvar(c1)
        page.add(salvar)



     
    page.add(c1,c2,c3)
ft.app(target=main)
