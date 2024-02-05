"""

    - O tabuleiro é uma grade 3x3.
    - Dois jogadores, 'X' e 'O', jogam alternadamente.
    - Cada jogador pode escolher uma célula vazia e colocar seu marcador ('X' ou 'O') nela.
    - O jogo continua até que um dos jogadores vença ou o tabuleiro esteja cheio (empate).
    - Um jogador vence se conseguir três de seus marcadores em linha (horizontal, vertical ou diagonal).

"""
# tabuleiro trabalhado com matrizes
"""
tabuleiro = [0,0,0]
while True:
    print("Sejam bem-vindo ao jogo da velha PYTHON!")
    print("1- comeca o jogo")
    print("2- regras do jogo")
    print("3- sair do jogo")
    escolha_introducao = int(input(">:"))
    match escolha_introducao:
        case 1:
                print("Para comecarmos o jogo, escolha qual jogador deseja ser!")
                print("1 - jogador X / 2 - jogador O")
                escolha_jogador = int(input(">:"))
                if escolha_jogador == 1:
                        print("")
                        print("Abaixo tera o tabuleiro!")
                        print(tabuleiro)
                        print(tabuleiro)
                        print(tabuleiro)
                        print("Voce tem que escolher a fileira e qual numero deseja jogar!")
                        print("")
                        
                        print("Para comecar escolhe qual linha voce deseja jogar! ")
                        posicao_linha = int(input(""))
                        print("Qual coluna voce deseja jogar")
                        posicao_coluna = str(input(""))
                        def jogo_posicoes(posicao_coluna,posicao_linha):
                              return print("teste")
                        
                        #se a posicao for 1 e a letra for a b ou c 
                                #tabuleiro altere posicao da primeira coluna
                        #se a posicao for 2 e a letra for a b ou c
                                #tabuleiro altere a posicao da segunda coluna
                        #se a posicao for 3 e a letra for a b ou c
                                #tabuleiro altere a posicao da segunda coluna
                        break 
                else:
                    escolha_jogador2 = 1    
        case 2:
                print("Dois jogadores, 'X' e 'O', jogam alternadamente.")
                ("Cada jogador pode escolher uma célula vazia e colocar seu marcador ('X' ou 'O') nela.")
                print("O jogo continua até que um dos jogadores vença ou o tabuleiro esteja cheio (empate)")
                print("Um jogador vence se conseguir três de seus marcadores em linha (horizontal, vertical ou diagonal).")
                print("Se deseja retornar aperte enter!")
                input(">:")
        case 3:
                print("Obrigado por ter entrado no jogo!")
                break
"""