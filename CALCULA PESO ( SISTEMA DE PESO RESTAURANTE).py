print("RESTAURANTE ARTHUR")
try:
    preco_por_quilo = 18.90  # Preço fixo por quilo
    print(f"Preço por quilo: R$ {preco_por_quilo:.2f}")
    peso = float(input("Digite o peso da comida: "))
    if preco_por_quilo < 0 or peso < 0:
        print("Erro: O preço e o peso devem ser valores positivos.")
    else:
        preco_total = preco_por_quilo * peso
        if peso > 1:
            print("Como o peso do prato do cliente é maior que 1kg, será cobrada uma taxa de 10% sobre o valor total.")
            taxa = preco_total * 0.10
            preco_total += taxa
            print(f"Preço total com taxa: R$ {preco_total:.2f}")
        else:
            print(f"Preço total: R$ {preco_total:.2f}")
            print("O peso do prato é menor ou igual a 1kg, portanto não há taxa adicional.")
        print("Obrigado pela preferência!")
except ValueError:
    print("Erro: Digite apenas números válidos para o peso.")
# FIM DO PROGRAMA