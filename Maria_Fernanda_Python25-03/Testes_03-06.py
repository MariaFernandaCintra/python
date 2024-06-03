import time 
#Bibliotecepara reotr narum número inteiro aleatório 
from random import randint as rd
sorteado = rd(-100, 100)# Sorteia um numero de -100 a 100
print(sorteado)

#criando um lista de numeros inteiros aleatorios 
Lista = [rd(1, 6) for i in range (1, 11)]#tamanho da lista: 10
Lista2 = [x for x in range (1, 11)]
Lista3 = ["Rolo Compressor!!!" for f in range (1, 4)]

#print(Lista)
#print(Lista2)
#print(Lista3)

#Criando lista par 
par = [i for i in range(10) if i % 2 == 0 ]
#print(par)

#Povoando uma lista com input 
#ListaUsuario = [input("Digite um número: ") for p in range (5)]
#print(ListaUsuario)

#Utilizando o metodo split (cada palavra se torna um elemento da lista)
# tes   
#print(nome.split()) #momentaneo

#Aplicando o "split" com o input 
#notas = [n for n in input("Notas: ").split()] #A acada espaço é um elemento da lista 
#print(notas)

# notas2 = [float(n) for n in input("Notas: "). split(",")]#decimais 
# print(notas2)

#Lista com tipos diferentes de dados 
listaMista = [17, 70.5, "Sem mundial", True]
# print(listaMista)

#Manipulação / Fatiamento de listas 
veiculos1 = ["Carro", "Bicicleta", "Motor"]
# print("Veículos 1: ", veiculos1)

#veiculos2 = veiculos1 #É como se fosse outro nome para a lista veículo1

#del veiculos1[0]
#print("Veículos 2: ", veiculos2)

#Copiando todo o conteudo de uma lista para outra 
veiculos2 =  veiculos1[:]
del veiculos1[2]
# print("Veículos 1: ", veiculos1)
# print("Veículos 2: ", veiculos2)

#Copiando parte do conteudo deuma lista 
veiculos3 = veiculos2[0:1]# Não inclui o numero a direita 
# print("Veículos 3: ", veiculos3)

#copiando a parte do conteudo, incluindo o ultimo elemento 
veiculos4 = veiculos2[0:-1]
# print("Veículos 4: ", veiculos4) 

veiculos5 = veiculos2[-1:1]
# print("Veículos 5: ", veiculos5)

#Outras maneiras de fatiamento (omissão do star ou do end)
my_list = ["A", "B", "C", "D", "E", "F"]
print(my_list)
new_list = my_list[:3] # do indice 0 até um indice antes do indicado 
print(new_list)
new_list_fim = my_list[3:] # do indice indicado até o ultimo indice da lista 
print(new_list_fim)

#Apagando conteudo de listas 
del my_list[1:3] # Apagou de um a dois
print(my_list)
del my_list[:] # Apaga todo o conteudo 
print(my_list)

#Testando se alguns itens existem em uma lista ou não 
#Para isso, usamos palavras chave in e not in:
naosei = ["A", "B", 18, 15]
print("A" in naosei)# "A" está dentro da lista naosei, portanto a saída sera true, uma afirmação positiva 
print("C" not in naosei)# "C" não está dentro da lista naosei, portanto a saida será true, uma afirmação verdadeira 
print(15 not in naosei)# O numero 15 não está dentro da lista naosei, çportanto a resposta será falsa  



time.sleep(1)