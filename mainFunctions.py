from bitarray import bitarray
from hashFunctions import *
from ReadingFile import *
#786307
#n = 23000
#p = 0.00001 (1 in 100000)
#m = 3168072 (386.73KiB)
#k = 3

#sizeFilter =  3168072;

def createEmptyBloomFilter(sizeFilter=3168072):
 
    bloomFilter = bitarray(sizeFilter) # create a bittarray
    bloomFilter.setall(0)   # set all elements in a to 0
    return bloomFilter 

def fillBloomFilter(numberOfHashFunctions = 1,lst_file=[],sizeFilter=3168072,bloomFilter=None):

    hashFunctions = [le1_bon_hashage,le2_bon_hachage,el1_bon_hachage,co1_bon_hachage]

    for i in (0,numberOfHashFunctions-1):

        for element in lst_file:   

            index = (hashFunctions[i](element,sizeFilter))
            bloomFilter[index] = 1 

    return bloomFilter

def compareFiles(numberOfHashFunctions = 1,bloomFilter=None, lst_file=[],sizeFilter=3168072):

    lst_common_words = []

    hashFunctions = [le1_bon_hashage,le2_bon_hachage,el1_bon_hachage,co1_bon_hachage]

    for i in (0,numberOfHashFunctions-1):

        for element in lst_file:   

            index = (hashFunctions[i](element,sizeFilter))
            
            if bloomFilter[index] == 1:

                lst_common_words.append(element)


    return [lst_common_words,len(lst_common_words)]

        







