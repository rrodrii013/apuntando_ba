import math
import functions
milesimas = 0.05625

def dv_(a, b, c, d):
        
    #Restas de X e Y
    absoluto_x = a - b
    absoluto_y = c - d

    #abs() devuelve un numero entero
    absoluto_x_abs = abs(absoluto_x)
    absoluto_y_abs = abs(absoluto_y)

    dv_division = absoluto_x_abs / absoluto_y_abs

    #math.atan trabaja como tg-1 y degrees() lo pasa a grados ya que .atan devuelve en radianes
    tg_dv = math.degrees(math.atan(dv_division)) 
    dv_milesimas = tg_dv / milesimas


    #Ejecutamos function cuadrantes() para afectarle el mismo
    dv_milesimas = functions.cuadrantes(absoluto_x, absoluto_y, dv_milesimas)

    print("dv:", dv_milesimas)
    mi_dv = dv_milesimas
    return mi_dv
