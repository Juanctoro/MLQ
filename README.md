# Implementación del Algoritmo de Multilevel Queue (MLQ) y los algoritmos FCFS, SJF, STCF y RR

Este proyecto presenta una implementación del algoritmo de **Multilevel Queue (MLQ)** utilizando el paradigma de programación orientado a objetos en **Python**. El algoritmo organiza los procesos en diferentes colas según su prioridad, tiempo de llegada y su respectivo algoritmo.

## Estructura del Proyecto

La implementación se basa en la siguiente estructura:

- **Procesos**: Una lista de procesos con atributos como identificador, tiempo de CPU requerido, tiempo de llegada, etc.
- **Algoritmos**: Clases con la implementacion de la logica que conlleva cada uno de ellos.

- **Colas**: Listas que contienen procesos con sus respectivos parametros y el algoritmo a usarse. en este caso RR(3), RR(5), FCFS.
  - **Cola 1**: Implementa Round Robin con un quantum de 3.
  - **Cola 2**: Implementa Round Robin con un quantum de 5.
  - **Cola 3**: Implementa First-Come, First-Served.

- **MLQ**: Maneja las diferentes colas y se encarga de ejecutar los procesos con sus algoritmos dados

## Funcionalidad
Al clonar el repositorio, debes ingresar en la carpeta **text** los archivos con su debida estructura para la ejecución. Después de tenerlos bien estructurados solo se debe ejecutar el main.

En la carpeta donde tengas el repositorio se creara una carpeta llamada **output**, allí se crearan todos los archivos de salida con su respectivo nombre y la estructura predeterminada para este proyecto.

## Autor
Juan Carlos Toro Cifuentes

