#NOME
#PESO
#ALTURA
#IDADE
#TEM PESO MINIMO PRA DOAR
#TEM IDADE MINIMA PRA DOAR
print("Cadastro de doador de sangue")
try:
    nome = input("Digite o nome do doador: ")
    peso = float(input("Digite o peso do doador kg: "))
    altura = int(input("Digite a altura do doador em cm: "))
    ano_de_nascimento = int(input("Digite o ano de nascimento do doador: "))
    idade = 2025 - ano_de_nascimento

    tem_peso_minimo = peso >= 50
    tem_idade_minima = idade >= 16

    texto_saida = (
        f"O doador {nome} tem {idade} anos.\n"
        f"Pesa {peso} kg.\n"
        f"Mede {altura} cm.\n"
    )
    if tem_peso_minimo and tem_idade_minima:
        texto_saida += "Ele pode doar sangue.\n"
    else:
        texto_saida += "Ele NÃO pode doar sangue.\n"

    print(texto_saida)
except ValueError:
    print("Erro: Por favor, digite apenas números válidos para peso, altura e ano de nascimento.")
# FIM DO PROGRAMA


