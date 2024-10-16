class SJF:

    def __init__(self) -> None:
        pass
    
    # Execute es el metodo que recibe la lista de instrucciones y las ejecuta
    def execute(self, instructions, ct):
        self.matrixStats = [] # Matriz donde se va a almacenar lso tiempos de ejecucion de cada procesos
        self.waitProces = [] # Procesos en espera, listos para ejecutarse
        self.ct = ct
        self.instructions = instructions
        first = True

        for instruction in self.instructions: 

            # Para la primera ejecucion solo se toma el primero en llegar 
            if first:
                rt = self.ct
                wt = self.ct - int(instruction[2])
                self.ct = self.ct + int(instruction[1])
                tat = self.ct - int(instruction[2])
                tempMatrix = [tat, wt, self.ct, rt]
                self.matrixStats.append(tempMatrix)
                first = False
            
            # Agrega los demas procesos a la lista de espera y los organiza
            else:
                self.waitProces.append(instruction)
                self.waitProces.sort(key=lambda x: (x[1]))
        
        # Ejecuta los procesos ya organizados, añadiendo sus tiempos a la matris de estadisticas
        for temp in self.waitProces:
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