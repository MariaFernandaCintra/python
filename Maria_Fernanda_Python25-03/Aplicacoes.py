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
    print("elemneto encontrado no indice: ", i)
else:
    print("Elemento não encontrado!!!")  
time.sleep(3)