num=int(input("Informe o numero da sua tabuada:"))
for n in range(1,11):
    print(f"{n}x{num}={n*num}")
print("fim da tabuada do",num)

num2=int(input("informe o numero da tabuada 2:"))
i=1
while(i<=10):
    print(f"{i}x{num2}={i*num2}")
    i+=1
print("fim da segunda tabuada")