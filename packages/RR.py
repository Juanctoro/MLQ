class RR:

    def __init__(self, q):
        
        self.quantum = q
        self.time = 0

    def execute(self, instruction, ct):
        self.time = ct
        self.instruction = instruction
        self.matrixStats = [None for _ in range(len(self.instruction))]
        rt = {}
        remainingTime = {} 
        for i in self.instruction:

            remainingTime[i[0]] = int(i[1])
            rt[i[0]] = -1
        processCompleted = 0
        queue = self.instruction.copy()
        while processCompleted < len(self.instruction):
            for i in range(len(queue)):
                if i < len(queue):
                    currentProcess = queue[i]
                   
                if int(currentProcess[2]) <= self.time and remainingTime[currentProcess[0]] > 0:
                    
                    if (rt[currentProcess[0]] == -1):
                        rt[currentProcess[0]] = self.time

                    if remainingTime[currentProcess[0]] > self.quantum:
                        remainingTime[currentProcess[0]] -= self.quantum
                        self.time += self.quantum
                    else:
                        self.time += remainingTime[currentProcess[0]]
                        remainingTime[currentProcess[0]] = 0

                    if remainingTime[currentProcess[0]] == 0:
                        processCompleted += 1
                        rtValue = rt[currentProcess[0]]
                        tat = self.time - int(currentProcess[2]) 
                        wt = tat - int(currentProcess[1]) 
                        ct = self.time 
                        tempMatrix = [wt, ct, rtValue, tat]
                        
                        indice = self.instruction.index(currentProcess)
                        self.matrixStats[indice] = tempMatrix
                for j in queue:
                    if remainingTime[j[0]] == 0:
                        queue.remove(j)
                    
    def proms(self):
        wtProm = sum([i[0] for i in self.stats]) / len(self.stats)
        tatProm = sum([i[3] for i in self.stats]) / len(self.stats)
        ctProm = sum([i[1] for i in self.stats]) / len(self.stats)
        rtProm = sum([i[2] for i in self.stats]) / len(self.stats)
        print("WT: ", round(wtProm, 1), "\nCT: ", round(ctProm, 1), "\nRT: ",  round(rtProm, 1), "\nTAT: ",  round(tatProm, 1))

    def getStats(self):
        return self.matrixStats
