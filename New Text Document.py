#programming language used python


#question :3

import enchant
stringX = input('Enter STRING X ')
stringS = input('Enter STRING S ')
print(enchant.utils.levenshtein(stringX, stringS))


#question:-1
inputArr= ['+91-9999999999', '0919999999999', '919999999999', '9999999999']
outArr = []
for i in inputArr:
  x = i[-10:]
  outArr.append(x)
print(outArr)


