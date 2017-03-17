'''
Created on Mar 14, 2017

@author: Jarred
'''

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
        The score currently ranges between 0 and 2, but this range is subject to change. 
        """
        message=message.replace('_', ' ')
        if not ' ' in message:
            message=self.insert_spaces(message)
        validWords=0
        totalWords=0
        for word in message.split(' '):
            totalWords+=1
            validWords+=self.ref.get_score(word)
            #print(word+": "+str(ref.get_score(word)))
        return validWords/totalWords
        
        
    def insert_spaces(self, message):
        """
        This method will be used to insert spaces appropriately to try to make words. It is currently not implemented
        """
        return message
    
    def decrypt(self, message, *args):
        """Reverse the encryption of the message using the keys given in *args"""
        raise NotImplementedError
    
    def crack(self, mesage):
        """Guess at how to reverse the encryption of the message"""
        raise NotImplementedError
    
    def encrypt(self, message, *args):
        """Encrypt the message using the keys given in *args"""
        raise NotImplementedError
