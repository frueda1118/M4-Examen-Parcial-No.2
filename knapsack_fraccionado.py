#Universidad del Valle de Guatemala
#Análisis y Diseño de Algoritmos - Sección 20
#Fernando Rueda - 23748
#Problema 2: Knapsack fraccionado
#Algoritmo greedy que maximiza el valor robado ordenando
#los artículos por razón precio/peso descendente.

def knapsack_fraccionado(p, w, W):
    n = len(p)
    #calcula la razón precio/peso para cada artículo y guarda su índice original
    items = []
    for i in range(n):
        r = p[i] / w[i]
        items.append((r, p[i], w[i], i))
    #ordena descendentemente por razón
    items.sort(key=lambda x: x[0], reverse=True)
    c = [0] * n
    espacio = W
    for r, precio, peso, idx_original in items:
        if espacio == 0:
            break
        cantidad = min(peso, espacio)
        c[idx_original] = cantidad
        espacio = espacio - cantidad
    return c

def imprimir_resultado(p, w, W, c):
    n = len(p)
    print(f"Capacidad de la bolsa: W = {W}")
    print("Artículos disponibles:")
    for i in range(n):
        print(f"  Artículo {i + 1}: peso = {w[i]}, precio = {p[i]}, razón = {p[i] / w[i]:.2f}")
    valor_total = 0
    peso_total = 0
    print("Solución:")
    for i in range(n):
        if c[i] > 0:
            valor = (p[i] / w[i]) * c[i]
            valor_total += valor
            peso_total += c[i]
            print(f"  {c[i]} unidades del artículo {i + 1} (valor: {valor:.2f})")
    print(f"Peso total: {peso_total} / {W}")
    print(f"Valor total: {valor_total:.2f}")
    print()

#caso 1: ejemplo del enunciado (item1: w=10 p=60, item2: w=20 p=100, item3: w=30 p=120, W=50)
print("=== Caso 1: ejemplo del enunciado ===")
p1 = [60, 100, 120]
w1 = [10, 20, 30]
W1 = 50
c1 = knapsack_fraccionado(p1, w1, W1)
imprimir_resultado(p1, w1, W1, c1)

#caso 2: cuatro artículos con razones variadas
print("=== Caso 2 ===")
p2 = [40, 30, 50, 70]
w2 = [8, 5, 10, 14]
W2 = 25
c2 = knapsack_fraccionado(p2, w2, W2)
imprimir_resultado(p2, w2, W2, c2)

#caso 3: la bolsa cabe todos los artículos completos
print("=== Caso 3: cabe todo ===")
p3 = [20, 30, 15]
w3 = [4, 6, 3]
W3 = 100
c3 = knapsack_fraccionado(p3, w3, W3)
imprimir_resultado(p3, w3, W3, c3)
