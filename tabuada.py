""""
Imprime a tabuada de 1 ao 10
"""

__version__ = "0.1.0"
__author__ = "Moisés"


#num = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))
#print(num)

#Iterable (percorriveis)


#Para cada numero em numeros:
for num in numeros:
    print("tabuada do:", num)
    for outro_num in numeros:
        print(num * outro_num)
    print("-------------")