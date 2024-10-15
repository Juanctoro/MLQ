class SJF:

    def __init__(self) -> None:
        pass
        
    def execute(self, instruction, ct):
        self.matrixStats = []
        self.waitProces = []
        self.ct = ct
        self.instruction = instruction
        first = True
        for i in self.instruction: 
            if first:
                rt = self.ct
                wt = self.ct - int(i[2])
                self.ct = self.ct + int(i[1])
                tat = self.ct - int(i[2])
                tempMatrix = [tat, wt, self.ct, rt]
                self.matrixStats.append(tempMatrix)
                first = False
            else:
                self.waitProces.append(i)
                self.waitProces.sort(key=lambda x: (x[1]))
                
        for temp in self.waitProces:
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