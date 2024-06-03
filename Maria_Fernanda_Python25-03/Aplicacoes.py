import time 
#Encontrar o maior valor na lista - exemplo 1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maiorNumero = lista[0] #recebeu o numero 17

for i in range(1, len(lista)):
    if lista[i] > maiorNumero:
        maiorNumero = lista[i]
print("O maior número da lista é: ", maiorNumero)

#Exemplo2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
# maior = my_list[0]
# for i in my_list:
#     if i > maior:
#         maior = i
# print("O maior valor da lista my_List é: ", maior)

#Exemplo3
ultima_lista = my_list[:]
Mel = ultima_lista[0]
for i in ultima_lista[1:]:
    if i > Mel:
        Mel = i
print("O maior elemento é: ", Mel)

#Encontrar a localização de um determinado elemento dentro de uma lista 
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range (len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break
if achado:
    print("elemento encontrado no indice: ", i)
else:
    print("Elemento não encontrado!!!")  

#Conferidor de aposta em loteria 
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0 

for numero in sorteados:
    if numero in apostados:
        acertos += 1
print("A quantidade de acertos foi de: ", acertos)

#Remoção de números repetidos em uma lista 
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista original: ", lista)

#lista de apoio
vistos = []

#Iterar pela lista original de trás para frente 
for i in range(len(lista) -1, -1, -1):
    # Se o número já está na lista "vistos", removelo da lista original 
    if lista[i] in vistos:
        del lista[i]
    else:
        #Caso contrário, adicionar à lista "vistos"
        vistos.append(lista[i])
print("lista modificada: ", lista)

#Listas avançadas 
#2D - listas aninhadas bidimensionais 
tabela = [[":(", ":)", ":|", ";-;"], [";-:", ":|", ":)", ":("], [":|", ":)", ";-;", ":("]]
print(tabela[0][3])# Motrar o index de uma matriz
print(tabela[2][2])
print(tabela)

#3D - TRIDIMENSIONAL 
cubo = [ [[":(", "y", "z"], [":)", "y", "z"], [":|", "y", "z"]], 
    [["Amor", "Ódio", "Caridade"], ["Paz", "Esperaça", "Férias"], ["tina", "Prior", "pp"]],  
    [["Restinga", "Patrocinio", "Rifaina"], ["Amazonense", "Fluminense", "Santos"], ["Pizza", "Lasanha", "Pastel"]] ]

print(cubo)
print(cubo[1])
print(cubo[1][0])
print(cubo[1][0][2])


time.sleep(3)