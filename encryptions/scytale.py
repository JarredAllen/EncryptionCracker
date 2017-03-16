'''
Created on Mar 14, 2017

@author: Jarred
'''
from encryptions.base_class import base_class

class scytale(base_class):
    '''
    classdocs
    '''


    def __init__(self, dictionary):
        '''
        Constructor
        '''
        super(scytale, self).__init__(dictionary)
    
    def decrypt(self, message, length):
        width=len(message)//length
        decrypt=''
        for i in range(width):
            decrypt+=message[i::width]
            return decrypt

    def crack(self, message):
        legitimacy=-99999999
        decrypt=''
        mode=0
        for i in range(1, len(message)):
            possible=self.decrypt(message, i)
            if self.get_validity(possible)>legitimacy:
                legitimacy=self.get_validity(possible)
                decrypt=possible
                mode=i
        return (decrypt, mode, legitimacy)