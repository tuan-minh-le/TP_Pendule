from Pendule_LE_Tuan_Minh_02102023 import words
from Pendule_LE_Tuan_Minh_02102023 import split
from Pendule_LE_Tuan_Minh_02102023 import hideletter
from Pendule_LE_Tuan_Minh_02102023 import appearance
from Pendule_LE_Tuan_Minh_02102023 import guess
from Pendule_LE_Tuan_Minh_02102023 import modifyguess
from Pendule_LE_Tuan_Minh_02102023 import openfile
from Pendule_LE_Tuan_Minh_02102023 import replay
from Pendule_LE_Tuan_Minh_02102023 import score


dicti = openfile()

def main() :
    answer = 'Y'
    scores = []
    while answer == 'Y' :
        chances = 8
        word = words(dicti)
        splitword = split(word)
        hiddenletters = hideletter(splitword)
        appearance(hiddenletters)
        while chances != 0 and "_" in hiddenletters :
            letter = guess(splitword,hiddenletters)
            if letter or letter == True :
                hiddenletters = modifyguess(splitword, hiddenletters, letter)
                appearance(hiddenletters)
            elif letter == False  :
                chances -= 1
                print("Wrong, you have ", chances, " chances left")
        if chances != 0 :
            print("Congrats")
            
        else :
            print("zuck")
        scores = score(scores, chances)
        answer = replay()
    print("Votre meilleur score est ", scores[0])
        
    


main()