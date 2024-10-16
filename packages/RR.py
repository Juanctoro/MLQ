class RR:

    # Constructor del objeto, cada objeto de tipo RR va a tener um quantum predeterminado
    def __init__(self, q):
        self.quantum = q

    # Execute es el metodo que recibe la lista de instrucciones y las ejecuta
    def execute(self, instruction, ct):
        self.time = ct
        self.instruction = instruction

        #Se crea una matris del mismo tamaño de las instrucciones para guardar por etiqueta y no por tiempo de completado
        self.matrixStats = [None for _ in range(len(self.instruction))] 

        # Diccionarios para el RT y para saber el tiempo restante de cada proceso
        rt = {}
        remainingTime = {} # Por la etiqueta tiene un valor que inicia igual al BT

        # Se llenan los diccionarios con sus respectivos valores
        for i in self.instruction:
            remainingTime[i[0]] = int(i[1])
            rt[i[0]] = -1

        # Contador que determina si todos los procesos acabaron o falan
        processCompleted = 0
        queue = self.instruction.copy()

        while processCompleted < len(self.instruction):
            for i in range(len(queue)):

                # Se asigna el proceso a la variable currentProcess
                if i < len(queue):
                    currentProcess = queue[i]
                
                # Si el proceso cumple las condiciones pasa a la ejecucion
                if int(currentProcess[2]) <= self.time and remainingTime[currentProcess[0]] > 0:
                    
                    # Si es la primera ejecucion se le asiga el rt a ese proeso, cambiando de -1 al valor que le corresponde
                    if (rt[currentProcess[0]] == -1):
                        rt[currentProcess[0]] = self.time

                    # Si el proceso aun tine un tiempo restante mayor al quantum
                    if remainingTime[currentProcess[0]] > self.quantum:
                        remainingTime[currentProcess[0]] -= self.quantum
                        self.time += self.quantum

                    # Si es menor, el proceso entra en esta parte
                    else:
                        self.time += remainingTime[currentProcess[0]]
                        remainingTime[currentProcess[0]] = 0
                    
                    # Para verificar si el proceso termino se obtiene el timepo restante y se iguala a 0
                    # Si se cumple esto entra y se calculan sus estadisticas
                    if remainingTime[currentProcess[0]] == 0:
                        processCompleted += 1
                        rtValue = rt[currentProcess[0]]
                        tat = self.time - int(currentProcess[2]) 
                        wt = tat - int(currentProcess[1]) 
                        ct = self.time 
                        tempMatrix = [wt, ct, rtValue, tat]
                        
                        indice = self.instruction.index(currentProcess)
                        self.matrixStats[indice] = tempMatrix
                
                # Si un proceso termina se saca de la cola, asi le ciclo solo contara con los procesos que aun se pueden ejecutar
                for j in queue:
                    if remainingTime[j[0]] == 0:
                        queue.remove(j)

    # En caso de querer saber los promedios de este algoritmo se llama este metodo          
    def proms(self):
        wtProm = sum([i[0] for i in self.stats]) / len(self.stats)
        tatProm = sum([i[3] for i in self.stats]) / len(self.stats)
        ctProm = sum([i[1] for i in self.stats]) / len(self.stats)
        rtProm = sum([i[2] for i in self.stats]) / len(self.stats)
        print("WT: ", round(wtProm, 1), "\nCT: ", round(ctProm, 1), "\nRT: ",  round(rtProm, 1), "\nTAT: ",  round(tatProm, 1))

    # Retorna la matris con los tiempos de ejecucion de cada procesos
    def getStats(self):
        return self.matrixStats
