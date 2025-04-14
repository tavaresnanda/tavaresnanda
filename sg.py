inicio = ft.Container (width=965,height=620,padding=20,
                           content= ft.Text("Sair")),
    
    alunos = ft.Container (bgcolor="#ffffff",width=965,height=620,padding=20,
                           content= ft.DataTable(columns=[
                               ft.DataColumn(ft.Text("Nome")),
                               ft.DataColumn(ft.Text("Matriculas")),
                               ft.DataColumn(ft.Text("Turmas")),
                               ft.DataColumn(ft.Text("Ações"))
                           ])),
    
    responsavel = ft.Container (bgcolor="#ffffff",width=965,height=620,padding=20),

    finaceiro = ft.Container (bgcolor="#ffffff",width=965,height=620,padding=20),

    turmas = ft.Container (bgcolor="#ffffff",width=965,height=620,padding=20),

    disciplinas = ft.Container (bgcolor="#ffffff",width=965,height=620,padding=20),
    

    def ini(e:ft.ControlEvent):
       page.remove(ini)
       page.add() 


    def sair (e):
        page.window_close()
        page.update()

                                                                                                                         
    page.add(ft.Row([c1,alunos]))
