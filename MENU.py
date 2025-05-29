opcao = 0
while opcao != 3:
    print(" 1- receber elogio \n 2- calcular o fatorial \n 3- sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("Você é uma pessoa muito inteligente!")
    elif opcao == 2:
        numero = int(input("Digite um número para calcular o fatorial: "))
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        print(f"O fatorial de {numero} é {fatorial}.")
    elif opcao == 3:
        print("Saindo do programa. Até logo!")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        print("Tente novamente.")
        continue
    # Opção de ajuda após cada ação principal
    print("Posso te ajudar com mais alguma coisa?")
    print("Digite 1 para sim ou 2 para não.")
    resposta = int(input("Digite sua resposta: "))
    if resposta == 1:
        print("Estou aqui para ajudar!")
        while True:
            print(" 1- Fazer contas de matemática   \n 2- voltar ao menu \n 3- sair")
            sub_opcao = int(input("Digite a opção desejada: "))
            if sub_opcao == 1:
                primeiro_valor = int(input("Por favor, informe o primeiro valor: "))
                segundo_valor = int(input("Por favor, informe o segundo valor: "))
                soma = primeiro_valor + segundo_valor
                print("A soma dos valores é " + str(soma))
                subtracao = primeiro_valor - segundo_valor
                print("A subtração dos valores é " + str(subtracao))
                if segundo_valor != 0:
                    divisao = primeiro_valor / segundo_valor
                    print("A divisão dos valores é " + str(divisao))
                else:
                    print("Não é possível dividir por zero.")
                multiplicacao = primeiro_valor * segundo_valor
                print("A multiplicação dos valores é " + str(multiplicacao))
            elif sub_opcao == 2:
                print("Voltando ao menu principal...")
                break
            elif sub_opcao == 3:
                print("Saindo do submenu.")
                exit()
            else:
                print("Opção inválida no submenu.")
    elif resposta == 2:
        print("Tudo bem, se precisar, estarei aqui!")
    else:
        print("Resposta inválida. Por favor, digite 1 ou 2.")
print("Obrigado por usar o programa!")
print("Volte sempre!")
print("Arthur Menezes. Vou conseguir! 2024")
# FIM DO PROGRAMA
