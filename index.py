import string 

def vigenere(inpx = str  , intx = str  , crypt = bool , space = '') -> str  : 
    if len(inpx) > len(intx) : 
        intx = intx * (len(inpx) // len(intx)) + intx[:(len(inpx) // len(intx))]
    if crypt == True : 
        return space.join([ string.ascii_lowercase[ (inp + int) % 26 ] for inp , int in zip([ string.ascii_letters.index(x) for x in inpx  ] , [string.ascii_letters.index(x) for x in intx])]) 
    if crypt == False : 
        return space.join([ string.ascii_lowercase[ (inp - int) % 26 ] for inp , int in zip([ string.ascii_letters.index(x) for x in inpx  ] , [string.ascii_letters.index(x) for x in intx])]) 


# True for crypt , False for decrypt 

print(vigenere('hicham' , 'rahab' , True))