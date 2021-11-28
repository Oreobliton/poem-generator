from Generation import * 
from MarkovWordTable import *
import sys
sys.path.insert(1, '../')
from env import *

m = MarkovTable(INPUT_FILENAME)
m.generateTable()
m.dumpTable()
gen = MarkovianGenerator(m)
text = ""
for i in range(NB_SENTENCES_TO_GENERATE):
    text += gen.generation(500) + "\n"
f = open(OUTPUT_FILENAME_MARKOV,"w")
f.write(text)
f.close()