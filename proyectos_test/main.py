import calculo_dd
import calculo_dv
import calculo_o_dr
from functions import ang_vigilancia_or_o
from functions import calculo_distancia


#User selecciona el metodo de punteria deseado
seleccion_de_calculo = input(f'Escribe por que metodo deseas apuntar:\n"Angulo de vigilancia"\n"Orientacion"\n')
if seleccion_de_calculo.lower() == 'angulo de vigilancia':
    #Coordenadas X PV
    while True:
        try:
            coordenadas_x_pv_str = input("Ingresa las coordenadas de X en PV:")
            if len(coordenadas_x_pv_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_x_pv = int(coordenadas_x_pv_str)
                print("Dato guardado.")
                break
        except ValueError:
            print("Por favor, ingresa un valor valido.")

    #Coordenadas Y PV        
    while True:
        try:
            coordenadas_y_pv_str = input("Ingresa las coordenadas de Y en PV:")
            if len(coordenadas_y_pv_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_y_pv = int(coordenadas_y_pv_str)
                print("Dato guardado.")
                break
        except ValueError:
            print("Por favor, ingresa un valor valido.")

    #coordenadas X CB 
    while True:
        try:
            coordenadas_x_cb_str = input("Ingresa las coordenadas de X en CB:")
            if len(coordenadas_x_cb_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_x_cb = int(coordenadas_x_cb_str)
                print("Dato guardado.")
                break
        except ValueError:
            print("Por favor, ingresa un valor valido.")
    #coordenadas Y CB 
    while True:
        try:
            coordenadas_y_cb_str = input("Ingresa las coordenadas de Y en CB:")
            if len(coordenadas_y_cb_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_y_cb = int(coordenadas_y_cb_str)
                print("Dato guardado.")
                break
        except ValueError:
            print("Por favor, ingresa un valor valido.")
               
                #Coordenadas X DR
    while True:
        try:
            coordenadas_x_dr_str = input("Ingresa las coordenadas de X en DR:")
            if len(coordenadas_x_dr_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_x_dr = int(coordenadas_x_dr_str)
                print("Dato guardado.")
            break
        except ValueError:
            print("Por favor, ingresa un valor valido.")

        #Coordenadas Y DR       
    while True:
        try:
            coordenadas_y_dr_str = input("Ingresa las coordenadas de Y en DR:")
            if len(coordenadas_y_dr_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_y_dr = int(coordenadas_y_dr_str)
                print("Dato guardado.")
            break
        except ValueError:
            print("Por favor, ingresa un valor valido.")
    
    #importamos funcion de calculo ODV y ODR
    mi_dv = calculo_dv.dv_(coordenadas_x_pv,coordenadas_x_cb, coordenadas_y_pv, coordenadas_y_cb)
    mi_dr = calculo_o_dr.dr_(coordenadas_x_dr, coordenadas_x_cb, coordenadas_y_dr, coordenadas_y_cb)

    #resultado final AV y Distancia
    mi_av = ang_vigilancia_or_o(mi_dr, mi_dv)
    print(f'El angulo de vigilancia es: {round(mi_av)}')
    mi_distancia = calculo_distancia(coordenadas_x_pv, coordenadas_x_cb, coordenadas_y_pv, coordenadas_y_cb)
    print(f'La distancia es: {round(mi_distancia)}')


elif seleccion_de_calculo.lower() == 'orientacion':
    while True:
        try:
            ano_carta = int(input("Ingresa el año de creación de la carta:"))
            break
        except ValueError:
            print("Por favor, ingresa un valor valido.")
        else:
            print("Dato guardado.")

    while True:
        try:
            ano = int(input("Ingresa el año corriente:"))
            break
        except ValueError:
            print("Por favor, ingresa un valor valido.")
        else:
            print("Dato guardado.")

    while True:    
        try:
            var_anual = float(input("Ingresa la variación anual:"))
            break
        except ValueError:
            print("Por favor, ingresa un valor valido.")
        else:
            print("Dato guardado.")

    while True:
        try:
            dias_hoy = int(input("Ingresa la cantidad de dias hasta la fecha:"))
            break
        except ValueError:
            print("Por favor, ingresa un valor valido.")
        else:
            print("Dato guardado.")

    while True:
        try:
            angulo_declinacion = float(input("Ingresa el angulo de declinacion que indica la carta:"))
            break
        except ValueError:
            print("Por favor, ingresa un valor valido.")
        else:
            print("Dato guardado.")

            #Coordenadas X PV
    while True:
        try:
            coordenadas_x_pv_str = input("Ingresa las coordenadas de X en PV:")
            if len(coordenadas_x_pv_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_x_pv = int(coordenadas_x_pv_str)
                print("Dato guardado.")
                break
        except ValueError:
            print("Por favor, ingresa un valor valido.")

    #Coordenadas Y PV        
    while True:
        try:
            coordenadas_y_pv_str = input("Ingresa las coordenadas de Y en PV:")
            if len(coordenadas_y_pv_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_y_pv = int(coordenadas_y_pv_str)
                print("Dato guardado.")
                break
        except ValueError:
            print("Por favor, ingresa un valor valido.")

    #coordenadas X CB 
    while True:
        try:
            coordenadas_x_cb_str = input("Ingresa las coordenadas de X en CB:")
            if len(coordenadas_x_cb_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_x_cb = int(coordenadas_x_cb_str)
                print("Dato guardado.")
                break
        except ValueError:
            print("Por favor, ingresa un valor valido.")

    #coordenadas Y CB 
    while True:
        try:
            coordenadas_y_cb_str = input("Ingresa las coordenadas de Y en CB:")
            if len(coordenadas_y_cb_str) != 6:
                print("Dato no valido. Recuerda que las coordenadas deben ser números y tener 6 digitos.")
            else:
                coordenadas_y_cb = int(coordenadas_y_cb_str)
                print("Dato guardado.")
                break
        except ValueError:
            print("Por favor, ingresa un valor valido.")

    #importamos funcion para registrar coordenadas pv, datos carta y datos actuales

    #importamos funcion de calculo por orientacion
    mi_dv = calculo_dv.dv_(coordenadas_x_pv,coordenadas_x_cb, coordenadas_y_pv, coordenadas_y_cb)
    mi_dd = calculo_dd.mi_dd(ano, ano_carta, dias_hoy, var_anual, angulo_declinacion)
    print(mi_dd, type(mi_dd))
    resultado_dd = mi_dd.resultado_dd
    resultado_dv = mi_dv.mi_dv
    mi_orientacion = ang_vigilancia_or_o(resultado_dd, resultado_dv)
    print(f'La DD es: {resultado_dd}') 
    print(f'La DV es: {mi_dresultado_dv}') 
    print(f'La Orientación es: {mi_orientacion}') 
else:
    print("Por favor, verifica haber escrito correctamente el metodo por el cual deseas apuntar.")