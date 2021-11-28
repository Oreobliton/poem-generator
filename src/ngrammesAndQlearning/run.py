from Generation import * 
import sys
sys.path.insert(1, '/home/amarante/Bureau/Projets/fac/Tatia/projet-tatia/src/')
from env import *

NB_SENTENCES_TO_GENERATE = 200
SENTENCE_LENGTH_LIMIT = 15
NGRAM_SIZE = 2

n = NgramTable(CORPUS_FILENAME_LOWER, NGRAM_SIZE)
n.generateTable()
n.dumpTable()
gen = NgramGenerator(n)

text = ""
for i in range(NB_SENTENCES_TO_GENERATE):
    text += gen.generationForNgrams(SENTENCE_LENGTH_LIMIT) + "\n"
f = open(OUTPUT_FILENAME_NGRAM,"w")
f.write(text)
f.close()