class FCFS:

    def __init__(self) -> None:
        pass
    
    # Execute es el metodo que recibe la lista de instrucciones y las ejecuta
    def execute(self, instruction, ct):
        self.matrixStats = [] # Matriz donde se va a almacenar lso tiempos de ejecucion de cada procesos
        self.ct = ct
        self.instruction = instruction
        self.instruction.sort(key=lambda x: (x[2])) # Organiza los procesos depende a su orden de llegada
        
        # Ejecuta cada proceso y calcula sus tiempos de ejecucion
        for temp in self.instruction:
            rt = self.ct
            self.ct = self.ct + int(temp[1])
            tat = self.ct - int(temp[2]) 
            wt = tat - int(temp[1])
            tempMatrix = [wt, self.ct, rt, tat]
            self.matrixStats.append(tempMatrix)
    
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