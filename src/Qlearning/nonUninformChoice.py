import random

def frequency_list_builder(dico: dict()) -> tuple:
    frequency_tuple_list = list()
    current_frequency = 0
    for key in dico.keys():
        frequency_tuple_list.append((key, current_frequency + dico[key]))
        current_frequency += dico[key]
    return (frequency_tuple_list, current_frequency)

def pick_elem_from_frequency_list(elemNumber: int, frequencylist: list) -> list:
    if elemNumber < frequencylist[0][1]:
        return frequencylist[0][0]
    if elemNumber == frequencylist[-1][1]:
        return frequencylist[-1][0]
    for tuple in range(len(frequencylist)-1):
        if (elemNumber >= frequencylist[tuple][1] and
        elemNumber < frequencylist[tuple+1][1]):
            return frequencylist[tuple+1][0]
            
def nonUniformChoice(dico: dict) -> str:
    """Renvois un mot du dictionnaire 

    Cette fonction selectionne un mot de manière aléatoire non-uniforme
    dans un dictionnaire de couple (mot : occurences)
    """
    (frequency_tuple_list, cumulated_frequency) = frequency_list_builder(dico)
    choice = random.randint(0, cumulated_frequency)
    return pick_elem_from_frequency_list(choice, frequency_tuple_list)