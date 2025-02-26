import pygame as p
import random 

#codigo para inicializar função
p.init()

PRETO = (0,0,0)
BRANCO = (255,255,255)
VERDE = (0,255,0)
VERMELHO = (255,0,0)
AZUL = (0,0,255)


#variavel criada para tamanho da tela
altura = 400
largura = 600


#codigo para criar tela 
#(tela)criada para maniculação
tela = p.display.set_mode ((largura,altura))
titulo = p.display.set_caption('Snake')


#definição do tamanho da cobra
TAMANHO_COBRA = 20

clock = p.time.Clock()

#codigo para aplicar cor na janela

def desenhar(cobra):
   for segmento in cobra :
    p.draw.rect(tela,VERDE,[segmento[0],segmento[1],TAMANHO_COBRA,TAMANHO_COBRA])

def jogo():

   x_cobra = largura // 2
   y_cobra = altura // 2
   movimento_x = 0
   movimento_y = 0
   cobra = []
   comprimento_cobra = 1

   comida_x = random.randrange(0,largura - TAMANHO_COBRA,TAMANHO_COBRA)
   comida_y  = random.randrange(0,altura - TAMANHO_COBRA,TAMANHO_COBRA)

   fim_de_jogo =False
   while not fim_de_jogo:
         for evento in p.event.get():
            if evento.type == p.QUIT:
               fim_de_jogo = True
            if evento.type == p.KEYDOWN:
               if evento.key == p.K_LEFT:
                  movimento_x = -TAMANHO_COBRA
                  movimento_y = 0
               elif evento.key == p.K_RIGHT:
                  movimento_x = TAMANHO_COBRA
                  movimento_y = 0
               elif evento.key == p.K_UP:
                  movimento_y = -TAMANHO_COBRA
                  movimento_x = 0
               elif  evento.key == p.K_DOWN:
                  movimento_y = TAMANHO_COBRA
                  movimento_x = 0

         if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
                        fim_de_jogo = True

         x_cobra += movimento_x
         y_cobra += movimento_y


         cabeça_cobra = []
         cabeça_cobra.append(x_cobra)
         cabeça_cobra.append(y_cobra)
         cobra.append(cabeça_cobra)

         if len(cobra) > comprimento_cobra:
                  del cobra [0]

               #verifica se a cobra colidiu com ela mesma
         for segmento in cobra [:-1]:
            if segmento == cabeça_cobra:
               fim_de_jogo = True


         tela.fill(PRETO)
         desenhar(cobra)
         p.draw.rect(tela,VERMELHO,[comida_x,comida_y,TAMANHO_COBRA,TAMANHO_COBRA])

         if x_cobra == comida_x and y_cobra == comida_y:
               comida_x = random.randrange(0,largura - TAMANHO_COBRA,TAMANHO_COBRA)
               comida_y = random.randrange(0,altura - TAMANHO_COBRA,TAMANHO_COBRA)
               comprimento_cobra += 1

         p.display.update()
         clock.tick(15)
   
   fonte = p.font.SysFont(None,55)
   texto_fim = fonte.render("Fim de Jogo!",True,AZUL)
   tela.blit(texto_fim,[largura // 3, altura // 3])
   p.display.update()
   p.time.wait(2000)
   p.quit()

jogo()
