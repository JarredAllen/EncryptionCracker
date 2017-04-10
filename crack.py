'''
Created on Mar 11, 2017

@author: Jarred
'''

from encryptions.dictionary import dictionary, supported_languages
from encryptions.caesar import caesar
from encryptions.affine import affine
from encryptions.scytale import scytale

from sys import argv

def main():
    mode=argv[1]
    
    if mode=='-encrypt':
    #If encrypting
        message=argv[2]
        cipher=argv[3]
        if cipher=='caesar':
            rot=int(argv[4])
            print(caesar(None).encrypt(message, rot))
        elif cipher=='affine':
            a=int(argv[4])
            b=int(argv[5])
            print(affine(None).encrypt(message, a, b))
        elif cipher=='scytale':
            key=int(argv[4])
            print(scytale(None).encrypt(message, key))
        else:
            raise ValueError('Unsupported cipher: ' + cipher)
        
    elif mode=='-decrypt':
    #If decrypting
        encrypted_text=argv[2]
        cipher=argv[3]
        language=None
        if argv.count('-language')>0:#determine if the user gave the language
            language=argv[1+argv.index('-language')]
        if cipher=='caesar':
            rot=None
            if argv.count('-args')>0:
                rot=int(argv[argv.index('-args')+1])
            if rot==None:
                if language==None:
                    message=''
                    legitimacy=-1
                    for language in supported_languages:
                        decr=caesar(dictionary(language))
                        trial=decr.crack(encrypted_text)
                        if trial[-1]>legitimacy:
                            message=trial[0]
                    print(message)
                else:
                    print(caesar(dictionary(language)).crack(encrypted_text)[0])
            else:
                print(caesar(None).decrypt(encrypted_text, rot)) 
        elif cipher=='affine':
            a=None
            b=None
            if argv.count('-args')>0:
                a=int(argv[argv.index('-args')+1])
                b=int(argv[argv.index('-args')+2])
            if a==None or b==None:
                if language==None:
                    message=''
                    legitimacy=-1
                    for language in supported_languages:
                        trial=affine(dictionary(language)).crack(encrypted_text)
                        if trial[-1]>legitimacy:
                            message=trial[0]
                    print(message)
                else:
                    print(affine(dictionary(language)).crack(encrypted_text)[0])
            else:
                print(affine(None).decrypt(encrypted_text, a, b))
        elif cipher=='scytale':
            key=None
            if argv.count('-args')>0:
                key=int(argv[argv.index('-args')+1])
            if key is None:
                if language is None:
                    message=''
                    legitimacy=-1
                    for language in supported_languages:
                        trial=scytale(dictionary(language)).crack(encrypted_text)
                        if trial[-1]>legitimacy:
                            message=trial[0]
                    print(message)
                else:
                    print(scytale(dictionary(language)).crack(message))
        else:
            raise ValueError('Unsupported cipher: ' + cipher)
    else:
    #The user gave an incorrect second option
        raise ValueError('Unsupported mode: ' + mode)


if __name__=='__main__':
    main()