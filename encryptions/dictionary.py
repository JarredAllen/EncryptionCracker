'''
The dictionary class, which handles verifying if something is a word, as well as how common the word is

@author: Jarred
'''

#from encryptions.base_class import base_class

supported_languages=['english']

list_of_english_words=[]
def build_list_of_english_words():
    if list_of_english_words:
        return list_of_english_words
    #note: this file just contains a list of all English words
    with open('words.txt') as f:
        for line in f:
            list_of_english_words.append(line.strip())
    return list_of_english_words

list_of_common_english_words=[]
def build_list_of_common_english_words():
    if list_of_common_english_words:
        return list_of_common_english_words
    #note: This file contains a list of common English words (top 10K-ish)
    with open('common_words.txt') as f:
        for line in f:
            list_of_common_english_words.append(line.strip())
    return list_of_common_english_words


class dictionary:
    def __init__(self, language='english'):
        """
        Constructor for dictionary objects.
        
        Has one optional argument for the language that it is to decrypt in. If unspecified or left as None, it defaults to English.
        """
        if language==None or language.lower()=='english':
            self.words=build_list_of_english_words()
            self.common_words=build_list_of_common_english_words()
        else:
            raise ValueError('Unrecognized or unsupported language')
    
    def get_words(self, reverse=False):
        if reverse:
            return self.reverse_words
        return self.words
    
    def get_common_words(self, reverse=False):
        if reverse:
            return self.reverse_common_words
        return self.common_words
    
    def is_word(self, word):
        return binary_search(word, self.words)
    
    def is_common_word(self, word):
        return binary_search(word, self.common_words)
    
    def get_score(self, word):
        word=word.strip()
        if self.is_common_word(word):
            return 2.
        if self.is_word(word):
            return 1.
        return -2


def binary_search(term, sequence):
    left=0
    right=len(sequence)
    index=(left+right)//2
    while left<right-1:
        if term==sequence[index]:
            return True
        elif term<sequence[index]:
            right=index
        else:
            left=index
        #print(sequence[index], left, right)
        index=(left+right)//2
    return term==sequence[left]

if __name__=='__main__':
    english=dictionary()
    print(english.get_score('g'))

"""
t=['a', 'b', 'c', 'd', 'f']
print(binary_search('a', t))
print(binary_search('b', t))
print(binary_search('c', t))
print(binary_search('d', t))
print(binary_search('e', t))
print(binary_search('f', t))
print(binary_search('ba', t))
"""
"""
def clear_dictionary_of_words_with_nonalphanumeric_characters():
    words=[]
    with open('common_words.txt') as f:
        for line in f:
            line=line.strip()
            if not contains_nonalpha(line) and len(line)>0:
                words.append(line)
    words.sort()
    content=''
    for word in words:
        content+=word+'\n'
    #print(words)
    #print(content)
    with open('common_words.txt', 'w') as f:
        f.write(content)
    

def contains_nonalpha(word):
    for i in word:
        if not i.isalpha():
            return True
    return False

clear_dictionary_of_words_with_nonalphanumeric_characters()"""
