#1 CREACIÓN DE INSTANCIA APLICACIÓN EN FLASK
from flask import Flask, render_template, request
app = Flask(__name__)
#2 DEFINICIÓN DE RUTAS
@app.route('/')
def index():
    return render_template('index.html')
#3 DEFINICIÓN DE RUTAS Y FUNCIONES
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        #3.1 SE DEFINEN VARIABLES QUE RECIBEN LOS VALORES INGRESADOS DESDE EL FORMULARIO
        nota1 = request.form['num1']
        nota2 = request.form['num2']
        nota3 = request.form['num3']
        asist = request.form['num4']

        #3.2 SE DEFINEN VARIABLES QUE CONVIERTEN LOS VALORES RECIBIDOS DESDE EL FORMULARIO A TIPO INT
        suma = int(nota1) + int(nota2) + int(nota3)
        promedio = suma/3
        asistencia = int(asist)
        estado = ' '

        #3.3 ESTRUCTURA CONDICIONAL IF-ELSE PARA RETORNAR UN VALOR U OTRO
        #--- SE RETORNA EL ARCHIVO HTML
        #--- SE RETORNAN 2 VARIABLES CON VALORES QUE SERAN UTILIZADOS EN EL ARCHIVO HTML
        if promedio >= 4.0 and asistencia >= 75:
            estado = 'Aprobado'
            return render_template('ejercicio1.html', promedio= promedio, estado=estado)
        else:
            estado = 'Reprobado'
            return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        #3.4 SE DEFINEN VARIABLES QUE RECIBEN LOS VALORES INGRESADOS DESDE EL FORMULARIO
        nombre = request.form['nombre']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        #3.5 SE INICIALIZAN 4 VARIABLES EN 0 Y UNA DE TIPO STRING VACÍA
        total1 = 0
        total2 = 0
        total3 = 0
        mayor = 0
        nom = ''
        #3.6 SE DECLARAN 3 VARIABLES DE TIPO STRING LAS CUALES SERÁN RETORNADAS DESDE LA FUNCIÓN HACIA EL ARCHIVO HTML
        string = 'El nombre con mayor cantidad de caracteres es: '
        string2 = 'El nombre tiene: '
        string3 = 'caracteres.'
        #3.7 SE DECLARAN 3 BUCLES FOR, CADA UNO RECORRE CADA NOMBRE RECIBIDO DESDE EL FORMULARIO
        #--- POR CADA LETRA RECORRIDA VA SUMANDO 1 A LA VARIABLE ANTES DEFINIDA (TOTAL1, TOTAL2, TOTAL3)
        for i in nombre:
            total1 = total1 + 1

        for i in nombre2:
            total2 = total2 + 1

        #3.8 ESTRUCTURA CONDICIONAL IF-ELIF
        #--- EVALUA CUAL VARIABLE RECORRIDA OBTUVO MÁS CARACTERES
        #--- LA VARIABLE MAYOR TOMARÁ EL VALOR DE (TOTAL1, TOTAL2 O TOTAL3)
        #--- LA VARIABLE NOM TOMARÁ EL MISMO VALOR RECIBIDO DESDE EL FORMULARIO
        for i in nombre3:
            total3 = total3 + 1

        if total1 > total2 and total1 > total3:
            mayor = total1
            nom = nombre
            return render_template('ejercicio2.html', string=string, string2=string2, string3=string3, nom=nombre, mayor=mayor)
        elif total2 > total1 and total2> total3:
            mayor = total2
            nom = nombre2
            return render_template('ejercicio2.html', string=string, string2=string2, string3=string3, nom=nombre2, mayor=mayor)
        elif total3 > total1 and total3> total2:
            mayor = total3
            nom = nombre3
            return render_template('ejercicio2.html', string=string, string2=string2, string3=string3, nom=nombre3, mayor=mayor)

    return render_template('ejercicio2.html')
#4 EJECUCIÓN DE LA APLICACIÓN
if __name__ == '__main__':
    app.run(debug=True)