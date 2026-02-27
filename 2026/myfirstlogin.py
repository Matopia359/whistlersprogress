nomes = ['João bastos', 'Paulo Silva', 'Ricardo da silva'] #nomes registrados
comando = input("seleciona um comando")
if comando == "logar": #se o comando feito for o de logar
    NS = input("seu nome abaixo (funciona apenas com usuários registrados)") #input de colocar nome
    def logar(): #função de logar
        print("logou no sistema!") 
    if NS in nomes: #se tiver o value do NS em nomes:
        logar() #chama a função logar
    else:
        print("") #faz nada 
elif comando == "registrar": #se o comando é o de registrar
    NPA = input("Escreve teu nome para registrar") 
    if NPA != "": # se NPA não for nada
        nomes.append(NPA) #coloca um novo usuário
        print("Registraste!")
elif comando == "Excluirconta": # se o comando for o de excluir
    UPR = input("qual usuario desejas excluir?")
    if UPR in nomes: 
       nomes.remove(UPR) #remove o usuário
       print("usuarios agora:", nomes)
