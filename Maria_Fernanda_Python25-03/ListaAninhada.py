import time

#Criando uma lista dentro de outra lista usando o for 
Lista = [[x for x in range (4)] for i in range(5)]
print(Lista)

lista2 = [12, 22, 17, 45, 32]
print(lista2)
#Organiza a lista em ordem crescente, alfabetica... (Atualiza as posições)
lista2.sort()
print(lista2)
print(lista2[3])

#Organiza a lista em ordem descrescente... (atualiza as posições) 
lista2.reverse()
print(lista2)


time.sleep(5)