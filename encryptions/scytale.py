'''
Created on Mar 14, 2017

@author: Jarred
'''
from encryptions.base_class import base_class

from math import ceil

class scytale(base_class):
    '''A class that handles encrypting, decrypting, and cracking scytale ciphers'''


    def __init__(self, dictionary):
        '''
        Creates a new scytale object
        
        The one argument is the dictionary that it needs to use
        '''
        super(scytale, self).__init__(dictionary)
    
    def decrypt(self, message, length):
        chunks=[]
        for i in range(0, len(message),length):
            chunks.append(message[i:i+length])
        decrypt=''
        #print(chunks)
        for i in range(length):
            for chunk in chunks:
                decrypt+=chunk[i]
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
    
    def encrypt(self, message, length):
        padding=(length-len(message)%length)%length
        message+='_'*(padding)
        encrypt=''
        for i in range(length+1):
            encrypt+=message[i::length+1]
        return encrypt

message='iamverybadlyhurthelp'
scy=scytale(None)
print(scy.decrypt(scy.encrypt(message, 5),5))
'''
for length in range(1,len(message)):
    if message != scy.decrypt(scy.encrypt(message, length), length).replace('_', ''):
        print(length, scy.decrypt(scy.encrypt(message, length), length))
print('Test done')
'''