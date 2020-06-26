import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(word):
	word= word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys())) >0:
		yn=input( "did you mean %s instead ? Enter y if yes , or n if no." %get_close_matches(word,data.keys())[0])
		if yn == 'y':
			return data[get_close_matches(word,data.keys())[0]]
		elif yn == 'n':
			return none
	else:
		return "The word doesn't exist"
word = input("Enter the word>>")
print(translate(word))
