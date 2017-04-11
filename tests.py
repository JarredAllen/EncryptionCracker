'''
Created on Mar 14, 2017

@author: Jarred
'''
import unittest
from encryptions import *
from random import randrange, choice

class Test(unittest.TestCase):
    
    def test_affine(self):
        '''
        Tests the affine cipher for incorrect
        '''
        generator=generate_phrases()
        cipher=affine.affine(dictionary.dictionary())
        for i in range(100):
            message=generator.__next__()
            a=choice(affine.coprime_with_alphabet_length)
            b=randrange(26)
            encrypted_text=cipher.encrypt(message, a, b)
            res=cipher.crack(encrypted_text)
            self.assertEqual(message, res[0], message+'decrypted as '+res[0]+' with key '+str(a)+','+str(b)+' on trial #'+str(i+1))\
    
    def test_caeser(self):
        generator=generate_phrases()
        cipher=caesar.caesar(dictionary.dictionary())
        for i in range(100):
            message=generator.__next__()
            key=randrange(26)
            encrypted_text=cipher.encrypt(message, key)
            res=cipher.crack(encrypted_text)
            self.assertEqual(message, res[0], message+'decrypted as '+res[0]+' with key '+str(key)+' on trial #'+str(i+1))
    
    
    #Commented out because it does not work
    
    def test_scytale(self):
        generator=generate_phrases()
        cipher=scytale.scytale(dictionary.dictionary())
        for i in range(100):
            message=generator.__next__()
            key=randrange(2, 12)
            encrypted_text=cipher.encrypt(message, key)
            res=cipher.crack(encrypted_text)
            self.assertEqual(message, res[0], 'Modes: '+str(key)+' & '+message+' became '+str(res)+'\n'+str(i))

def generate_phrases(language='english', length=5):
    d=dictionary.dictionary(language)
    #yield 'the quick brown fox jumped over the lazy dog'
    while True:
        line=''
        for wordNumber in range(length):
            if randrange(2)==1:
                line+=choice(d.words)+' '
            else:
                line+=choice(d.common_words)+' '
        yield line.strip()
    #this line will never run, I included it to stop the compiler from yelling at me over unused values
    wordNumber+=1
    
if __name__ == "__main__":
    unittest.main()