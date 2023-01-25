import random

def jogar(): 
    print ("\n",32*"*", sep="")
    print ("Bem vindo ao jogo de Adivinhação")
    print (32*"*")

    numero_secreto = random.randrange(1,51)
    pontos = 1000

    nivel = int(input("Escolha o nível: 1-Fácil 2-Médio 3-Difícil: "))
    if nivel==1:
        total_tentativas = 25
    elif nivel==2:
        total_tentativas = 15
    elif nivel==3:
        total_tentativas = 5
    else:
        print("Nível inválido")
        total_tentativas = 0

    for rodada in range(1, total_tentativas+1): #último range é excludente. Aceita mais uma parâmetro, step
        print ("\nTentativa {} de {}.".format(rodada, total_tentativas)) #string interpolation
        entrada = input("Digite um número de 1 a 50: ") #type(chute) -> input sempre retorna str
        chute = int(entrada) #py não converte str em número automaticamente ("42" != 42)

        acertou =     chute == numero_secreto
        fora_range =  chute > 50 or chute < 1
        chute_maior = chute > numero_secreto

        if acertou: 
                print("\nVocê acertou! Sua pontuação foi {}".format(pontos)) 
                break #sai do laço
        else:
            if fora_range:
                print("\nO número deve estar entre 0 e 50!") #os blocos devem ser identados com 4 espaços (config tab)
                continue #pula para a próxima iteração
            elif chute_maior:
                print("\nSeu chute foi maior que o número secreto.")
            else:
                print("\nSeu chute foi menor que o número secreto.")
            
            pontos = pontos - abs(chute - numero_secreto) #numero absoluto

    print("\nFim do jogo", end=2*"\n") #sem identação, entende que o bloco acabou
