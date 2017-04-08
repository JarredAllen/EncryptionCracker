'''
Created on Mar 14, 2017

@author: Jarred
'''
from encryptions.base_class import base_class
from encryptions.dictionary import dictionary

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
        return decrypt.replace('_', '')

    def crack(self, message):
        legitimacy=-99999999
        decrypt=''
        mode=0
        for i in range(1, len(message)):
            padding=(i-len(message)%i)%i
            paddedMessage=message+'_'*(padding)
            possible=self.decrypt(paddedMessage, i)
            score=self.get_validity(possible)
            if score>legitimacy:
                legitimacy=score
                decrypt=possible
                mode=i
                #if legitimacy>1.2:
                    #note: This can cause failures if the key length is close to the actual 
                    #return (decrypt, mode, legitimacy)
        return (decrypt, mode, legitimacy)
    
    def encrypt(self, message, length):
        padding=(length-len(message)%length)%length
        message+='_'*(padding)
        encrypt=''
        for i in range(len(message)//length):
            encrypt+=message[i::len(message)//length]
            #print(message[i::len(message)//length],end=' ')
        #print()
        return encrypt

if __name__=='__main__':
    pass    