import json
from Generation import * 
import sys
sys.path.insert(1, '/home/amarante/Bureau/Projets/fac/Tatia/projet-tatia/src/')
from env import *

NB_SENTENCES_TO_GENERATE = 200
SENTENCE_LENGTH_LIMIT = 15
NGRAM_SIZE = 2
IMPORT_TABLE = True
IMPORTED_TABLE_FILENAME = "/home/amarante/Bureau/Projets/fac/Tatia/projet-tatia/src/ngrammesAndQlearning/table_dump.json"

def generateTable(imported = False, importedTableFilename = ""):
    n = NgramTable(CORPUS_FILENAME_LOWER, NGRAM_SIZE)

    if imported:
        n.importTable(importedTableFilename)
    else:
        n.generateTable()
        n.dumpTable()

    gen = NgramGenerator(n)
    return gen

gen = generateTable(IMPORT_TABLE, IMPORTED_TABLE_FILENAME) 
text = ""
for i in range(NB_SENTENCES_TO_GENERATE):
    text += gen.generationForNgrams(SENTENCE_LENGTH_LIMIT) + "\n"
f = open(OUTPUT_FILENAME_NGRAM,"w")
f.write(text)
f.close()