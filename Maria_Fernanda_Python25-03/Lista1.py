import time 

numeros = [111, 7, 2, 1]
print(len(numeros))

#Acrescenta um numero na ultima posição
numeros.append(52)
print(len(numeros))
print(numeros)

#Acrescenta um numero em uma certa posição e joga os numeros 
#adiante para uma posição a frente que estavam
numeros.insert(0,222)
print(len(numeros))
print(numeros)

#Acresnta um número na ultima posição, mas como o numero vai sobrepor uma posição 
#ele joga o numero que estava naquela posição para 
#frente deixando assim o numero que foi acresentdo na penultima posição
numeros.insert(-1, 12)
print(numeros)

numeros.insert(1, 18)
print(numeros)

numeros.insert(-2, 20)
print(numeros)



time.sleep(5)