## Codificación

"""
## Codificación






**6) Suma dos**. Dado un array y un número N retorna true si hay números A y B tal que A + B = N. Sino retorna fallo

* `[1, 2, 3, 4], 5` ⇒ `True`
* `[3, 4, 6], 6` ⇒ `False`

<br/>


**7) Intersection**. Devuelve la intersección de dos listas

* `[1, 2, 4, 6, 10], [2, 4, 5, 7, 10]` ⇒ `[2, 4, 10]`




"""



def imprime_caracter_si_es_multiplo(caracter:int):
    """

    **1) AAABBB.** Imprime números del 1 al 100

    * Si es múltiplo de 3, imprime "AAA"
    * Si es múltiplo de 5, imprime "BBB"
    * Si es múltiplo de 5, imprime "BBB"
    * Si es de ambos — “AAA BBB"
    * Sino imprime el número

    
    Ejemplo de salida: 1, 2, AAA, 4, BBB, AAA, 7, 8, AAA, BBB, 11, AAA, 13, 14, AAA BBB, 16, 17, AAA, 19, BBB, AAA, 22, 23, AAA, BBB, 26, AAA, 28, 29, AAA BBB, 31, 32, AAA, 34, BBB, AAA, ...

    <br/>

    """
    if (caracter % 3) == 0:
        return "AAA"
    
    if (caracter % 5) == 0:
        return "BBB"
    
    return caracter

values = [x for x in range(101) if x > 0]

# for i in values:
#     print(imprime_caracter_si_es_multiplo(i))



def funcion_factorial(numero:int):
    """
    **2) Factorial**. Escribe el factorial de un número

    * `factorial(4)` = 4! = 1 * 2 * 3 * 4 = 24

    <br/>
    
    """
    factorial = numero
    values = [x for x in range(numero) if x > 0]

    for i in values:
        print(factorial)
        factorial = factorial * i

    return factorial

# print(funcion_factorial(4))


def avg(lista: list[int]):
    """
    **3) Media**. Calcula la media de una lista

    * `avg([4, 36, 45, 50, 75]) = 42`

    <br/>
    """

    suma: int = 0

    for i in lista:
        suma = suma + i

    return int(suma/len(lista))


# print(avg([4, 36, 45, 50, 75]))


def devolver_lista_sin_duplicados(lista: list[int]) -> list:
    """
    **4) Borras duplicados**. Elimina duplicados de una lista La lista no está ordenada y el orden de la lista final debe de ser la misma

    * `[1, 2, 3, 2]` ⇒ `[1, 2, 3]`
    * `[1, 2, 2, 1, 5, 3, 2, 1, 4]` ⇒ `[1, 3, 2, 5, 4]`

    <br/>
    
    """
    lista_sin_duplicados: list = []

    for i in lista:
        if i not in lista_sin_duplicados:
            lista_sin_duplicados.append(i)

    return lista_sin_duplicados

# test
# print(devolver_lista_sin_duplicados([1, 2, 3, 2]))
# print(devolver_lista_sin_duplicados([1, 2, 2, 1, 5, 3, 2, 1, 4]))

def cuenta_duplicados(lista: list[int]):

    """
    **5) Contar**. Cuantas veces se repite el elemento de una lista

    `[1, 3, 2, 1, 5, 3, 5, 1, 4]` ⇒  
    * 1: 3 veces
    * 2: 1 vez
    * 3: 2 veces
    * 4: 1 vez
    * 5: 2 veces

    <br/>
    """

    valores_unicos = []
    valores_duplicados = [x for i, x in enumerate(lista) if i != lista.index(x)]
    conteo = {}

    # lista de valores únicos
    for i in lista:
        if i not in valores_unicos:
            valores_unicos.append(i)

    # Inicializamos el contador.
    for x in valores_unicos:
        conteo[x] = 1

    # Establecmos las sumas.
    for j in valores_duplicados:
        for i in lista:
            conteo[j] += 1

    print(conteo, valores_duplicados)

# cuenta_duplicados([1, 3, 2, 1, 5, 3, 5, 1, 4])


def suma_dos(lista: list[int], numero: int):

    """
    **6) Suma dos**. Dado un array y un número N retorna true si hay números A y B tal que A + B = N. Sino retorna fallo

    * `[1, 2, 3, 4], 5` ⇒ `True`
    * `[3, 4, 6], 6` ⇒ `False`

    <br/>
    """
    lista_original = lista
    for i in lista:
        lista_comprobar = [x for x in lista if x != i]
        print(lista_comprobar, i)
        for j in lista_comprobar:
            if j + i == numero:
                return True
            
    return False
        

print(suma_dos([1, 2, 3, 4], 16))
        