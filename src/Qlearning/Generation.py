from NgramTable import *
from nonUninformChoice import *

STARTING_WORD = "^"
ENDING_WORD = "#"

class NgramGenerator:

    def __init__(self,ngramTable):
        self.ngramTable = ngramTable.getTransitionTable()
        self.ngramSize = ngramTable.ngramSize
            
    def prochainMot(self, motCourrant):
        #simuler un choix aléatoire à probabilités non uniformes
        motsPossibles = self.ngramTable[motCourrant]
        return nonUniformChoice(motsPossibles)


    def generationForNgrams(self, sentence_length_limit):
        phrase = []
        sousPhraseActuelle = []
        motCourrant = STARTING_WORD
        for _i in range(sentence_length_limit):
            phrase += motCourrant
            try:
                if len(phrase)>= self.ngramSize:
                    sousPhraseActuelle = phrase[- self.ngramSize:]
                    sousPhraseActuelle = "%".join(sousPhraseActuelle)
                else:
                    sousPhraseActuelle = STARTING_WORD
                motCourrant = self.prochainMot(sousPhraseActuelle)
                motCourrant = motCourrant.split("%")
                if motCourrant == "":
                    break
            except KeyError:
                break
            if motCourrant == ENDING_WORD:
                break
        return " ".join(phrase)