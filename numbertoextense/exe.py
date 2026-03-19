import time
#EXD = extenso dezena
#EXC = extenso centena
#EXU = extenso unidade
#DEU = dezenas e unidades agrupados
#cf = centena final
# df = dezena final
#uf = unidade final
#FN = final number
# criador do numero final | cria o numero final
# cemrule | alterna entre cem e cento
#eleven rule | faz os numeros entre 10 e 20 (desenove, dezoito etc)
# E RULE DO DEU | TIRA OS "E" da dezena e unidade juntos 
# EDEUCF RULE | é E RULE para o DEU e o CF
print("os números devem ser feitos com 0, por exemplo: 021 ao invés de 21") #aviso
time.sleep(1)
print("")
numero = input("escreve o número") #input
c = numero[-3] #separa centena
d = numero[-2] #separa dezena
u = numero[-1] #separa unidade
replace1 = "0" #variavel pro nada
null = ""
EXC = { # extenso centenas
    "0": "",
    "1": "Cem",
    "2": "duzentos",
    "3": "trezentos",
    "4": "quatrocentos",
    "5": "quinhentos",
    "6": "seicentos",
    "7": "setecentos",
    "8": "oitocentos",
    "9": "novecentos",
}
cf = EXC[c] #centena final é a centena na EXC
    
EXD = { #extenso dezenas
    "0": "",
    "1":"dez",
    "2":"vinte",
    "3":"trinta",
    "4":"quarenta",
    "5":"cinquenta",
    "6":"sessenta",
    "7":"setenta",
    "8":"oitenta",
    "9":"noventa"
}
df = EXD[d] # dezena final é a dezena na EXD
# cria as unidades
EXU = { #extenso unidades
    "0": "",
    "1":"um",
    "2":"dois",
    "3":"tres",
    "4":"quatro",
    "5":"cinco",
    "6":"seis",
    "7":"sete",
    "8":"oito",
    "9":"nove"
}
uf = EXU[u] # unidade final é a unidade no EXU

DEU = df + " e " + uf
####### QUEDA DOS NUMEROS ###########
    
if c == "1" and d == "0" and u == "0": # se centena for 1 e dezena e unidade for zero
    cf = "cem" #vira cem
elif c == "1": # se c for 1 e os outros nao forem zero
    cf = "cento" #centena final vira cento

######### QUEDA DO CEMRULE ############

if d == "0" and u == "0": # se dezena e unidade for 0
    DEU = DEU.replace(" e ", " ") #tira o " e " do unidade e dezena agrupados.
    
if d == "1" and u == "8": # se dezena for 1 e u for 8
    DEU = "dezoito" # dezena e unidade vira dezoito
    
if d == "1" and u == "1": # se dezena e unidade for 1
    df = "on" # manipula a dezena
    uf = "ze"  # manipula a unidade
    
    DEU = df + uf # tira o e, vira dezena com unidade crus
    
if d == "1" and u == "2": # bse dezena for 1 e unidade for 2
    df = "do" #manipula a dezena
    uf = "ze" #manipula a unidade
    DEU = df + uf # tira o e, vira dezena com unidade crus
    
if d == "1" and u == "3": # se dezena for 1 e unidade for 3
    df = "tre" #manipula dezena
    uf = "ze" #manipula unidade
    DEU = df + uf #tira o e , vira dezena e unidade crus.
    
if d == "1" and u == "4": # se for cartoze
    df = "carto" #manipula dezena
    uf = "ze" #manipula unidade
    DEU = df + uf #tira o " e ", vira dezena e unidade crus
    
if d == "1" and u == "5": # se for quinze
    df = "qui" #manipula dezena
    uf = "ze" #manipula unidade
    DEU = df + uf #vira dezena e unidade crus
    
######## QUEDA DO ELEVENRULE    ############

if uf == EXU[replace1]:    #se uf for zero
    DEU = df        # deu vira dezena crua
elif df == EXD[replace1]: # Se df for zero
    DEU = uf     # DEU vira unidade crua
    
###### QUEDA DO E RULE DO DEU #############

FN = cf + " e " + DEU #cria o número final

############# QUEDA DO CRIADOR DO NUMERO FINAL#####

if DEU == null: # se Dezena e unidade for nada
    FN = cf  # final number vira centena crua
    
if cf == null: # SE CENTENA FINAL FOR NADA
    FN = DEU # FINAL NUMBER VIRA Dezena e unidade

######### QUEDA DO EDEUCF RULE ######### 

if FN == "dez e nove":
    FN = "desenove"
print(FN)
