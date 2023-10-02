from Pendule_LE_Tuan_Minh_02102023 import words
from Pendule_LE_Tuan_Minh_02102023 import split
from Pendule_LE_Tuan_Minh_02102023 import hideletter
from Pendule_LE_Tuan_Minh_02102023 import appearance
from Pendule_LE_Tuan_Minh_02102023 import guess
from Pendule_LE_Tuan_Minh_02102023 import modifyguess
from Pendule_LE_Tuan_Minh_02102023 import openfile

dicti = openfile()

def main() :
    chances = 8
    word = words(dicti)
    splitword = split(word)
    hiddenletters = hideletter(splitword)
    appearance(hiddenletters)
    while chances != 0 and "_" in hiddenletters :
        letter = guess(splitword)
        if letter :
            hiddenletters = modifyguess(splitword, hiddenletters, letter)
            appearance(hiddenletters)
        else :
            chances -= 1
            print("Wrong, you have ", chances, " chances left")
    if chances != 0 :
        print("Congrats")
    else :
        print("zuck")


main()