programa {
  
  //banco de informações
  inteiro bag  = 2 ,bcc = 16 ,bsn = 2022 , i
  caracter voltar
 real saldo= 1500 , limite= 3000 , total= limite + saldo , deposito 

   
   funcao vetor(){

    para(i=1; i<=1000; i++){


    }

    para(i=1; i<1000; i++){

      
    }


   }
   
   
   
   
   
   funcao inicio(){

    inteiro ag, cc , sn
  

    faca{
      escreva("    Bem-vindo ao Banco Senac \n")
    escreva("informe o número da agência: \n")
    leia(ag)
    escreva("informe o número da conta: \n")
    leia(cc)
    escreva("informe a senha: \n")
    leia(sn)
    limpa()
    }enquanto (bag != ag ou bcc != cc ou bsn != sn )


    menu()
  }





  funcao menu() { 

    inteiro op

    escreva("\n Escolha uma Operação Abaixo\n")
    escreva("\n 1 -Saldo | 2 -Extrato | 3 -Saque | 4 -Depósito | 5 -Sair \n")
    escreva("Opção:\n")
    leia(op)
    limpa()

    escolha(op){
      caso 1 :
       saldo()
      pare
       caso 2 :
       extrato()
      pare

       caso 3 :
       saque()
      pare

       caso 4 :
       deposito()
      pare

       caso 5 :
       sair()
      pare

      caso contrario: escreva("Opção Inválida, Tente Novamente")
    }


  }
    
   funcao saldo(){
   faca{
     escreva("\n Saldo: \n", saldo)
     escreva("\n Limite: \n", limite)
     escreva("\n Total: \n", total)
  escreva("\n Deseja Voltar ao Menu Principal s|n ?")
    leia(voltar)
  }
   enquanto(voltar != 's')
   menu()
   }
       funcao extrato(){
         faca{

     escreva("Deseja Volta ao Menu Pricipal s|n \n ")
     leia(voltar)

    }
   enquanto(voltar != 's')
   menu()
   }

    funcao saque(){
      faca{
        escreva("Qual Valor Deseja Sacar? \n")
        leia(deposito)
         escreva("------------------ \n\n")
         

        se(saldo){
     
          escreva("saldo indisponivel \n")
        }

      escreva("Deseja Voltar ao Menu Principal s|n ?")
      leia(voltar)

    }
   enquanto(voltar !='s')
   menu()
   }
  
    funcao deposito(){
      faca{

      escreva("qual valor deseja deposita?\n")
      leia(deposito)

      escreva("Deseja Voltar ao Menu Principal s|n ?")
      leia(voltar)
      escreva("---------------------\n\n")

    }
   enquanto(voltar != 's')
   menu()
   }
}
