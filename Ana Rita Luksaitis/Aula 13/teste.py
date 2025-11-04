#criando e escrevendo (modo w) - sobrescreve tudo
import zipfile
nome=input("Digite o nome do seu arquivo:") 
with open("teste.txt","w") as f:
    f.write("Batatinha quando nasce \n")
    f.write("Esparra pelo chao \n")
    #/n cria uma quebra na linha apos sua chamada
    
#lendo para verificar (modo r) - lê o arquivo criado
with open("teste.txt") as f:
    print("Conteudo após modo w\n",f.read())
    
#adicionando mais conteudo (modo a)- sobrescreve o arquivo
with open("teste.txt", "a") as f:
    f.write("Meninha quando dorme \n")
    f.write("põe a mão no coração \n")
    
#lendo novamente para verificar 
with open("teste.txt", "r") as f:
    print("Conteudo após modo a:\n",f.read())
    
#apenas leitura
with open("teste.txt","r") as f:
    conteudo=f.readline()
#le cada linha e coloca em lista

print("Conteudo do arquivo lido com modo r:")
for linha in conteudo:
    print("-",linha.strip())
#strip remove a quebra da linha visual

#criando um arquivo zip
with zipfile.Zipfile("meus_arquivos.zip","w") as z:
    z.write("teste.txt")
    z.write("ximbinha.txt")
    z.write("Colapso.txt")
    z.write("Xoelma.txt")    
print("Arquivos compactados em meus_arquivos.zip")

'''baixando o zip:
files.download("meus_arquivos.zip")


#descompactando arquivos
with zipfile.ZipFile("meus_arquivos.zip", "r") as z:
    z.extractall("Descompactados")
print("Arquivos descompactados na pasta 'descompactados'")'''