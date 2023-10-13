from random import randint
import matplotlib.pyplot as plt



def rollADie(explosionArray):

    oneReroll = False
    
    roll = randint(1,10)
    if roll == 1 and oneReroll == False:
        oneReroll = True
        roll = randint(1,10)
    result = roll

    while roll in explosionArray:
        roll = randint(1,10)
        if roll == 1 and oneReroll == False:
            oneReroll = True
            roll = randint(1,10)
        result += roll

    return result

def add_text(screen, font, text, color, location):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(topleft = location)
        screen.blit(text_obj, text_rect)

def rollDiceGetMax(number, explosionArray):

    result = 0

    for i in range(number):
        roll = rollADie(explosionArray)
        if roll > result:
            result = roll

    

    return result


def rollDiceModified(number, explosionArray, bonus):

    result = rollDiceGetMax(number, explosionArray) + bonus
    return result



def getRollData(number, explosionArray, bonus, iterations, threshold):

    output = []

    for i in range(threshold+1):
        output.append(0)



    for i in range(iterations):
        result = rollDiceModified(number, explosionArray, bonus)
        result = min([result, threshold])
        output[int(result)] += 1

    plotBargraph(output, iterations)
    #return returns
    

def plotBargraph(rolls, iter):
    offset = 0
    while rolls[0] == 0:
        rolls.pop(0)
        offset += 1

    bins = []
    for i in range(len(rolls)):
        bins.append(i + offset)


    probabilities = [i / iter for i in rolls]

    plt.bar(bins, probabilities, edgecolor='black')
    plt.xlabel('Result')
    plt.ylabel('Probability')

    plt.show()

