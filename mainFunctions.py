from bitarray import bitarray
from hashFunctions import *
from ReadingFile import *
#786307
#n = 23000
#p = 0.00001 (1 in 100000)
#m = 3168072 (386.73KiB)
#k = 3

#sizeFilter =  3168072;

def createEmptyBloomFilter(sizeFilter):
 
    bloomFilter = bitarray(sizeFilter) # create a bittarray
    bloomFilter.setall(0)   # set all elements in a to 0
    return bloomFilter 

def fillBloomFilter(numberOfHashFunctions,lst_file,bloomFilter,sizeFilter=3168072):

    hashFunctions = [le1_bon_hashage,le2_bon_hachage,el1_bon_hachage,co1_bon_hachage,co1_hachage_original]

    for i in range(0,numberOfHashFunctions):

        for element in lst_file:   

            index = (hashFunctions[i](element,sizeFilter))
            bloomFilter[index] = 1 

    return bloomFilter

def compareFiles(numberOfHashFunctions,lst_file,bloomFilter,sizeFilter=3168072):


    lst_common_words = []

    hashFunctions = [le1_bon_hashage,le2_bon_hachage,el1_bon_hachage,co1_bon_hachage,co1_hachage_original]

        
    for element in lst_file: 

        count = 0

        for i in range(0,numberOfHashFunctions):

            index = (hashFunctions[i](element,sizeFilter))
            

            if bloomFilter[index] == 1:
                count += 1

        if count == numberOfHashFunctions:
            
             lst_common_words.append(element)


    return [lst_common_words,len(lst_common_words)]

        







