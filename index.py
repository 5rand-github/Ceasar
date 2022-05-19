import string 

# put True if you need to crypt and false for decrypt 

def ceasar (inpx , intx , encrypt = bool , space = ''  ) : 
    if encrypt : 
        return space.join([ string.ascii_letters[(string.ascii_letters.index(x) + intx ) % 26 ] for x in inpx])
    else : 
        return space.join([ string.ascii_letters[(string.ascii_letters.index(x) - intx ) % 26 ] for x in inpx])


# this function return the chipper key   
def chiperCeasar(inpx  = str ) : 
    return int(string.ascii_letters.index([ x for x in { x : inpx.count(x) for x in list(inpx)  }  if { x : inpx.count(x) for x in list(inpx)  } .get(x) == max({ x : inpx.count(x) for x in list(inpx)  }.values())][0])) - 4 


# put true if you need to crypt and false if you nedd to decrypt 

def vigenere(inpx = str  , intx = str  , crypt = bool , space = '') -> str  : 
    if len(inpx) > len(intx) : 
        intx = intx * (len(inpx) // len(intx)) + intx[:(len(inpx) // len(intx))]
    if crypt == True : 
        return space.join([ string.ascii_lowercase[ (inp + int) % 26 ] for inp , int in zip([ string.ascii_letters.index(x) for x in inpx  ] , [string.ascii_letters.index(x) for x in intx])]) 
    if crypt == False : 
        return space.join([ string.ascii_lowercase[ (inp - int) % 26 ] for inp , int in zip([ string.ascii_letters.index(x) for x in inpx  ] , [string.ascii_letters.index(x) for x in intx])])
    
# True to crypt  
print(vigenere('hicham' , 'rahab' , True))
# False to decrypt 
print(vigenere('yijhbd' , 'rahab' , False))
# True to crypt
print(ceasar('rahab' , 2 , True))
# False to decrypt 
print(ceasar('tcjcd' , 2 , False))
# Key of crypt 
print(chiperCeasar("tcjcd"))

