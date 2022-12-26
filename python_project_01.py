# first, we will get the string as input from the user which we want to convert into an acronym.
userInput = input("Enter the string: ")
#now we have to split the string provided by the user to get all the words provided.
# we will store the words in a list for further use. 
myList = userInput.split(" ")
finalResult = ""
#we get the first letter of each word to create the acronym.
for x in myList:
    finalResult+=x[0]
#finally we need to convert the acronym into the upper case.
#and print the acronym.
print("The acronym for the given string is:",(finalResult).upper())