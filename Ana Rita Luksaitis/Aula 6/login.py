'''Criar um sistema onde uma pessoa informa o Usuário e a Senha pessoal.
Caso o usuário for igual a "senai" e a senha igual a "senai123", então mostrar "Bem vindo! Entrada autorizada.".
Caso contrário, mostrar "ENTRADA NEGADA! Usuário ou senha incorreta."'''

user = str(input("Digite o usuário: "))
password = str(input("Digite a senha: "))

if(user=="" or password==""):
    print("Preencha os campos obrigatórios.")
else:
    if (user=="senai" and password=="senai123"):
        print("Bem vindo!!!! Entrada autorizada.")
    elif (user=="senai" and password!="senai123"):
        print("ENTRADA NEGADA! Senha incorreta.")
    elif (user!="senai" and password=="senai123"):
        print("ENTRADA NEGADA! Usuário incorreto.")
    else:
        print("ENTRADA NEGADA!!! Usuário ou senha incorreta.")
    
#Desafio: Se o usuário for igual a "senai" e a senha diferente de "senai123", então "ENTRADA NEGADA! Senha incorreta."
#Se o usuário for diferente de "senai" e a senha for igual, então "ENTRADA NEGADA! Usuário incorreto."

