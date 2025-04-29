from flet import *

def main(page: Page):
    page.window.center()
    page.window.width = 768
    page.window.height = 500
    page.bgcolor = "#557dff"
    page.padding = 0


    e = TextField(label = "Email", prefix_icon = icons.EMAIL,border_radius=20)

    s = TextField(label = "Senha", prefix_icon = icons.PASSWORD, can_reveal_password = True, password = True,border_radius=20)

    m = TextField(label = "Nome", prefix_icon = icons.PEOPLE_ALT,border_radius=20)

    t = Text("Login",height=90, size= 40,weight= FontWeight.W_900,color="#000000")

    t2 = Text("Olá, amigo!", height= 70, size= 40,weight= FontWeight.W_900,color="#000000")

    t3 = Text("Insira suas informação",height=20,color="#000000")

    t4 = Text("esqueceu sua senha?",height=20,color="#000000")

    t5 = Text("Bem-vindo!",height=70, size= 40,weight= FontWeight.W_900,color="#000000")

    t6 = Text("Criar uma conta",height=90, size= 30,weight= FontWeight.W_900,color="#000000")

    t7 = Text("Use seu e-mail para registro",height=20,color="#000000")

    t8 = Text("Registre-se com seus dados pessoais para \n usar todos os recursos do site",height= 90,color="#000000")

    t9 = Text("Insira seus dados pessoais para usar todos \n os recursos do site",height= 60,color="#000000")

    button1 = FilledButton(text = "Cadastrar",style=ButtonStyle(bgcolor="#557dff",color="#000000"),on_click = lambda e: entrar(e))

    button2 = FilledButton(text = "Voltar",style=ButtonStyle(bgcolor="#557dff",color="#000000"), on_click = lambda e: voltar(e))

    button3 = OutlinedButton(text = "Increver-se",style=ButtonStyle(color="#000000"), on_click = lambda e: voltar(e))

    button4 = OutlinedButton(text = "Entrar", style=ButtonStyle(color="#000000"),on_click = lambda e: entrar(e))

    google = Image(src="google.png",height=15, width=15)

    face = Image(src="face.png",height=15, width=15)

    github = Image(src="github.png",height=15, width=15)

    i = Image(src="linkedin.png",height=15, width=15)
    
    r = Row([google, face, github, i], alignment=MainAxisAlignment.CENTER)

    cadastro = Row([

        Container(height = 490, width = 385, bgcolor = "#ffffff", padding=30,
                  border_radius = border_radius.only(top_right = 150, bottom_right = 150),
                  content = Column([t5, t9, button2
                                    
                                    ],alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER
                                    )
                  ), 
                

        Container(height = 490, width = 385, bgcolor = "#557dff", padding=30,
                  content = Column([t6, r, t7, m, e, s, button3
                                    
                                    ],alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER)
                  )
        
                
    ])

    lg = Row([

         Container(height = 490, width = 385, bgcolor = "#557dff", padding=30,
                  
                  content = Column([t, r, t3, e, s, t4, button4
                                    ],alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER)
                  ),
                  
                

        Container(height = 490, width = 385, bgcolor = "#ffffff", padding=30,border_radius = border_radius.only(top_left = 150, bottom_left= 150),
                  content = Column([t2, t8, button1
                                    ],alignment=MainAxisAlignment.CENTER, horizontal_alignment=CrossAxisAlignment.CENTER)
                  
                  )

    ])

   



    def entrar(e):
        cadastro.visible = True
        lg.visible = False
        page.update()

    def voltar(e):

        lg.visible = True
        cadastro.visible = False
        page.update()
    
    page.add(lg,cadastro)
app(target = main)
