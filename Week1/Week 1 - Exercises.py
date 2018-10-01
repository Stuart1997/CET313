#Exercise 4.1
#Create Python code to convert temperature between Farenheit and Centigrade:
def celsiusToFahrenheit(celsiusParam):
    result = (celsiusParam * 1.8) + 32
    return print(result)

def fahrenheitToCelsius(fahrenheitParam):
    result = (fahrenheitParam - 32) / 1.8
    return print(result)
    
celsiusToFahrenheit(25)
fahrenheitToCelsius(77)


#Exercise 4.2
#Create a program to average any number of numbers. You will need to use a loop like:
numberArray = [1,2,3,12,15,26,30,50]
arrayLength = len(numberArray)
cumulative = 0;

for index in numberArray:
    cumulative += index

average = cumulative / arrayLength
print(average)


#Exercise 4.3a
#Use lists, dictionaries etc. to create Python data structures:
#Instantiating a dictionary
personInfoDict = {}
personInfoDict[0] = {"Name": "Sue", "Age" : 21, "Height" : 160, "Gender" : 'F'}
print(personInfoDict[0])

#Zipping two arrays to make a dictionary
personInfoHeadings = ["Name", "Age", "Height", "Gender"]
personInfoValues = ["Sue", 21, 160, 'F']
personInfo = zip(personInfoHeadings, personInfoValues)
print(dict(personInfo))


#Exercise 4.3b:
#David - boss of Ken and Nick, has staff
#Nick - has a department
#Ken - has a department
#Department - has staff


#Plurals Exercise
#Try to write general rules for pluralisation in Python. Main rules: vowel change: man -> men, -f +ves: shelf -> shelves, consonant -y + ies: lady -> ladies, o/ss/ch/x + es: box -> boxes
def pluralise(word):
    endsWithMan = word.endswith("man")
    endsWithF = word.endswith("f")
    endsWithY = word.endswith("y")
    endsWithO = word.endswith("o")
    endsWithSs = word.endswith("ss")
    endsWithCh = word.endswith("ch")
    endsWithX = word.endswith("x")
    
    if (endsWithMan):
        split = word.rsplit('man', 1) #Last occurrence of 'man' in case the word contains more than one
        firstHalfSplit = split[0]
        pluralised = firstHalfSplit + "men"
        return pluralised
    
    elif (endsWithF):
        print("ends with f")
        split = word.rsplit('f', 1) #Last occurrence of 'f' in case the word contains more than one
        print(split)
        firstHalfSplit = split[0]
        print(firstHalfSplit)
        pluralised = firstHalfSplit + "ves"
        return pluralised
    
    elif (endsWithY):
        split = word.rsplit('y', 1) #Last occurrence of 'y' in case the word contains more than one
        firstHalfSplit = split[0]
        pluralised = firstHalfSplit + "ies"
        return pluralised
    
    elif (endsWithO or endsWithSs or endsWithCh or endsWithX):
        pluralised = word + "es"
        return pluralised

toPluralise = "church"
print(pluralise(toPluralise))