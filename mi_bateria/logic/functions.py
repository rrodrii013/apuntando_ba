import math

#CUADRANTES 

def cuadrantes(x, y, dv):
    if x > 1 and y < 1:
        return 3200 - dv 
        print("cuadrante 2")
    elif x < 1 and y < 1:
        return 3200 + dv
        print("cuadrante 3")
    elif x < 1 and y > 1:
        return 6400 - dv
        print("cuadrante 4")
    else:
        return


#Calculo AV
def ang_vigilancia_or_o(valor_dr, valor_dv):
    av = valor_dr - valor_dv
    if av < 1:
        av += 6400
    return av


#Calculo de distancia 
def calculo_distancia(a, b, c, d):
    valores_x = a - b
    valores_y = c - d
    #abs() devuelve un numero entero
    valores_x_ent = abs(valores_x)
    valores_y_ent = abs(valores_y)
    #math.sqrt() equivale a raiz cuadrada, pow() eleva el primer digito por el segundo
    mi_distancia = math.sqrt(pow(valores_x_ent, 2) + pow(valores_y_ent, 2))
    return mi_distancia