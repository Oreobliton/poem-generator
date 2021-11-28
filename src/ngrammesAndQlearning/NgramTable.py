import json

class NgramTable:
    def __init__(self, filename, ngramSize):
        self.datafileName = filename     #Nom de la base de données à utiliser
        self.ngramSize = ngramSize
        self.transitionTable = dict()    #Dico de transitions "c1c2 -> int"

    def fileToList(self): 
        with open(self.datafileName) as f:
            #le ^ et $ permettront d'identifier le début et la fin d'un mot
            text = f.read()
            text = text.replace("  "," ")
            self.lines = text.split("\n")
            #enlever caractères vides
            res = []
            for l in self.lines:
                if l != "":
                    res.append(l)
            self.lines = res
            data = (
                text.replace("\n"," ").split(" ")
            )
        f.close
        self.dataList = data

    """
    Marque les mots afin de reconnaitre les débuts de phrase (Majuscule généralement)
    Et les fin de phrases(.)
    On ajoute une transition à ces caractères (^-> débuts) et (fin -> .)
    """
    def calculDebutEtFin(self):
        self.transitionTable["^"] = dict()
        for line in self.lines:
            words = line.split(" ")
            #Caractère en début
            startingNgram = words[:self.ngramSize]
            startingNgram = "%".join(startingNgram)
            if startingNgram not in self.transitionTable["^"] :
                self.transitionTable["^"][startingNgram] = 1
            else :
                self.transitionTable["^"][startingNgram] += 1

            #Caractère de fin
            endingNgram = words[-self.ngramSize:]
            endingNgram = "%".join(startingNgram)
            if endingNgram not in self.transitionTable :
                self.transitionTable[endingNgram] = {"#": 1}
            else :
                self.transitionTable[endingNgram]["#"] += 1


    def calculTransition(self, currentNgram,nextWord):
        #Since we can't use lists as keys of dictionnaries
        #I use the % char to separate the words
        currentNgram = "%".join(currentNgram) 
        if currentNgram not in self.transitionTable.keys() :
            newDict = {nextWord:1}
            self.transitionTable[currentNgram] = newDict
        else :
            if nextWord not in self.transitionTable[currentNgram]:
                self.transitionTable[currentNgram][nextWord] = 1
            else :
                self.transitionTable[currentNgram][nextWord] += 1
    

    def generateTable(self):
        #init avec le debut et la fin
        self.fileToList()                #Charges les données de la BDD correspondant à datafileName dans une liste
        self.calculDebutEtFin()

        sizeOfdataList = len(self.dataList) - self.ngramSize
        for i in range(sizeOfdataList):
            self.calculTransition(
                self.dataList[i:i+self.ngramSize],
                self.dataList[i + self.ngramSize]
            )

    def prettyPrint(self):
        for k in self.transitionTable.keys() :
            print(k + ":" +  str(self.transitionTable[k]))

    def getTransitionTable(self):
        return self.transitionTable
    
    def importTable(self, importedTableFilename):
        with open(importedTableFilename, "r") as read_file:
            table = json.load(read_file)
        self.transitionTable = table


    def dumpTable(self, filename="table_dump.json"):
        with open(filename, 'w', encoding='utf8') as f:
            f.write(json.dumps(self.transitionTable, ensure_ascii=False))
        f.close