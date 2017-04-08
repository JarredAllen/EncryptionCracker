'''
Created on Mar 14, 2017

@author: Jarred
'''
from encryptions.base_class import base_class
from encryptions.dictionary import dictionary

coprime_with_alphabet_length=[1,3,5,7,9,11,15,17,19,21,23,25]

def modular_multiplicative_inverse(number, modulus):
    ans=1
    while (number*ans) % modulus != 1:
        ans+=1
    return ans

class affine(base_class):
    '''A class that handles encrypting, decrypting, and cracking affine encryption.'''


    def __init__(self, dictionary):
        super(affine, self).__init__(dictionary)
        #self.ref=dictionary
    
    def crack(self, message):
        legitimacy=-99999999
        decrypt=''
        mode=(-1,-1)
        for a in coprime_with_alphabet_length:
            for b in range(26):
                possible=self.decrypt(message, a, b)
                if self.get_validity(possible)>legitimacy:
                    legitimacy=self.get_validity(possible)
                    decrypt=possible
                    mode=(a,b)
                    if legitimacy>=1:
                        return (decrypt, mode[0], mode[1], legitimacy)
        return (decrypt, mode[0], mode[1], legitimacy)

    def decrypt(self, message, a, b):
        a=a%26
        b=b%26
        decrypt=''
        inv=modular_multiplicative_inverse(a,26)
        for i in message.lower():
            if i.isalpha():
                val=(inv*((ord(i)-ord('a'))-b))%26
                decrypt+=chr(val+ord('a'))
            else:
                decrypt+=i
        return decrypt

    def encrypt(self, message, a, b):
        a=a%26
        b=b%26
        encrypt=''
        for i in message.lower():
            if i.isalpha():
                encrypt+=chr(ord('a')+(a*(ord(i)-ord('a'))+b)%26)
            else:
                encrypt+=i
        return encrypt

ref=dictionary()
aff=affine(ref)