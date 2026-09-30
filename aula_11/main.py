#idade = 20
#idade2 = 30
#nome = "sofiazinR6"
#nome2 = "joao"
#soma_idade = print(f"a soma de idade e {idade + idade2}")
#print(f"bom dia {nome} e {nome2}")

import random as rd

cardapio = {
     "chocolate": 5.00,
     "baunilha":4.50,
     "morango":3.00,
     "flocos":9.00,

}

brindes =["canudo","copo personalizado","gelo","badge"]

def mostrar_cardapio():
    print("__cardapio__")
    for sabor ,preco in cardapio.items():
        print(f"{sabor.title()}: R$ {preco:.2f}")

def fazer_pedido():
    total=0
    pedido=[]
    
    while True:
        sabor = input("\ndigite o sabor do sorvete que deseja:(digite 'sair'para sair)").lower()
        if sabor == "sair":
            break
        elif sabor in cardapio:
            total += cardapio[sabor]
            pedido.append(sabor)
            print(f"{sabor} adcionado ao pedido")
        else:
            print("sabor indisponivel")
    return pedido, total
    
mostrar_cardapio()
pedido, total = fazer_pedido()
print(f"\n Seu pedido :{pedido}")
print(f"total a pagar :R$ {total:.2f}")

if total >=15:
 random_brinde = rd.choice(brindes)
 print(f"parabens voce gannhou um brinde:{random_brinde}")






