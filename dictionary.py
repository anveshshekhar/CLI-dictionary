import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]);
    
        if (yn =="y"):
            return data[get_close_matches(w, data.keys())[0]];
        elif (yn =="n"):
         print("Did you mean %s instead? If not, we didn't get your entry: " % get_close_matches(w, data.keys())[1])
            
        
        

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
