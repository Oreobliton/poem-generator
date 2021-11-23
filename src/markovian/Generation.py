from MarkovWordTable import MarkovTable
import random 
from nonUninformChoice import *

INPUT_FILENAME = "Merge.txt"
OUTPUT_FILENAME = "sentence.txt"
NB_SENTENCES_TO_GENERATE = 300
STARTING_WORD = "^"
ENDING_WORD = "#"

class MarkovianGenerator:

    def __init__(self,markovTable):
        self.markovTable = markovTable.getTransitionTable()
            
    def prochainMot(self, motCourrant):
        #simuler un choix aléatoire à probabilité non uniformes
        #Pour l'instant on se contente d'un choix uniforme
        motsPossibles = self.markovTable[motCourrant]
        return nonUniformChoice(motsPossibles)

    def generation(self, n):
        phrase = ""
        #Remplacer le random start par un caractère de début/fin
        motCourrant = STARTING_WORD
        for i in range(n):
            phrase += motCourrant + " "
            try:
                motCourrant = self.prochainMot(motCourrant)
                if motCourrant == "":
                    break
            except KeyError:
                break
            if motCourrant == ENDING_WORD:
                break
        return phrase


#TODO nettoyer cette boucle elle est plutôt sale
m = MarkovTable(INPUT_FILENAME)
m.generateTable()
m.dumpTable()
gen = MarkovianGenerator(m)
text = ""
for i in range(NB_SENTENCES_TO_GENERATE):
    text += gen.generation(500) + "\n"
f = open(OUTPUT_FILENAME,"w")
f.write(text)
f.close()
