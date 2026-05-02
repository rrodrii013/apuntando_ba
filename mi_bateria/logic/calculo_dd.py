
# aca debo abrir una funcion: si el user decide calcular por dd, ejecutamos la funcion en main.py
#ano, ano_carta, dias_hoy, var_anual, angulo_declinacion

def mi_dd(a, b, c, d, e):
    #Datos calculados segun datos brindados por el user
    ano_hoy = int(a - b)
    dias_hoy_prom = float(c / 365)


    #sumamos diferencia de años + días del año en prom.
    total_hoy = float(ano_hoy + dias_hoy_prom)
    #multiplicacion de var anual y total_hoy
    vara_totalhoy = float(d * total_hoy)
    #sumamos angulo declinacion y anterior
    ad_vara = float(vara_totalhoy + e)
    #restamos 400 (6400m en grados) al valor de ad_vara
    vuelta_ad_totalhoy = float(400 - ad_vara)


    #aplicamos la regla de 3 
    mult_regla_tres = float(6400 * vuelta_ad_totalhoy)
    div_regla_tres = float(mult_regla_tres / 400)

    #resultado dd redondeada hacia arriba
    mi_dd_final = round(div_regla_tres)

    return mi_dd_final



#Parte donde el usuario podrá ver los resultados de los calculos para más transparencia y saber de donde salieron los números
#print(f'Diferencia de años hasta hoy: {ano_hoy}, Promedio de dias: {dias_hoy_prom}, Suma de diferencia de años y promedio de dias: {total_hoy}, Multiplicación de var. anual y suma de diferencia de años y promedio de dias: {vara_totalhoy}, Angulo de declinación sumado a cuenta anterior: {ad_vara}, 400 restado al valor anterior: {vuelta_ad_totalhoy}')
#print(f'Regla de 3: 6400 x {vuelta_ad_totalhoy} / 400')
#print("La DD encontrada es:", final_dd)


#Suguiente parte del proyecto: 
#Añadir sección donde podamos calcular la orientación de la dirección de vigilancia
#Al ingresar el usuario escogerá si se va a apuntar por AV o DD. Simplemente con palabras. Ej si palabra = x se tira por DD.