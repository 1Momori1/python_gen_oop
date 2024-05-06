import random

def shuffle_word(word):
    letters = list(word)  
    random.shuffle(letters) 
    return ''.join(letters)  

word = "пример"
shuffled_word = shuffle_word(word)
print(shuffled_word)
