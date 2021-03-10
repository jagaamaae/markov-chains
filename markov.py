"""Generate Markov text from text files."""
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
   
    data= open(file_path)#object
    data=data.read()#turned to a giant sting
    #lines = data.split()
    
    #for text_string in data:
    #   print(text_string)
    return data


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> 
        [None]
    """

    chains = {}#dict
    words = text_string.split()#list returned
    #words.append(None)
    #print(text_string)
    #print(words)
    
    for i in range(len(words)-2):# i is a counter
        key = ( words[i], words[i + 1] ) #words at 1, 2 at become keys as a tuple
        value = words[i + 2] #word 3 is a value if a list
        #.setdefault.creates with an empty list, then append to the empty list
        #if key not in chains:
        #    chains[key]=[]
        chains.setdefault(key, []).append(value)
        #chains[key].append(value)
        chains.setdefault(key, []).append(value)
        #chains[key].append(value)
    print(type(chains))
    return chains

import random

def make_text(chains):
    """Return text from chains."""
    #A link in our case is a key from our dictionary 
    # and a random word from the list of words that follow it. 
    #Put that link in some kind of container 
    # (the skeleton file suggests adding each word 
    # to a list and joining the list into a string at the end).
    #  Once we have our first link, we can add another to it, 
    # and we can repeat the following process to add more:
    # make a new key out of the second word in the first key and the random word you pulled out from the list of words
   #look up that new key in the dictionary, and pull a new random word out of the new list.
    key = choice(list(chains.keys()))#key is a list with all the random keys
    word = choice(chains[key]) #random choice of key from teh dict
    container = [key[0], key[1]] #container is a list and contains 1st or 2nd keys


    while word is not None:
        
        key = (key[1], word)#make a new key out of the second word in the first key and the random word 
        container. append(word)
        word = choice(chains[key]) # random word
        return ' '.join(container)
    
input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print(chains)
# Produce random text
random_text = make_text(chains)

print(random_text)
