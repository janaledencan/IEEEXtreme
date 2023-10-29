import string
import itertools

def remove_punctuation(sentence):
    
    punctuations = string.punctuation
    translator = str.maketrans('', '', punctuations)
    sentence_without_punctuation = sentence.translate(translator)

    return sentence_without_punctuation
    

n = int(input())

for _ in range(n):
    secret_message = input()
    recipe = ''
    
    secret_to_recipe = {
    'A': 0 ,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0
}
    
    # Create an iterator that returns the characters from index 1 to the end of the string
    char_iter = itertools.islice(secret_message, 0, None)
    
    for char in char_iter:
        if char == 'a':
            secret_to_recipe['A']+=1
        if char == 'b':
            secret_to_recipe['B']+=1
        if char == 'c':
            secret_to_recipe['C']+=1
        if char == 'd':
            secret_to_recipe['D']+=1
        if char == 'e':
            secret_to_recipe['E']+=1    
        if char == 'f':
            secret_to_recipe['F']+=1
        if char == 'g':
            secret_to_recipe['G']+=1
            
    sorted_dict = dict(sorted(secret_to_recipe.items(), key=lambda item: item[1]))
    
    last_key = list(sorted_dict)[-1]
    
    if sorted_dict[last_key] >= 2:
        recipe+=last_key
            
    print(recipe)

