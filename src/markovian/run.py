import json
from Generation import * 
from MarkovWordTable import *

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