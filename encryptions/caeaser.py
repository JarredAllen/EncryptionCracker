'''
Created on Mar 14, 2017

@author: Jarred
'''
from encryptions.base_class import base_class

class caeasar(base_class):
    '''A class that handles encrypting, decrypting, and cracking caeasar ciphers.'''

    def __init__(self, dictionary):
        super(caeasar, self).__init__(dictionary)
    
    def crack(self, message):
        legitimacy=-99999999
        decrypt=''
        mode=-1
        for i in range(26):
            possible=self.decrypt(message, i)
            if self.get_validity(possible)>legitimacy:
                legitimacy=self.get_validity(possible)
                decrypt=possible
                mode=i
        return (decrypt, mode, legitimacy)

    def decrypt(self, message, rot):
        rot=rot%26
        decrypt=''
        for i in message:
            if i.isalpha():
                decrypt+=chr((ord(i.lower())-ord('a')-rot)%26+ord('a'))
            else:
                decrypt+=i
        return decrypt
    
    def encrypt(self, message, rot):
        rot=rot%26
        encrypt=''
        for i in message:
            if i.isalpha():
                encrypt+=chr((ord(i.lower())-ord('a')+rot)%26+ord('a'))
            else:
                encrypt+=i
        return encrypt