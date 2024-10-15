class STCF: 

    def __init__(self) -> None:
        pass

    def execute(self, instructions, ct):
        self.time  = ct
        waitProcess = []
        self.instructions = instructions
        self.matrixStats = [None for _ in range(len(self.instructions))]
        rt = {}
        remainingTime = {} 

        for i in self.instructions:
            remainingTime[i[0]] = int(i[1])
            rt[i[0]] = -1
        processCompleted = 0
        
        while processCompleted < len(self.instructions):
            waitProcess = []

            for i in self.instructions:
                if int(i[2]) <= self.time and remainingTime[i[0]] > 0:
                    waitProcess.append(i)
            
            if waitProcess:
                waitProcess.sort(key=lambda x: remainingTime[x[0]])
                currentProcess = waitProcess[0]

                if (rt[currentProcess[0]] == -1):
                    rt[currentProcess[0]] = self.time

                remainingTime[currentProcess[0]] -= 1
                self.time += 1
                
                if remainingTime[currentProcess[0]] == 0:
                    processCompleted += 1
                    rtValue = rt[currentProcess[0]]
                    tat = self.time - int(currentProcess[2]) 
                    wt = tat - int(currentProcess[1]) 
                    ct = self.time 
                    tempMatrix = [wt, ct, rtValue, tat]
                    
                    indice = self.instructions.index(currentProcess)
                    self.matrixStats[indice] = tempMatrix
                    
    def proms(self):
        wtProm = sum([i[0] for i in self.stats]) / len(self.stats)
        tatProm = sum([i[3] for i in self.stats]) / len(self.stats)
        ctProm = sum([i[1] for i in self.stats]) / len(self.stats)
        rtProm = sum([i[2] for i in self.stats]) / len(self.stats)
        print("WT: ", round(wtProm, 1), "\nCT: ", round(ctProm, 1), "\nRT: ",  round(rtProm, 1), "\nTAT: ",  round(tatProm, 1))

    def getStats(self):
        return self.matrixStats
