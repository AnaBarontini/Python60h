cardapio = ("agua", "batata frita", "hot-dog", "misto quente", "refri", "suco", "x-burguer", "x-salada", "x-bacon", "sundae")
Pedido = []
'''
Pedido.append(cardapio[2])
Pedido.append(cardapio[4])
Pedido.append(cardapio[6])
Pedido.append(cardapio[1])
Pedido.append(cardapio[9])
print("Cardapio:", cardapio)
print("pedido:" Pedido)
'''
Pedido.append(cardapio[int(input("Informe a opção:"))-1])
Pedido.append(cardapio[int(input("Informe a opção:"))-1])
Pedido.append(cardapio[int(input("Informe a opção:"))-1])
Pedido.append(cardapio[int(input("Informe a opção:"))-1])
Pedido.append(cardapio[int(input("Informe a opção:"))-1])
print("Produtos escolhidos no cardápio:", Pedido)
