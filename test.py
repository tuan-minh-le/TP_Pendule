from Pendule_LE_Tuan_Minh_02102023 import words
from Pendule_LE_Tuan_Minh_02102023 import split
from Pendule_LE_Tuan_Minh_02102023 import hideletter
from Pendule_LE_Tuan_Minh_02102023 import appearance
from Pendule_LE_Tuan_Minh_02102023 import guess
from Pendule_LE_Tuan_Minh_02102023 import modifyguess


dict = ["balls"]

testword = print(words(dict))
testword = words(dict)
testsplit = print(split(testword))
testsplit = split(testword)
testhide = print(hideletter(testsplit))
testhide = hideletter(testsplit)
testappearance = appearance(testhide)
testmodify = print(modifyguess(testsplit,testhide,'b'))
