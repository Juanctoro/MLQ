import os

class READ_AND_WRITE:

    def __init__(self) -> None:
        pass

    #Lee el arhivo de texto y retorna la lista para la ejecucion
    def read(self, file):
            matrixInstruction = [] 
            with open(file, 'r') as archivo:
                for line in archivo:
                    if line.startswith('#') or not line:
                        continue
                    line = line.strip() 
                    parts = line.split('; ') 
                    newList = []
                    for i in parts:
                        newList.append(i)
                    matrixInstruction.append(newList)
                    newList = []
            return matrixInstruction
    
    #Asigna los procesos a cada fila
    def assignProcesses(self, processes):
        queue0 = []
        queue1 = []
        queue2 = []

        for process in processes:
            currentProcess = process

            if int(currentProcess[3]) == 1:
                queue0.append(process)
            elif int(currentProcess[3]) == 2:
                queue1.append(process)
            elif int(currentProcess[3]) == 3:
                queue2.append(process)
        
        return queue0, queue1, queue2
    
    # Escribe los archivos de salida como se indica en la guia
    def writeOuput(self, fileName, matrixInstruction, stats, averages):
        output  = 'output'
        outputPath = os.path.join(output, fileName)

        if not os.path.exists(output):
            os.makedirs(output)

        # Junta la matris de procesos con la matris que da la ajecucion
        processes = []
        for (label, bt, at, q, pr), (wt, ct, rt, tat) in zip(matrixInstruction, stats):
            processes.append({
                'label': label,
                'BT': bt,
                'AT': at,
                'Q': q,
                'Pr': pr,
                'WT': wt,
                'CT': ct,
                'RT': rt,
                'TAT': tat
            })

        #Crea el archivo y escribe lo indicado
        with open(outputPath, 'w') as file:

            #Cabeceras
            file.write("# archivo: {}\n".format(fileName))
            file.write("# etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT\n\n")

            #Procesos y tiempos 
            for process in processes:
                file.write("{}; {}; {}; {}; {}; {}; {}; {}; {}\n".format(
                    process['label'],
                    process['BT'],
                    process['AT'],
                    process['Q'],
                    process['Pr'],
                    process['WT'],
                    process['CT'],
                    process['RT'],
                    process['TAT']
                ))

            #Promedios de las ejecuciones
            file.write("\n")
            file.write("WT={:.1f}; CT={:.1f}; RT={:.1f}; TAT={:.1f};\n".format(
                averages['WT'],
                averages['CT'],
                averages['RT'],
                averages['TAT']
            ))
