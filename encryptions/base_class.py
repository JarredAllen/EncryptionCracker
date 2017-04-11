'''
Created on Mar 14, 2017

@author: Jarred
'''
import re
from encryptions.dictionary import dictionary

class base_class:
    '''
    A base class that provides some common functionality to all classes for decrypting.
    
    Do note that it raises exceptions for some methods but defines get_validity and insert_spaces so those two are usable, but other methods need to be defined by the subclass
    '''


    def __init__(self, dictionary):
        '''
        The constructor for this class. Behavior is undefined if any superclass tries to extend it without calling this constructor
        
        The one argument is the dictionary that it should use to check if something is a word. If the dictionary is None, then some methods will not work.
        '''
        self.ref=dictionary
    
    
    def get_validity(self, message):
        """
        This method returns a floating-point number representing how likely it thinks that this is a valid and meaningful message.
        The score currently ranges between -2 and 2, but this range is subject to change. 
        """
        message=message.replace('_', ' ')
        validWords=0
        totalWords=0
        for word in message.split(' '):
            totalWords+=1
            validWords+=self.ref.get_score(word)
            #print(word+": "+str(ref.get_score(word)))
        return validWords/totalWords
    
    
    def decrypt(self, message, *args):
        """Reverse the encryption of the message using the keys given in *args"""
        raise NotImplementedError
    
    def crack(self, mesage):
        """Guess at how to reverse the encryption of the message"""
        raise NotImplementedError
    
    def encrypt(self, message, *args):
        """Encrypt the message using the keys given in *args"""
        raise NotImplementedError
    
    #Here come utilities that don't actually try to decode a message, but may be useful for determining what cipher was used.
    
    def index_of_coincidence(self, message, length=None):
        """
        This method calculates the index of coincidence for the given string.
        If the length is unspecified, then it defaults to checking it for the entire message, otherwise, it breaks the message into chunks and calculates it separately.
        
        Most useful for determining the length of the key in a Vigenere cipher.
        """
        message=re.sub('[^a-zA-Z]+', '', message)
        #print(message)
        if length is None:
            length=1
        cols=[]
        for i in range(length):
            cols.append(message[i::length])
        #print(cols)
        coin=0
        for col in cols:
            colcoin=0
            for i in col:
                colcoin+=col.count(i)-1
            colcoin/=len(col)*(len(col)-1)
            coin+=colcoin
        coin/=len(cols)
        return coin

if __name__=='__main__':
    b=base_class(dictionary())
    print(b.get_validity('inweaves nullity tscharik flyeater celestiality boastings tenebrosity duchan scattermouch gandermooner'))
