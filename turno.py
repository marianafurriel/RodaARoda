import roleta
def turno(pontos):
    jogador = 0
    while(jogador<3):
        pontuacao = roleta.giraRoleta()
        if pontuacao == 'Passa a vez':
            jogador +=1
        elif pontuacao =='Perdeu tudo':
            pontos[jogador]=0
        else:
            pontos[jogador] = pontuacao
        

