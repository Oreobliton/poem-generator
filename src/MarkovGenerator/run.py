import json
from Generation import * 
from PostGeneration import *


##########################Configurer ici
GENERATING = False
NB_SENTENCES_TO_GENERATE = 20000
MAKING_RHYMES = True
SENTENCE_LENGTH_LIMIT = 12
NGRAM_SIZE = 2
POEM_LINES_NB = 7
IMPORT_TABLE = False
IMPORTED_TABLE_FILENAME = ""
CORPUS_PATH = "../../data/Corpus_POETRY.txt"
OUTPUT_PREGEN_FILENAME = "../../out/ngram-pregen-out.txt"
OUTPUT_FINAL_FILENAME = "../../out/ngram-postgen-out.txt"
###########################


def generateTable(imported=False, importedTableFilename=""):
    n = NgramTable(CORPUS_PATH, NGRAM_SIZE)

    if imported:
        n.importTable(importedTableFilename)
    else:
        n.generateTable()
        n.dumpTable()
        print("---- New Table generated !")

    gen = NgramGenerator(n)
    return gen

gen = generateTable(IMPORT_TABLE, IMPORTED_TABLE_FILENAME) #will use pre-existing table
text = ""

if GENERATING :
    for i in range(NB_SENTENCES_TO_GENERATE):
        text += gen.generationForNgrams(SENTENCE_LENGTH_LIMIT) + "\n"
    f = open(OUTPUT_PREGEN_FILENAME,"w")
    f.write(text)
    f.close()

if MAKING_RHYMES:
    list_of_pregenerated_sentences = open(OUTPUT_PREGEN_FILENAME, "r").readlines()
    list_of_pregenerated_sentences = [s.strip() for s in list_of_pregenerated_sentences]
    text = run(POEM_LINES_NB, list_of_pregenerated_sentences)
    f = open(OUTPUT_FINAL_FILENAME, "w")
    f.write(text)
    f.close()
