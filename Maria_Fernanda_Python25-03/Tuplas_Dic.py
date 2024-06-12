import time

tupla = tuple()
tupla = (1)
tupla = (1,)
tupla = 1, 2, 3 

print(tupla)
print(tupla[1])
#tupla[0] = 100 ERRO, pois não é possivel alterar uma tupla

#Manipulando dicionarios 
dic = {"semMundial":"Palmeiras", "1Mundial":"Corinthias", "2Mundias":"SãoPaulo"}

print(dic['semMundial'])

notas = {"Matematica":5, "LP":10, "EF":8 }
print(notas)
print("Nota de Lingua Portugesa:",notas["LP"])

print(dir(notas))# Lista de funcionalidades/metodos que podem ser usados em "notas"

print(notas.values())
print(notas.keys())
print(len(notas))

for disciplina in notas.keys():
    print(disciplina)
time.sleep(5)