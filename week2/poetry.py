#poetry.py is a simple program designed to demonstrate string manipulation
import re #importing regular expressions

fox = "The quick brown fox jumps over the lazy dog." #an English pangram 
alice = "Alice\'s aunt ate apples and acorns around august" #alleteration phrase in English

def letterLoop(phrase): #defining a function to count the number of times 'a' shows up
	count = 0 #declaring a variable
	for x in phrase: # a shortened way of doing a loop. Note how "phrase" is a string, and python treats the string as an array
		if x == "a":
			count += 1
		#use print(x) for troubleshooting
	return count


def checkLength(phraseList): #this is a function to check the 
        longest = "" #declaring the 'longest string' variable
        for x in phraseList: #another loop
                if len(x) > len(longest):
                        longest = x
        return longest
                                  
        
'''
YOU COULD HAVE WRITTEN THE LOOP LIKE THIS:
	
def alternativeLoop(phrase): #defining a function to count the number of times 'a' shows up
	count = 0
	for x in phrase:
		if x = re.search(r ...
			count += 1
	return count

However, we don't know regex yet...
Can you think of ways we could have used .upper() or .lower()?
	
'''
phraseList = [fox, alice] #this is a list of the phrases

phrase = raw_input('Enter your phrase: ') #demonstrating the power of user input

phraseList.append(phrase) #appending the phrase you wrote to the list

foxCount = letterLoop(fox)
aliceCount = letterLoop(alice)
phraseCount = letterLoop(phrase)

print("The pangram has " + str(foxCount) + " iterations of \'a\'.") #print the outputs
print("The alleteration phrase has " + str(aliceCount) + " iterations of \'a\'.")
print("Your phrase has " + str(phraseCount) + " iterations of \'a\'.")
print("The longest phrase was \'" + str(checkLength(phraseList)) + "\'.")
#print("If we want to sound angry, we can write it like this: \'" + str(checkLength(phraseList)).upper() + "\'.")
