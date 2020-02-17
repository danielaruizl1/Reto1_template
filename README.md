# Reto1_template

Este repositorio contiene una plantilla del proyecto del reto con el ejemplo de implementación de una aplicación en el esquema Modelo-Vista-Controlador que carga datos y realiza consultas usando las estructuras de datos implementadas. 

*	ADT: archivos Python con la definición de los Tipos Abstractos de Datos.
*	App: aplicación Python cliente que usa las ADTs y ordenamientos para dar solución a laboratorios y retos.
    * view.py: Entrada y salida de datos e interacción con el usuario
    * controller.py: Comunica la vista con el modelo a través de las operaciones invocadas por el usuario desde la vista
    * model.py: Representa el modelo del mundo.
*	Data: archivos con los datos (csv, json, txt, etc) usados en el laboratorio o reto. El contenido de esta carpeta NO se debe versionar.
*	DataStructures: archivos Python con las estructuras de datos básicas (listas enlazadas y arreglos).
*	Sorting: archivos Python que implementan los algoritmos de ordenamiento.
*	Test: pruebas unitarias en Python para validar el código desarrollado.

![Modelo-Vista-Controlador](http://sistemasproyectos.uniandes.edu.co/iniciativas/architlab/wp-content/uploads/sites/7/2020/02/MVC.png)


Daniela Andrea Ruiz Lopez y Jesús Manuel Ospino Bernal.

¿Se debería ordenar la información? ¿Por qué concepto?
Sí, ya que permite la obtención de datos de manera más eficiente.
La información de las películas se organizó bajo el concepto de promedio de votos.
¿Cómo usar la menor cantidad de memoria posible?
Referenciando apuntadores a otras listas. 
¿Cómo se utilizaron las estructuras de datos vistas en clase?
Se utilizó la lista como Tipo Abstracto de Datos para la resolución de los requerimientos. Lo anterior,
 a través de una vista, un modelo y un controlador, lo cuales permitian una implementación versatil en caso de
 querer cambiar el tipo de lista a usar (lista encadenada o arreglo). Asimismo, se utilizó el tipo de ordamiento
 mergesort para organizar las listas de películas bajo el el promedio de votos de esta, ya que se considera el método
 de ordamiento más eficiente y estable. 

