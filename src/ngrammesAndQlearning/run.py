import json
from Generation import * 
import sys
sys.path.insert(1, '/home/amarante/Bureau/Projets/fac/Tatia/projet-tatia/src/')
from env import *

NB_SENTENCES_TO_GENERATE = 20000
SENTENCE_LENGTH_LIMIT = 10
NGRAM_SIZE = 2
IMPORT_TABLE = False

def generateTable(imported = False, importedTableFilename = ""):
    n = NgramTable(CORPUS_FILENAME_LOWER, NGRAM_SIZE)

    if imported:
        n.importTable(importedTableFilename)
    else:
        n.generateTable()
        n.dumpTable()

    gen = NgramGenerator(n)
    return gen

gen = generateTable(IMPORT_TABLE, IMPORTED_TABLE_FILENAME_NGRAM) #will use pre-existing table
#gen = generateTable()  #will generate a new table
text = ""

for i in range(NB_SENTENCES_TO_GENERATE):
    text += gen.generationForNgrams(SENTENCE_LENGTH_LIMIT) + "\n"
f = open(OUTPUT_FILENAME_NGRAM,"w")
f.write(text)
f.close()