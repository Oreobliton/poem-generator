import json
class MarkovTable:
    def __init__(self, filename):
        self.datafileName = filename     #Nom de la base de données à utiliser
        self.fileToList()       #Charges les données de la BDD correspondant à datafileName dans une liste
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
            if words[0] not in self.transitionTable["^"] :
                self.transitionTable["^"][words[0]] = 1
            else :
                self.transitionTable["^"][words[0]] += 1
            #Caractère de fin
            if words[-1] not in self.transitionTable :
                self.transitionTable[words[-1]] = {"#": 1}
            else :
                self.transitionTable[words[-1]]["#"] += 1


    def calculTransition(self, currentWord,nextWord):
        if currentWord not in self.transitionTable.keys() :
            newDict = {nextWord:1}
            self.transitionTable[currentWord] = newDict
        else :
            if nextWord not in self.transitionTable[currentWord]:
                self.transitionTable[currentWord][nextWord] = 1
            else :
                self.transitionTable[currentWord][nextWord] += 1
    

    def generateTable(self):
        #init avec le debut et la fin
        self.calculDebutEtFin()
        for word in range(len(self.dataList)-1):
            self.calculTransition(self.dataList[word], self.dataList[word +1])

    def prettyPrint(self):
        for k in self.transitionTable.keys() :
            print(k + ":" +  str(self.transitionTable[k]))

    def getTransitionTable(self):
        return self.transitionTable

    def dumpTable(self, filename="dump.json"):
        with open(filename, 'w', encoding='utf8') as f:
            f.write(json.dumps(self.transitionTable, ensure_ascii=False))
        f.close
        