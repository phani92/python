hindiToEngDict = {
  'Namaste' : "Hello",
  'Dhanyawad' : "Thank you",
  'Shukriya' : "Thank you",
  'Pyar' : "Love"
 }

print(hindiToEngDict)
print(hindiToEngDict.get('Namaste'))

dictToUpdate = {
  'Fakr' : "Self respect",
  'Ijjat' : "respect",
 }

hindiToEngDict.update(dictToUpdate)
print(hindiToEngDict)
