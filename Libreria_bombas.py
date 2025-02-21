import pandas as pd
import streamlit as st


# --- CLASES Y FUNCIONES CRUD --- # Este bloque contiene las funciones que realizan las operaciones CRUD



# --- Funciones para las Bombas ---

# Función para agregar una bomba.
def agregar_bomba(id_creacion, nombre_creacion, presion, amperaje):
    """
    Esta función agrega una bomba al sistema con los parámetros dados.
    """
    st.session_state['bombas'][id_creacion] = {'id':id_creacion, 'Nombre': nombre_creacion, 'Presión': presion, 'Amperaje': amperaje}
    st.success(f"Bomba '{nombre_creacion}' agregada.")  # Mensaje de éxito.
    mostrar_bomba()  # Muestra el DataFrame con las bombas actualizadas.

# Función para ver una bomba.
def ver_bomba(id_busqueda):
    """
    Esta función permite ver una bomba usando su ID.
    """
    if id_busqueda in st.session_state['bombas']:
        st.write(st.session_state['bombas'][id_busqueda])  # Muestra los detalles de la bomba.
    else:
        st.error(f"Bomba con ID '{id_busqueda}' no encontrada.")  # Mensaje de error si no se encuentra la bomba.
    mostrar_bomba()  # Muestra el DataFrame con las bombas.

# Función para eliminar una bomba.
def eliminar_bomba(id_eliminacion):
    """
    Esta función elimina una bomba usando su ID.
    """
    if id_eliminacion in st.session_state['bombas']:
        del st.session_state['bombas'][id_eliminacion]  # Elimina la bomba del diccionario.
        st.success(f"Bomba con ID '{id_eliminacion}' eliminada.")  # Mensaje de éxito.
    else:
        st.error(f"Bomba con ID '{id_eliminacion}' no encontrada.")  # Mensaje de error si no se encuentra la bomba.
    mostrar_bomba()  # Muestra el DataFrame con las bombas actualizadas.

# Función para actualizar una bomba.
def actualizar_bomba(id_actualizacion, nombre_actualizado, presion_actualizada, amperaje_actualizado):
    """
    Esta función actualiza una bomba con los nuevos valores dados.
    """
    if id_actualizacion in st.session_state['bombas']:
        st.session_state['bombas'][id_actualizacion] = {
            'Nombre': nombre_actualizado,
            'Presión': presion_actualizada,
            'Amperaje': amperaje_actualizado
        }
        st.success(f"Bomba con ID '{id_actualizacion}' actualizada.")  # Mensaje de éxito.
        mostrar_bomba()  # Muestra el DataFrame con las bombas actualizadas.
    else:
        st.error(f"Bomba con ID '{id_actualizacion}' no encontrada.")  # Mensaje de error si no se encuentra la bomba.



# Funciones para mostrar los DataFrames
def mostrar_bomba():
    df = pd.DataFrame.from_dict(st.session_state['bombas'], orient='index')
    st.subheader("Listado de Bombas")
    st.write(df)