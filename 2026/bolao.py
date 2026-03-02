import time #framework de delay
pontos = 0 #pontos
print("bem vindo ao bolão da copa de 2022 grupo A")
####################     ROUND 1             ###########

def round1():
    global pontos # traz os pontos
    print("round 1, qual time ganhou na final? argentina ou frança?")
    print("1: frança | 2: argentina | 3: empate")
    result1 = input("escreve o número correto.")
    if result1 == '2': #se o resultado for
        print("você acertou! vamos para a round 2.")
        pontos += 1
    else:
        print("você errou resultado real: 2, vamos para a round 2.")
################            ROUND 2           ###############
def round2():
    time.sleep(1) # delay
    global pontos # traz os pontos
    print('round 2, quem ganhou no jogo grupo A: "catar ou equador"')
    result2 = input("1: Catar | 2: Equador | 3: empate")
    if result2 == '2': #se o resultado for
        pontos += 1
        print("Você ganhou! vamos para o round 3.")
    else:
        print(" você perdeu! a resposta é 2. vamos para o round 3.")
###########        ROUND 3         #####################
def round3():
    global pontos # traz os pontos
    time.sleep(1) # delay
    print("quem ganhou no jogo grupo A: holanda ou senegal?")
    result3 = input("1: senegal | 2: holanda | 3: empate")
    if result3 == '2': #se o resultado for
        pontos += 1
        print("Você ganhou! vamos para o round 4.")
    else:
        print("Você perdeu! a resposta é 2. vamos pro round 4.")
#############         ROUND 4            #############
def round4():
    global pontos # traz os pontos
    time.sleep(1)  #delay
    print('Quem ganhou no jogo do grupo A: "Catar ou senegal"?')
    result4 = input("1: Catar | 2: senegal | 3: empate")
    if result4 == '1': #se o resultado for
        pontos += 1
        print("Você ganhou, vamos para o round 5.")
    else:
        print("Você perdeu, a resposta é 1")
##############          ROUND 5          ############################
def round5():
    global pontos # traz os pontos
    time.sleep(1) #delay
    print('quem ganhou no jogo do grupo A: "Holanda ou equador"?')
    result5 = input("1: holanda | 2: equador | 3: empate")
    if result5 == "3": #se o resultado for 3
        pontos += 1
        print("você ganhou, vamos para o round 6")
    else:
        print("você perdeu, o a resposta é 3, vamos pro round 6")
###########        ROUND 6       ################################# 
def round6():
    global pontos # traz os pontos
    time.sleep(1) #delay
    print('quem ganhou no jogo do grupo A: "Holanda ou Catar"?')
    result6 = input("1: equador | 2: holanda | 3: empate")
    if result6 == '2': #se result é 2
        pontos += 1 #soma os pontos
        print("acertou")
    else:
        print('errou! o resultado certo é 2')
############ROUND 7##############
def round7():
    global pontos # traz os pontos
    time.sleep(1) #delay
    print('quem ganhou no jogo do grupo A: " equador e senegal"?')
    result7 = input("1: senegal | 2: equador | 3: empate") 
    if result7 == '1': #se resultado for 1
        pontos += 1 #somar 1
        print("acertou, você zerou o jogo!")
        print("pontos acumulados: ", pontos)
    else: # se errar
        print("você errou, a resposta correta era 1.")
        print("pontos acumulados: ", pontos)

#executa as functions e faz delay
time.sleep(1)
round1()
print("")
time.sleep(1)
round2()
print("")
time.sleep(1)
round3()
print("")
time.sleep(1)
round4()
print("")
time.sleep(1)
round5()
print("")
time.sleep(1)
round6()
print("")
time.sleep(1)
round7()

#resultados:

#round1: 2
#round2: 2
#round3: 2
#round4: 1
#round5: 3
#round6: 2
#round7: 1