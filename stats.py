#Function to import book as input fp
import sys

def acceptInput():
    print("Usage: python3 main.py <path_to_book>")

    if len(sys.argv) == 1:
        print("\nERROR: Book not detected")
        sys.exit(1)
    
    else:
        booktitle = sys.argv[1]
    
    return booktitle
    

def get_book_text():
    path = acceptInput()
    with open(str(path)) as f:
        file_contents = f.read()

    return file_contents

#Splits imported book into a list of words. Returns length of list. 
def character_count():
    wordCnt = get_book_text().split()

    return f"Found {len(wordCnt)} total words"

#Returns dictionary of number of characters per unique character
def word_count():
    num_characters = {}
    num_words = (get_book_text().lower()) #makes all characters lower case to avoid duplicates
    
    #Add individual characters keys to the dictionary. Set all values equal to 0. 
    #Any value would work since values can be reassigned. Set to 0 for common sense reasons
    for word in num_words:
        num_characters[str(word)] = 0

    #Per key, counts each occurence in the book and appends the total as the value. 
    #Begins by cycling through each individual key
    for k in num_characters.keys():
        count = 0  
        #Checks each letter for matches in the boos. Adds count for each occurrence
        for word in num_words:
            if str(k) == word:
                count += 1
        num_characters[k] = count

    return num_characters

    #print (len(word_counts))
    #print(num_characters)

def sort_on(items):
    return items["num"]

#creates list of indiviudal dictionaries
def sort_book():
    dict = word_count()         #import dictionary of all words
    listDict = []               #creattes list to hold individual dictionaries
    Word_detail = {}        
    for k, v in dict.items():   #Per key and value, creates individual dictionary and adds to list
        Word_detail = {"name": k, "num": int(v)}
        listDict.append(Word_detail)
    listDict.sort(reverse=True, key=sort_on) 

    #print formatted list string
    
    print(character_count())
    
    for l in listDict:
        print(f"{l['name']}: {l['num']}")


