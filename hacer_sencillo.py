#Universidad del Valle de Guatemala
#Análisis y Diseño de Algoritmos - Sección 20
#Fernando Rueda - 23748
#Problema 1: Hacer sencillo
#Algoritmo greedy que encuentra la mínima cantidad de monedas para alcanzar un monto m, usando denominaciones {25, 10, 5, 1}.

def hacer_sencillo(m):
    D = [25, 10, 5, 1]
    c = [0, 0, 0, 0]
    for i in range(4):
        c[i] = m // D[i]
        m = m - c[i] * D[i]
    return c

def imprimir_resultado(monto_centavos, c):
    D = [25, 10, 5, 1]
    total_monedas = sum(c)
    print(f"Monto: Q{monto_centavos / 100:.2f} ({monto_centavos} centavos)")
    print(f"Cantidad mínima de monedas: {total_monedas}")
    for i in range(4):
        if c[i] > 0:
            print(f"  {c[i]} moneda(s) de Q{D[i] / 100:.2f}")
    print()

casos = [293, 99, 67, 100, 1]
for monto in casos:
    resultado = hacer_sencillo(monto)
    imprimir_resultado(monto, resultado)
