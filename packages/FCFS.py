class FCFS:

    def __init__(self) -> None:
        pass
        
    def execute(self, instruction, ct):
        self.matrixStats = []
        self.ct = ct
        self.instruction = instruction
        
        for temp in self.instruction:
            rt = self.ct
            self.ct = self.ct + int(temp[1])
            tat = self.ct - int(temp[2]) 
            wt = tat - int(temp[1])
            tempMatrix = [wt, self.ct, rt, tat]
            self.matrixStats.append(tempMatrix)
        
    def proms(self):
        wtProm = sum([i[0] for i in self.stats]) / len(self.stats)
        tatProm = sum([i[3] for i in self.stats]) / len(self.stats)
        ctProm = sum([i[1] for i in self.stats]) / len(self.stats)
        rtProm = sum([i[2] for i in self.stats]) / len(self.stats)
        print("WT: ", round(wtProm, 1), "\nCT: ", round(ctProm, 1), "\nRT: ",  round(rtProm, 1), "\nTAT: ",  round(tatProm, 1))

    def getStats(self):
        return self.matrixStats