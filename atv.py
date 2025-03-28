import os

os.system("cls || clear")  # Limpa a tela

# Inicializa as variáveis
total = 0  # Acumula o valor total do pedido
pedido = ""  # Armazena os pratos escolhidos como texto

# Menu de opções com os preços dos pratos
print("""
    ================= MENU =================
    1 | Picanha            | R$40,00
    2 | Filé a parmegiana  | R$38,00
    3 | Strogonoff         | R$25,00
    4 | Bife acebolado     | R$30,00
    5 | Lasanha            | R$15,00
    6 | Sushi              | R$20,00
    7 | Pão com ovo        | R$8,00
    0 | Finalizar pedido
""")

# Loop para fazer os pedidos
while True:
    escolha = int(input("Digite o código do prato ou 0 para finalizar o pedido: "))
    
    match escolha:
        case 1:
            prato = "Picanha"
            valor = 40
        case 2:
            prato = "Filé a parmegiana"
            valor = 38
        case 3:
            prato = "Strogonoff"
            valor = 25
        case 4:
            prato = "Bife acebolado"
            valor = 30
        case 5:
            prato = "Lasanha"
            valor = 15
        case 6:
            prato = "Sushi"
            valor = 20
        case 7:
            prato = "Pão com ovo"
            valor = 8
        case 0:
            break  # Encerra o pedido se o código for 0
        case _:
            print("Código inválido! Escolha um código de 1 a 7 ou 0 para finalizar.")
            continue
    
    # Acumula o valor total e adiciona o prato ao pedido
    pedido += f"{prato} - R${valor:.2f}\n"  # Adiciona prato ao pedido
    total += valor  # Acumula o valor total

# Exibe o pedido finalizado
print("\nSeu pedido finalizado:")
print(pedido)

# Exibe o subtotal (valor total sem acréscimo ou desconto)
print(f"Subtotal: R${total:.2f}")

# Solicita a forma de pagamento
while True:
    forma_pagamento = input("\nEscolha a forma de pagamento (à vista / cartão): ").strip().lower()

    match forma_pagamento:
        case "à vista":
            desconto = total * 0.1  # Calcula o desconto de 10%
            total_com_desconto = total - desconto
            print(f"Desconto de 10% aplicado. Valor do desconto: R${desconto:.2f}")
            print(f"Total com desconto: R${total_com_desconto:.2f}")
            break
        case "cartão":
            acrescimo = total * 0.1  # Calcula o acréscimo de 10%
            total_com_acrescimo = total + acrescimo
            print(f"Acréscimo de 10% aplicado. Valor do acréscimo: R${acrescimo:.2f}")
            print(f"Total com acréscimo: R${total_com_acrescimo:.2f}")
            break
        case _:
            print("Forma de pagamento inválida! Por favor, escolha 'à vista' ou 'cartão'.")
