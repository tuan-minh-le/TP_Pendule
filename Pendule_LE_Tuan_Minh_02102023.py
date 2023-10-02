from random import randint
import json

def words(dict) :
    choose = dict[randint(0,len(dict)-1)]
    return choose 

def split(word):
    splitword = list(word)
    return splitword

def hideletter(splitword):
    hiddenletters = []
    for val in splitword :
        hiddenletters.append("_")
    hiddenletters[0] = splitword[0]
    return hiddenletters

def appearance(hiddenletters) :
    print(*hiddenletters)

def guess(splitword,hiddenletter):
    letter = input("What letter are you guessing ? : ")
    if letter in hiddenletter :
        print("You already guessed this letter")
        return True
    elif letter in splitword :
        return letter
    elif letter not in splitword :
        return False 

def modifyguess(splitword, hiddenletters, letter) :
    for ind,val in enumerate(splitword) :
        if val == letter :
            hiddenletters[ind] = val
    return hiddenletters 

def openfile():
    file = open('dictionnaire.json','r')
    contenu = file.read()
    list = json.loads(contenu)
    return list

def replay() :
    answer = input ("Do you want to play again (Y/N) ? : ")
    return answer

def score(scores, chances):
    scores.append(chances)
    scores.sort
    return(scores)