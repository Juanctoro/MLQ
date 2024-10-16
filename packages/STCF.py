class STCF: 

    def __init__(self) -> None:
        pass

    # Execute es el metodo que recibe la lista de instrucciones y las ejecuta
    def execute(self, instructions, ct):
        self.time  = ct
        waitProcess = [] # Procesos en espera
        self.instructions = instructions

        #Se crea una matris del mismo tamaño de las instrucciones para guardar por etiqueta y no por tiempo de completado
        self.matrixStats = [None for _ in range(len(self.instructions))]

        # Diccionarios para el RT y para saber el tiempo restante de cada proceso
        rt = {}
        remainingTime = {} 

        # Se llenan los diccionarios con sus respectivos valores
        for i in self.instructions:
            remainingTime[i[0]] = int(i[1])
            rt[i[0]] = -1

        # Contador que determina si todos los procesos acabaron o falan
        processCompleted = 0
        
        #Ciclo hasta que todos los procesos enten completos
        while processCompleted < len(self.instructions):
            waitProcess = []

            # Para todos los procesos revisa cuales se pueden ejecutar en el tiempo de cpu actual
            for i in self.instructions:
                if int(i[2]) <= self.time and remainingTime[i[0]] > 0:
                    waitProcess.append(i)

            #Si la matris tiene algun proceso disponible entra
            if waitProcess:
                #Organiza los procesos disponibles
                waitProcess.sort(key=lambda x: remainingTime[x[0]])
                currentProcess = waitProcess[0]

                 # Si es la primera ejecucion se le asiga el rt a ese proeso
                if (rt[currentProcess[0]] == -1):
                    rt[currentProcess[0]] = self.time

                # Se merma en 1 el tiempo restante y el tiempo de cpu aumenta 1
                remainingTime[currentProcess[0]] -= 1
                self.time += 1
                
                # Para verificar si el proceso termino se obtiene el timepo restante y se iguala a 0
                # Si se cumple esto entra y se calculan sus estadisticas
                if remainingTime[currentProcess[0]] == 0:
                    processCompleted += 1
                    rtValue = rt[currentProcess[0]]
                    tat = self.time - int(currentProcess[2]) 
                    wt = tat - int(currentProcess[1]) 
                    ct = self.time 
                    tempMatrix = [wt, ct, rtValue, tat]
                    
                    indice = self.instructions.index(currentProcess)
                    self.matrixStats[indice] = tempMatrix

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
