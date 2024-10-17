from packages.FCFS import FCFS
from packages.SJF import SJF
from packages.STCF import STCF
from packages.RR import RR
from packages.MLQ import MLQ
from packages.ReWr import READ_AND_WRITE
import os
import glob

#Todos los archivos de texto que se encuentren en la carpeta se leeran y ejecutaran en el MLQ
dirFile = '/home/juantoro/SO/text'
filenames = glob.glob(os.path.join(dirFile, "*.txt"))
readFile = READ_AND_WRITE()

for file in filenames:
    matrixInstruction = readFile.read(file)

    #Se le asignan los procesos a cada fila
    queue0, queue1, queue2 = readFile.assignProcesses(matrixInstruction)

    #Instancia los objetos de los algoritmos
    rr = RR(3)
    rr2 = RR(5)
    fcfs = FCFS()

    #Se le entrega las filas comodadas para la ejecucion y el algoritmo a usarse en cada una
    queues = [
        (queue0, rr),   # Cola 0 con RR(3)
        (queue1, rr2),  # Cola 1 con RR(5)
        (queue2, fcfs), # Cola 2 con FCFS
    ]

    #Se crea el objeto MLQ y se ejecuta, tambien se crean los archivos de salida
    mlq = MLQ(queues)
    mlq.execute()
    fileName = os.path.basename(file)
    readFile.writeOuput(fileName, matrixInstruction, mlq.getStats(), mlq.averages())