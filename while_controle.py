jogando = True

while jogando:
    resposta = input("Quer continuar jogando? (sim/não): ").lower()
    if resposta == "não":
        jogando = False
        print("Você saiu do jogo.")
    elif resposta == "sim":
        print("O jogo continua!")
    else:
        print("Resposta inválida. Tente novamente.")