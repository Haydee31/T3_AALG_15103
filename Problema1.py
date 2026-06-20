VIDAS_INICIALES = 3
def imprime(mat):
    for fil in mat:
        print(fil)
    print()
 
def valido(lab, visitado, f, c):
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    if lab[f][c] == 0:
        return False
    if visitado[f][c] == 1:
        return False
    return True
 
def sollab(lab, res, visitado, f, c, vidas, paso):
    if f == 0 and c == 0:
        res[f][c] = 1
        visitado[f][c] = 1
        paso[0] += 1
        print(f"Paso {paso[0]}: el raton llega a F ({f},{c}) | Vidas restantes: {vidas}")
        imprime(res)
        return True
    else:
        if valido(lab, visitado, f, c):
            valor = lab[f][c]
            vidas_nuevas = vidas
            if valor == -1:
                vidas_nuevas -= 1
            elif valor == -2:
                vidas_nuevas -= 2
 
            if vidas_nuevas <= 0:
                print(f"-> Casilla ({f},{c}) tiene valor {valor}: el raton perderia "
                      f"sus {VIDAS_INICIALES} vidas. Camino inviable, se descarta.")
                return False
            res[f][c] = 1
            visitado[f][c] = 1
            paso[0] += 1
            print(f"Paso {paso[0]}: avanza a ({f},{c}) | Valor casilla: {valor} | "
                  f"Vidas restantes: {vidas_nuevas}")
            imprime(res)
 
            if sollab(lab, res, visitado, f + 1, c, vidas_nuevas, paso):
                return True
            elif sollab(lab, res, visitado, f, c + 1, vidas_nuevas, paso):
                return True
            elif sollab(lab, res, visitado, f - 1, c, vidas_nuevas, paso):
                return True
            elif sollab(lab, res, visitado, f, c - 1, vidas_nuevas, paso):
                return True
            else:
                res[f][c] = 0
                visitado[f][c] = 0
                print(f"Retrocede desde ({f},{c}), no hay salida por aqui.")
                return False
        else:
            return False
        
lab = [
    [1,  1,  1,  1,  0,  1,  1,  1,  1],  
    [-2, 0,  0, -1,  0,  1,  0,  1,  0],  
    [1,  1,  0,  1,  1,  1,  0,  1,  0],   
    [0,  1,  0, -1,  0,  0,  0, -1,  0], 
    [1,  1,  1,  1,  1,  1,  1,  1,  0],  
    [-1, 0,  0,  0,  0,  0,  0,  1,  1],  
    [1,  1,  1,  1, -1,  1,  1,  1,  0],  
    [1,  0,  0,  1,  0,  1,  0,  1,  0],  
    [1,  1, -1,  1,  1,  1,  0,  1,  1],  
]
 
lab_mostrar = [fila[:] for fila in lab]
lab_mostrar[0][0] = "F"
lab_mostrar[8][0] = "I"
 
print("=" * 60)
print("LABERINTO ORIGINAL (F = llegada, I = salida del raton)")
print("=" * 60)
imprime(lab_mostrar)
 
filas = len(lab)
columnas = len(lab[0])
res = [[0 for _ in range(columnas)] for _ in range(filas)]
visitado = [[0 for _ in range(columnas)] for _ in range(filas)]
paso = [0]
 
print("=" * 60)
print("RECORRIDO PASO A PASO (orden: abajo, derecha, arriba, izquierda)")
print("=" * 60)
 
encontrado = sollab(lab, res, visitado, filas - 1, 0, VIDAS_INICIALES, paso)
 
print("=" * 60)
if encontrado:
    print(f"EL RATON LOGRO SALIR DEL LABERINTO en {paso[0]} pasos efectivos.")
else:
    print("EL RATON NO LOGRO SALIR DEL LABERINTO. No existe un camino viable "
          "que no le haga perder sus 3 vidas.")
print("=" * 60)
print()
print("Matriz que indica el camino tomado (1 = casilla usada en el camino):")
imprime(res)