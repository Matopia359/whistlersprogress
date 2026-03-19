import time
#EXD = extenso dezena
#EXC = extenso centena
#EXU = extenso unidade
#DEU = dezenas e unidades agrupados
#cf = centena final
print("os números devem ser feitos com 0, por exemplo: 021 ao invés de 21")
time.sleep(1)
print("")
numero = input("escreve o número") #input
c = numero[-3] #separa centena
d = numero[-2] #separa dezena
u = numero[-1] #separa unidade
replace1 = "0"
null = ""
EXC = {
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
    
EXD = {
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
EXU = {
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
    
if c == "1" and d == "0" and u == "0":
    cf = "cem"
elif c == "1":
    cf = "cento"

######### QUEDA DO CEMRULE ############

if d == "0" and u == "0":
    DEU = DEU.replace(" e ", " ")
    
if d == "1" and u != "0":
    df = "dese"

if d == "1" and u == "8":
    df = "dez"
    DEU = "dezoito"
    
if d == "1" and u == "1":
    df = "on"
    uf = "ze"  
    DEU = df + uf
    
if d == "1" and u == "2":
    df = "do"
    uf = "ze"
    DEU = df + uf
    
if d == "1" and u == "3":
    df = "tre"
    uf = "ze"
    DEU = df + uf
    
if d == "1" and u == "4":
    df = "carto"
    uf = "ze"
    DEU = df + uf
    
if d == "1" and u == "5":
    df = "qui"
    uf = "ze"
    DEU = df + uf
########  queda do cemrule    ############

if uf == EXU[replace1]:#se uf for zero
    DEU = df
elif df == EXD[replace1]: # Se df for zero
    DEU = uf
###### QUEDA DO E RULE DO DEU

FN = cf + " e " + DEU #cria o número final

############# QUEDA DO CRIADOR DO NUMERO FINAL#####
if DEU == null:
    FN = cf 
if cf == null:
    FN = DEU
if FN == "dez e nove":
    FN = "desenove"
print(FN)
