from .FCFS import FCFS
from .SJF import SJF
from .STCF import STCF
from .RR import RR
    
class MLQ:

    def __init__(self, queues):
        self.queues = queues
    
    #Ejecuta el mlq
    def execute(self):
        self.stats = []
        first = True
        
        for queue in self.queues:
            #Primera ejecucion, tiempo de la cpu = 0
            if first:
                processes = queue[0]
                algorithm = queue[1] 
                algorithm.execute(processes, 0)
                statsTemp = algorithm.getStats()
                for i in statsTemp:
                    self.stats.append(i)
                first = False

            #Siguente ejecucion, tiempo de la cpu se calcual donde termino la anterior
            else:
                
                #Ultimo tiempo de la cpu
                lastTime = max(fila[1] for fila in self.stats)

                processes = queue[0]
                algorithm = queue[1] 
                algorithm.execute(processes, lastTime)
                statsTemp = algorithm.getStats()

                for i in statsTemp:
                    self.stats.append(i)

    #Saca los promedios
    def averages(self):
        wtProm = sum([i[0] for i in self.stats]) / len(self.stats)
        tatProm = sum([i[3] for i in self.stats]) / len(self.stats)
        ctProm = sum([i[1] for i in self.stats]) / len(self.stats)
        rtProm = sum([i[2] for i in self.stats]) / len(self.stats)
        averages = {
            'WT': wtProm,
            'CT': ctProm,
            'RT': rtProm,
            'TAT': tatProm
        }
        return averages

    #Retorna las estadisticas de ejecucion
    def getStats(self):
        return self.stats
        