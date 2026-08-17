import streamlit as st

# Importaciones de tu lógica 
import logic.calculo_dd as calculo_dd
import logic.calculo_dv as calculo_dv
import logic.calculo_o_dr as calculo_o_dr
from logic.functions import ang_vigilancia_or_o 
from logic.functions import calculo_distancia 

st.title('Apuntando tu Batería 💣')

# user selecciona el método de puntería deseado
seleccion_de_calculo = st.selectbox(
    "Selecciona el método por el que deseas apuntar:",
    ['Ángulo de vigilancia', 'Orientación']
)

st.write("---")

# ---------------------------------------------------------
# OPCIÓN 1: ÁNGULO DE VIGILANCIA
# ---------------------------------------------------------
if seleccion_de_calculo == 'Ángulo de vigilancia':
    
   #F O R M
    with st.form("form_angulo"):
        st.subheader("Ingreso de Coordenadas")
        st.info("Todas las coordenadas deben contener 6 dígitos.")
        
        # format="%d" para que el número se vea como entero y sin comas
        coordenadas_x_pv = st.number_input("Coordenadas de X en PV:", step=1, format="%d", value=0)
        coordenadas_y_pv = st.number_input("Coordenadas de Y en PV:", step=1, format="%d", value=0)
        coordenadas_x_cb = st.number_input("Coordenadas de X en CB:", step=1, format="%d", value=0)
        coordenadas_y_cb = st.number_input("Coordenadas de Y en CB:", step=1, format="%d", value=0)
        coordenadas_x_dr = st.number_input("Coordenadas de X en DR:", step=1, format="%d", value=0)
        coordenadas_y_dr = st.number_input("Coordenadas de Y en DR:", step=1, format="%d", value=0)
        
        # Btn para enviar el formulario
        submit_btn = st.form_submit_button("Enviar datos")
        
    # Lógica de validación y cálculo 
    if submit_btn:
        # Agrupamos los datos en una lista para revisarlos rápidamente
        datos = [coordenadas_x_pv, coordenadas_y_pv, coordenadas_x_cb, coordenadas_y_cb, coordenadas_x_dr, coordenadas_y_dr]
        
        # Comprobamos si hay algún dato que no tenga 6 dígitos
        ## guardo dato en la lista
        datos_invalidos = [dato for dato in datos if len(str(abs(int(dato)))) != 6]
        
        if datos_invalidos:
            st.error("🚨 Error: Ingresaste coordenadas no válidas. Verifica e intenta nuevamente.")
        else:
            # Si todo está bien, calculamos
            mi_dv = calculo_dv.dv_(coordenadas_x_pv, coordenadas_x_cb, coordenadas_y_pv, coordenadas_y_cb)
            mi_dr = calculo_o_dr.dr_(coordenadas_x_dr, coordenadas_x_cb, coordenadas_y_dr, coordenadas_y_cb)
            mi_av = ang_vigilancia_or_o(mi_dr, mi_dv)
            mi_distancia = calculo_distancia(coordenadas_x_pv, coordenadas_x_cb, coordenadas_y_pv, coordenadas_y_cb)
            
            st.success("✅ ¡Datos procesados correctamente!")
            
            st.write(f'**La orientación de la DR es:** {round(mi_dr)}')
            st.write(f'**La orientación de la DV es:** {round(mi_dv)}')
            st.write(f'**El ángulo de vigilancia es:** {round(mi_av)}')
            st.write(f'**La distancia es:** {round(mi_distancia)}')


# ---------------------------------------------------------
# OPCIÓN 2: ORIENTACIÓN
# ---------------------------------------------------------
elif seleccion_de_calculo == 'Orientación':
    
    with st.form("form_orientacion"):
        st.subheader("Datos de la Carta")
        ano_carta = st.number_input("Año de creación de la carta:", step=1, format="%d", value=1980)
        ano = st.number_input("Año corriente:", step=1, format="%d", value=2026, min_value=2026)
        var_anual = st.number_input("Variación anual (ej. 0.5):", format="%.2f", value=0.0)
        dias_hoy = st.number_input("Cantidad de días hasta la fecha:", step=1, format="%d", min_value=0, value=1)
        angulo_declinacion = st.number_input("Ángulo de declinación que indica la carta:", format="%.2f", value=0.0)
        
        st.write("---")
        st.subheader("Ingreso de Coordenadas")
        st.info("Todas las coordenadas deben contener 6 dígitos.")
        
        coordenadas_x_pv = st.number_input("Coordenadas de X en PV:", step=1, format="%d", value=0)
        coordenadas_y_pv = st.number_input("Coordenadas de Y en PV:", step=1, format="%d", value=0)
        coordenadas_x_cb = st.number_input("Coordenadas de X en CB:", step=1, format="%d", value=0)
        coordenadas_y_cb = st.number_input("Coordenadas de Y en CB:", step=1, format="%d", value=0)
        
        submit_btn = st.form_submit_button("Enviar datos")
        
    if submit_btn:
        datos_coord = [coordenadas_x_pv, coordenadas_y_pv, coordenadas_x_cb, coordenadas_y_cb]
        datos_invalidos = [dato for dato in datos_coord if len(str(abs(int(dato)))) != 6]
        
        if datos_invalidos:
            st.error("🚨 Error: Ingresaste coordenadas no válidas. Verifica e intenta nuevamente.")
        else:
            mi_dv = calculo_dv.dv_(coordenadas_x_pv, coordenadas_x_cb, coordenadas_y_pv, coordenadas_y_cb)
            mi_dd = calculo_dd.mi_dd(ano, ano_carta, dias_hoy, var_anual, angulo_declinacion)
            mi_orientacion = ang_vigilancia_or_o(mi_dd, mi_dv)
            
            st.success("✅ ¡Datos procesados correctamente!")
            st.write(f'**La DD es:** {mi_dd}') 
            st.write(f'**La DV es:** {round(mi_dv)}') 
            st.write(f'**La Orientación es:** {round(mi_orientacion)}')

            st.title("© 2026 Alf. Mateo Rodríguez ")