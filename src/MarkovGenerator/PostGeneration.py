from random import choice




#Cherche une autre phrase avec laquelle rhymer qui n'est pas non plus la phrase de départ
def rhymer(sentence, list_of_pregenerated_sentences):
    for s in list_of_pregenerated_sentences:
        if s[-4:] == sentence[-4:] and s != sentence and s.split(" ")[-1] != sentence.split(" ")[-1]:
            return s
    return -1

def generate2per2(numberOfLines, list_of_pregenerated_sentences):
    lres = []
    for i in range(numberOfLines):
        currentSentence = choice(list_of_pregenerated_sentences)
        while(currentSentence[-1:] != ","):
            currentSentence = choice(list_of_pregenerated_sentences)
        catchUp = rhymer(currentSentence, list_of_pregenerated_sentences)
        if catchUp != -1:
            lres.append(currentSentence)
            lres.append(catchUp)
    return lres
    
def run(numberOfLines, list_of_pregenerated_sentences):
        l = [str(s) for s in generate2per2(numberOfLines, list_of_pregenerated_sentences)]
        res = "\n".join(l)
        res = res.replace("^","")
        print(res)
        return res