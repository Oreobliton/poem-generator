data = open("Corpus_RAPFR_lower.txt").readlines()
lres = []
insideOne = False

for s in data:
    sentence = ""

    for c in s:
        if c == "[" or c == "(":
            insideOne = True
        
        if not insideOne:
            sentence += c
        
        if c == "]" or c == ")":
            insideOne = False


    lres.append(sentence)

print("starting wb")
f = open("Corpus_RAPFR_lower_cleaner.txt", "w")
for l in lres:
    f.write(l)
