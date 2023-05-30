# inprtar libreria 
import sys

import sqlite3

from PyQt5  import QtWidgets, uic

# Conectar a la base de datos o crear una nueva si no existe

conn = sqlite3.connect('datos.db')

# conectar la aplicacion
app = QtWidgets.QApplication([])

# cargar pestañas


principal = uic.loadUi("Proyecto (3).ui")
instrucciones = uic.loadUi("Instrucciones_1 (1).ui")
ver_registro = uic.loadUi("ver_registro.ui")
regstro = uic.loadUi("registro.ui")



# funcion principal

def gui_principal():
    principal.show()


# funcion instrucciones

def gui_intrucciones():
    instrucciones.show()


# crear tabla:

conn.execute("CREATE TABLE IF NOT EXISTS personas (nombre TEXT, apellido TEXT, agua_aprovechada TEXT, fecha TEXT)")


def gui_registro():
    # Cargar el archivo .ui y crear la ventana de registro
    registro = uic.loadUi("registro.ui")

    def guardar_datos():
        nombre = registro.lineEdit.text()
        apellido = registro.lineEdit_2.text()
        agua_cantidad = registro.lineEdit_3.text()
        fecha = registro.lineEdit_4.text()

        # Insertar los datos ingresados en la tabla 'personas'
        conn.execute("INSERT INTO personas (nombre, apellido, agua_aprovechada, fecha) VALUES (?, ?, ?, ?)",
                     (nombre, apellido, agua_cantidad, fecha))
        conn.commit()

        # Cerrar la ventana de registro
        registro.close()

    # Conectar la función guardar_datos() al botón de guardar cambios
    registro.Instrucciones_3.clicked.connect(guardar_datos)

    # Mostrar la ventana de registro
    registro.show()

def gui_verregistro():
    cursor = conn.execute("SELECT * FROM personas")

    # Obtener el número de filas y columnas
    num_rows = cursor.rowcount
    num_cols = len(cursor.description)

    # Configurar el número de filas y columnas en el QTableWidget
    ver_registro.tableWidget.setRowCount(0)  # Limpiar las filas existentes
    ver_registro.tableWidget.setRowCount(num_rows)
    ver_registro.tableWidget.setColumnCount(num_cols) 

    # Obtener los datos de la base de datos y rellenar el QTableWidget
    for row_num, row_data in enumerate(cursor):
        ver_registro.tableWidget.insertRow(row_num)
        for col_num, col_data in enumerate(row_data):
            ver_registro.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

    # Mostrar la ventana de visualización del registro
    ver_registro.show()




# funcion para salir de la app

def salir():
    app.exit()
# botones

principal.Instrucciones.clicked.connect(gui_intrucciones)
principal.BaseDeDatos.clicked.connect(gui_verregistro)
principal.Componentes.clicked.connect(gui_registro)
 
# registro

ver_registro.Salir.clicked.connect(salir)



# ejecutar

principal.show()
app.exec()