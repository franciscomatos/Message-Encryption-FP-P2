#2.1 tipo posicao

def faz_pos(l,c): #recebe dois numeros e devolve uma posicao
    if isinstance(l,int) and isinstance(c,int):
        if l>=0 and c>=0:
            return (l,c)
        else:
            raise ValueError ('faz_pos: argumentos errados')
    else:
        raise ValueError ('faz_pos: argumentos errados')
    
def linha_pos(p): #recebe uma posicao e devolve o numero correspondente a linha da posicao
    return p[0]

def coluna_pos(p): #recebe uma posicao e devolve o numero correspondente a coluna da posicao
    return p[1]

def e_pos(arg): #recebe um argumento e devolve True se este corresponder a uma posicao ou False caso contrario
    if isinstance(arg,tuple):
        if len(arg)==2 and isinstance(arg[0],int) and isinstance(arg[1],int):
            if arg[0]>=0 and arg[1]>=0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def pos_iguais(p1,p2): #recebe duas posicoes e devolve True caso estas sejam iguais ou False caso contrario 
    if linha_pos(p1)==linha_pos(p2) and coluna_pos(p1)==coluna_pos(p2):
        return True
    else:
        return False
    
#2.2 tipo chave
  
def gera_chave_linhas(l,mgc): #a representacao interna da chave sera uma lista de listas: [[linha1],[linha2],[linha3],[linha4],linha[5]]
    letras_l=[] 
    chave=[] 
    conjunto_letras=('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    conjunto_letras_espaco=('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ')
    for letra in l:
        if letra not in conjunto_letras:
            raise ValueError ('gera_chave_linhas: argumentos errados')
    if isinstance(l,tuple) and len(l)==25:
            for i in range(0,len(l)):
                for j in range(i+1,len(l)):
                    if l[i]==l[j]: 
                        raise ValueError ('gera_chave_linhas: argumentos errados')
            for letra in l:
                if letra in mgc:
                    letras_l=letras_l 
                else:
                    letras_l=letras_l+[letra,] 
            for caracter in mgc:
                if isinstance(mgc,str) and caracter in conjunto_letras_espaco:
                    if caracter not in chave and caracter in l: 
                        chave=chave+[caracter,]
                    else:
                        chave=chave 
                else:
                    raise ValueError('gera_chave_linhas: argumentos errados') 
    else:
        raise ValueError('gera_chave_linhas: argumentos errados')
    chave=chave+letras_l #chave composta pelas letras de mgc nao repetidas e pelas letras de l que nao estao em mgc    
    return [chave[0:5],chave[5:10],chave[10:15],chave[15:20],chave[20:25]] #organiza uma lista de 5 listas correspondentes a cada linha da tabela


def gera_chave_espiral(l,mgc,s,pos): #a representacao interna da chave sera uma lista de listas: [[linha1],[linha2],[linha3],[linha4],linha[5]]
    letras_l=[] 
    chave=[] 
    conjunto_letras=('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    conjunto_letras_espaco=('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ')
    letras_repetidas=()
    for letra in l:
        if letra not in conjunto_letras:
            raise ValueError ('gera_chave_espiral: argumentos errados')
        elif letra in conjunto_letras and letra not in letras_repetidas:
            letras_repetidas=letras_repetidas+(letra,)
        else:
            raise ValueError ('gera_chave_espiral: argumentos errados')      
    if isinstance(l,tuple) and len(l)==25:
            for letra in l:
                if letra in mgc:
                    letras_l=letras_l 
                else:
                    letras_l=letras_l+[letra,] 
            for caracter in mgc:
                if isinstance(mgc,str) and caracter in conjunto_letras_espaco:
                    if caracter not in chave and caracter in l: 
                        chave=chave+[caracter,]
                    else:
                        chave=chave 
                else:
                    raise ValueError('gera_chave_espiral: argumentos errados') 
    else:
        raise ValueError('gera_chave_espiral: argumentos errados')
    chave=chave+letras_l #chave composta pelas letras de mgc nao repetidas e pelas letras de l que nao estao em mgc      
    if isinstance(s,str) and s in ('c','r'):
        if e_pos(pos) == True:
            if s=='r':
                if pos==(0,0):
                    return [chave[0:5],chave[15:19]+[chave[5],],[chave[14],]+chave[23:25]+[chave[19],]+[chave[6],],[chave[13],]+[chave[22],]+[chave[21],]+[chave[20],]+[chave[7],],[chave[12],]+[chave[11],]+[chave[10],]+[chave[9],]+[chave[8],]]
                elif pos==(0,4):
                    return [chave[12:16]+[chave[0],],[chave[11],]+chave[22:24]+[chave[16],]+[chave[1],],[chave[10],]+[chave[21],]+[chave[24],]+[chave[17],]+[chave[2],],[chave[9],]+[chave[20],]+[chave[19],]+[chave[18],]+[chave[3],],[chave[8],]+[chave[7],]+[chave[6],]+[chave[5],]+[chave[4],]]
                elif pos==(4,4):
                    return [chave[8:13],[chave[7],]+chave[20:23]+[chave[13],],[chave[6],]+[chave[19],]+[chave[24],]+[chave[23],]+[chave[14],],[chave[5],]+[chave[18],]+[chave[17],]+[chave[16],]+[chave[15],],[chave[4],]+[chave[3],]+[chave[2],]+[chave[1],]+[chave[0],]]
                else:
                    return [chave[4:9],[chave[3],]+chave[18:21]+[chave[9],],[chave[2],]+[chave[17],]+[chave[24],]+[chave[21],]+[chave[10],],[chave[1],]+[chave[16],]+[chave[23],]+[chave[22],]+[chave[11],],[chave[0],]+[chave[15],]+[chave[14],]+[chave[13],]+[chave[12],]]
            
            else:
                if pos==(0,0):
                    return [[chave[0],]+[chave[15],]+[chave[14],]+[chave[13],]+[chave[12],],[chave[1],]+[chave[16],]+[chave[23],]+[chave[22],]+[chave[11],],[chave[2],]+[chave[17],]+[chave[24],]+[chave[21],]+[chave[10],],[chave[3],]+chave[18:21]+[chave[9],],chave[4:9]]
                elif pos==(4,0):
                    return [[chave[12],]+[chave[11],]+[chave[10],]+[chave[9],]+[chave[8],],[chave[13],]+[chave[22],]+[chave[21],]+[chave[20],]+[chave[7],],[chave[14],]+chave[23:25]+[chave[19],]+[chave[6],],chave[15:19]+[chave[5],],chave[0:5]]
                elif pos==(4,4):
                    return [[chave[8],]+[chave[7],]+[chave[6],]+[chave[5],]+[chave[4],],[chave[9],]+[chave[20],]+[chave[19],]+[chave[18],]+[chave[3],],[chave[10],]+[chave[21],]+[chave[24],]+[chave[17],]+[chave[2],],[chave[11],]+chave[22:24]+[chave[16],]+[chave[1],],chave[12:16]+[chave[0],]]
                else: 
                    return [[chave[4],]+[chave[3],]+[chave[2],]+[chave[1],]+[chave[0],],[chave[5],]+[chave[18],]+[chave[17],]+[chave[16],]+[chave[15],],[chave[6],]+[chave[19],]+[chave[24],]+[chave[23],]+[chave[14],],[chave[7],]+chave[20:23]+[chave[13],],chave[8:13]]
        else:
            raise ValueError ('gera_chave_espiral: argumentos errados')
    else:
        raise ValueError ('gera_chave_espiral: argumentos errados')
        
def ref_chave(c,p): #recebe uma chave e uma posicao e devolve a letra correspondente 
    return c[linha_pos(p)][coluna_pos(p)]

def muda_chave(c,p,l): #devolve uma chave alterada de acordo com a letra e posicao recebidas
    c[linha_pos(p)][coluna_pos(p)]=l
    return c


def e_chave(arg): #recebe um argumento e devolve True se este for do tipo chave e False caso contrario
    conjunto_letras=('A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    letras=()
    if isinstance(arg,list) and len(arg)==5:
        for linha in arg:
            if isinstance(linha,list) and len(linha)==5:
                for elemento in linha:
                    if isinstance(elemento,str) and elemento in conjunto_letras:
                        if elemento not in letras:
                            letras=letras+(elemento,)
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        return True
    else:
        return False
                
            
def string_chave(c): #recebe uma chave e devolve as letras dessa chave dispostas numa matriz quadrada 5x5
    chave=''
    for linha in range(0,5):
        for coluna in range(0,5):
            chave=chave+str(c[linha][coluna])+' '
    return chave[0:10]+'\n'+chave[10:20]+'\n'+chave[20:30]+'\n'+chave[30:40]+'\n'+chave[40:50]+'\n'

#4 funcoes a desenvolver

def digramas(mens): #recebe uma cadeia de caracteres e devolve os digramas correspondentes a essa cadeia
    digrama=''
    for letra in mens:
        if letra != ' ':
            digrama=digrama+letra #cadeia de caracteres recebida sem os espacos vazios
    digrama2=list(digrama)
    letra1=0
    while letra1 <= len(digrama2)-2:
        letra2=letra1+1
        if digrama2[letra1]!=digrama2[letra2]:
            digrama2=digrama2
        else: 
            digrama2[letra1]=digrama2[letra1]+'X' #verifica se duas letras seguidas sao iguais
        letra1=letra1+2
    digrama3=''
    for letra3 in range(0,len(digrama2)):
        digrama3=digrama3+str(digrama2[letra3])
    if len(digrama3)%2!=0:
        digrama3=digrama3+'X' #verifica se o conjunto de digramas corresponde a um numero par de caracteres
    else:
        digrama3=digrama3
    return digrama3


def figura(digrm,chave): #recebe um digrama e uma chave e devolve a figura correspondente as posicoes do digrama nessa chave
    for linha in range(0,5):
        for coluna in range(0,5):
            if digrm[0] == chave[linha][coluna]:
                posicao_letra1=(linha,coluna) 
    for linha in range(0,5):
        for coluna in range(0,5):
            if digrm[1] == chave[linha][coluna]:
                posicao_letra2=(linha,coluna)
    if linha_pos(posicao_letra1)==linha_pos(posicao_letra2):
        fig=('l')
    elif coluna_pos(posicao_letra1)==coluna_pos(posicao_letra2):
        fig=('c')
    else:
        fig=('r')
    return (fig,posicao_letra1,posicao_letra2)


def codifica_l(pos1,pos2,inc):
    return (muda_posicao_linha(pos1,inc),muda_posicao_linha(pos2,inc))

def muda_posicao_linha(pos,inc): #funcao auxiliar que permite codificar ou descodificar um digrama cujos caracteres estejam na mesma linha de uma chave
    if inc==1:
        if coluna_pos(pos)<4:
            pos=(linha_pos(pos),coluna_pos(pos)+1)
        else:
            pos=(linha_pos(pos),0)
    else:
        if coluna_pos(pos)>0:
            pos=(linha_pos(pos),coluna_pos(pos)-1)
        else:
            pos=(linha_pos(pos),4)
    return pos


def codifica_c(pos1,pos2,inc):
    return (muda_posicao_coluna(pos1,inc),muda_posicao_coluna(pos2,inc))

def muda_posicao_coluna(pos,inc): #funcao auxiliar que permite codificar ou descodificar um digrama cujos caracteres estejam na mesma coluna de uma chave 
    if inc==1:
        if linha_pos(pos)<4:
            pos=(linha_pos(pos)+1,coluna_pos(pos))
        else:
            pos=(0,coluna_pos(pos))
    else:
        if linha_pos(pos)>0:
            pos=(linha_pos(pos)-1,coluna_pos(pos))
        else:
            pos=(4,coluna_pos(pos))
    return pos


def codifica_r(pos1,pos2): #codifica ou descodifica um digrama cujos caracteres encontram-se em linhas e colunas diferentes de uma chave
    nova_pos1=(linha_pos(pos1),coluna_pos(pos2))
    nova_pos2=(linha_pos(pos2),coluna_pos(pos1))
    return (nova_pos1,nova_pos2)


def codifica_digrama(digrm,chave,inc): #codifica ou descodifica um digrama independentemente das linhas e colunas correspondentes aos caracteres
    for linha in range(0,5):
        for coluna in range(0,5):
            if digrm[0] == chave[linha][coluna]:
                pos_letra1=(linha,coluna)
    for linha2 in range(0,5):
        for coluna2 in range(0,5):
            if digrm[1] == chave[linha2][coluna2]:
                pos_letra2=(linha2,coluna2)  
    if linha_pos(pos_letra1)==linha_pos(pos_letra2):
        novas_pos=codifica_l(pos_letra1,pos_letra2,inc)
    elif coluna_pos(pos_letra1)==coluna_pos(pos_letra2):
        novas_pos=codifica_c(pos_letra1,pos_letra2,inc)
    else:
        novas_pos=codifica_r(pos_letra1,pos_letra2)
    return ref_chave(chave,novas_pos[0])+ref_chave(chave,novas_pos[1])
        

def codifica(mens,chave,inc): #codifica ou descodifica uma mensagem de acordo com uma chave dada
    mensagem=digramas(mens)
    mensagem_final=''
    letra=0
    while letra<len(mensagem)-1:
        letra1=letra
        letra2=letra+1
        digrama=mensagem[letra1]+mensagem[letra2]
        digrama_final=codifica_digrama(digrama,chave,inc)
        mensagem_final=mensagem_final+digrama_final
        letra=letra+2
    return mensagem_final
    