#Universidad del Valle de Guatemala
#Análisis y Diseño de Algoritmos - Sección 20
#Fernando Rueda - 23748
#Problema 3: Combinaciones de n dígitos en el teclado del Nokia 3230
#Programación dinámica bottom-up que cuenta cuántas secuencias de longitud n se pueden formar moviéndose ortogonalmente entre teclas.

#tabla de adyacencia: cada dígito incluye a sí mismo y a sus vecinos válidos
adj = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [1, 2, 3, 5],
    3: [2, 3, 6],
    4: [1, 4, 5, 7],
    5: [2, 4, 5, 6, 8],
    6: [3, 5, 6, 9],
    7: [4, 7, 8],
    8: [0, 5, 7, 8, 9],
    9: [6, 8, 9]
}

def contar_combinaciones(n):
    C = [[0] * 10 for _ in range(n + 1)]
    #caso base: secuencias de longitud 1, una por cada dígito
    for d in range(10):
        C[1][d] = 1
    #llena las filas siguientes usando la recurrencia
    for k in range(2, n + 1):
        for d in range(10):
            for e in adj[d]:
                C[k][d] = C[k][d] + C[k - 1][e]
    total = 0
    for d in range(10):
        total = total + C[n][d]
    return total, C

def imprimir_resultado(n, total, C):
    print(f"n = {n}")
    print(f"Combinaciones que terminan en cada dígito:")
    for d in range(10):
        print(f"  dígito {d}: {C[n][d]}")
    print(f"Total de combinaciones: {total}")
    print()

#caso 1: n = 2 (esperado: 36 según el enunciado)
total1, C1 = contar_combinaciones(2)
imprimir_resultado(2, total1, C1)

#caso 2: n = 4
total2, C2 = contar_combinaciones(4)
imprimir_resultado(4, total2, C2)

#caso 3: n = 7
total3, C3 = contar_combinaciones(7)
imprimir_resultado(7, total3, C3)
