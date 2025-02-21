import pandas as pd
import streamlit as st

# --- CLASES Y FUNCIONES CRUD --- # Este bloque contiene las funciones que realizan las operaciones CRUD
# --- Funciones para los Estudiantes ---

# Función para agregar un estudiante.
def agregar_estudiante(id_creacion, nombre_creacion, matricula):
    """
    Esta función agrega un estudiante al sistema con los parámetros dados.
    """
    st.session_state['estudiantes'][id_creacion] = {'id':id_creacion, 'Nombre': nombre_creacion, 'Matrícula': matricula}
    st.success(f"Estudiante '{nombre_creacion}' agregado.")  # Mensaje de éxito.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.

# Función para ver un estudiante.
def ver_estudiante(id_busqueda):
    """
    Esta función permite ver un estudiante usando su ID.
    """
    if id_busqueda in st.session_state['estudiantes']:
        st.write(st.session_state['estudiantes'][id_busqueda])  # Muestra los detalles del estudiante.
    else:
        st.error(f"Estudiante con ID '{id_busqueda}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes.

# Función para eliminar un estudiante.
def eliminar_estudiante(id_eliminacion):
    """
    Esta función elimina un estudiante usando su ID.
    """
    if id_eliminacion in st.session_state['estudiantes']:
        del st.session_state['estudiantes'][id_eliminacion]  # Elimina al estudiante del diccionario.
        st.success(f"Estudiante con ID '{id_eliminacion}' eliminado.")  # Mensaje de éxito.
    else:
        st.error(f"Estudiante con ID '{id_eliminacion}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.

# Función para actualizar un estudiante.
def actualizar_estudiante(id_actualizacion, nombre_actualizado, matricula_actualizada):
    """
    Esta función actualiza los datos de un estudiante con los nuevos valores dados.
    """
    if id_actualizacion in st.session_state['estudiantes']:
        st.session_state['estudiantes'][id_actualizacion] = {
            'Nombre': nombre_actualizado,
            'Matrícula': matricula_actualizada
        }
        st.success(f"Estudiante con ID '{id_actualizacion}' actualizado.")  # Mensaje de éxito.
        mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.
    else:
        st.error(f"Estudiante con ID '{id_actualizacion}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.

# Funciones para mostrar los DataFrames
def mostrar_estudiante():
    df = pd.DataFrame.from_dict(st.session_state['estudiantes'], orient='index')
    st.subheader("Listado de Estudiantes")
    st.write(df)

