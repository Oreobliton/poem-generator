from random import choice
import sys
sys.path.insert(1, '/home/amarante/Bureau/Projets/fac/Tatia/projet-tatia/src/')
from env import *


GENERATED_TEXT = OUTPUT_FILENAME_NGRAM
SENTENCES = open(GENERATED_TEXT, "r").readlines()
SENTENCES = [s.strip() for s in SENTENCES]

#Cherche une autre phrase avec laquelle rhymer qui n'est pas non plus la phrase de départ
def rhymer(sentence):
    for s in SENTENCES:
        if s[-4:] == sentence[-4:] and s != sentence:
            #print("s : ",s[-4:])
            #print("sentence : ",sentence[-4:])
            return s
    return -1

def generate2per2(numberOfLines):
    lres = []
    for i in range(numberOfLines):
        currentSentence = choice(SENTENCES)
        while(currentSentence[-1:] != ","):
            currentSentence = choice(SENTENCES)
        catchUp = rhymer(currentSentence)
        if catchUp != -1:
            lres.append(currentSentence)
            lres.append(catchUp)
    return lres
    
def run(numberOfPoems):

    for poem in range(numberOfPoems):
        l = [str(s) for s in generate2per2(12)]
        print("\n".join(l))
        f = open(f"poems/rhymes-{poem}.txt","w")
        for i in l:
            f.write(i[2:])
            f.write("\n")
        f.close()

run(5)