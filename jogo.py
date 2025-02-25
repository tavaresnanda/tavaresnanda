def jogo():

    x_cobra = largura // 2
    y_cobra = altura // 2
    movimento_x = 0
    movimento_y = 0
    cobra = []
    comprimento_cobra = 1

    comida_x = random.randrange(0,largura - tamanho_cobra,tamanho_cobra)
    comida_Y  = random.randrange(0,altura - tamanho_cobra,tamanho_cobra)

    fim_de_jogo =False
    while not fim_de_jogo:
       for evento in p.event.get():
          if evento.type == p.QUIT:
             fim_de_jogo = True
          if evento.type == p.KEYDOWN:
            if evento.key == p.K_LEFT:
               movimento_x = -tamanho_cobra
               movimento_y = 0
            elif evento.key == p.K_RIGHT:
               movimento_x = tamanho_cobra
               movimento_y = 0
            elif evento.key == p.K_UP:
               movimento_x = -tamanho_cobra
               movimento_y = 0
            elif  evento.key == p.K_DOWN:
               movimento_y = tamanho_cobra
               movimento_x = 0

    cabeça_cobra = []
    cabeça_cobra.append(x_cobra)
    cabeça_cobra.append(y_cobra)
    cobra.append(cabeça_cobra)

    if len(cobra) > comprimento_cobra:
       del cobra [0]

    #verifica se a cobr colidiu com ela mesma
    for segmento in cobra[:-1]:
       if segmento == cabeça_cobra:
          fim_de_jogo = True
