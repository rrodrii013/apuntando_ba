import math
from . import functions
milesimas = 0.05625


def dr_(a, b, c, d):
        
    #Restas de X e Y
    absoluto_x = a - b
    absoluto_y = c - d

    #abs() devuelve un numero entero
    absoluto_x_abs = abs(absoluto_x)
    absoluto_y_abs = abs(absoluto_y)

    dr_division = absoluto_x_abs / absoluto_y_abs

    #math.atan trabaja como tg-1 y degrees() lo pasa a grados ya que .atan devuelve en radianes
    tg_dr = math.degrees(math.atan(dr_division)) 
    dr_milesimas = tg_dr / milesimas


    #Ejecutamos function cuadrantes() para afectarle el mismo
    dr_milesimas = functions.cuadrantes(absoluto_x, absoluto_y, dr_milesimas)

    print("dr:", dr_milesimas)
    mi_dr = dr_milesimas
    return mi_dr
