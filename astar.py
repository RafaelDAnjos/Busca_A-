

"""
Algoritmo A* implementação

Laribirinto pelo qual o agente será submetido.
"""
labirinto = []
arq =  open("labirinto.txt","r")
linha = arq.readline()
while linha != "":
    linha = linha.split(" ")
    labirinto.append(linha)

    linha = arq.readline()





partida = [0,0]


chegada = [len(labirinto)-1,len(labirinto[0])-1]



custo = 1



heuristica = [[9,8,7,6,5,4],
              [8,7,6,5,4,3],
              [7,6,5,4,3,2],
              [6,5,4,3,2,1],
              [5,4,3,2,1,0]]

delta = [[-1,0],  #pra cima
        [0,-1],  #pra esquerda
        [1,0],   #pra baixo
        [0,1]]   #pra direita


aberta = []


def busca():


   aberta.append(partida)



   while aberta[len(aberta)-1][0] != chegada[0] or aberta[len(aberta)-1][1] != chegada[1]:
       expande = []

       for i in range(len(delta)):
          xlab = aberta[len(aberta)-1][0]+delta[i][0]
          ylab = aberta[len(aberta)-1][1]+delta[i][1]


          if xlab>=0 and xlab<len(labirinto) and ylab>=0 and ylab<len(labirinto[0])and [xlab,ylab] not in aberta:
             if labirinto[xlab][ylab] != 1:
                expande.append([xlab,ylab])
       if expande != []:
           melhor_no = bestno(expande)

           aberta.append(melhor_no)

       else:

          print("Não existe nó para ir")
          break
   for i in aberta:
       print(i)
   return 0

def bestno(expande):
   menorc = custo+heuristica[expande[0][0]][expande[0][1]]
   caminho = [expande[0][0],expande[0][1]]

   for i in expande[1:]:
       if menorc > (custo+heuristica[i[0]][i[1]]) :
           menorc = custo+heuristica[i[0]][i[1]]
           caminho = i



   return caminho

busca()









