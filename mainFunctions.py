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

def fillBloomFilter(numberOfHashFunctions,lst_file,bloomFilter,sizeFilter):

    hashFunctions = [le1_bon_hashage,le2_bon_hachage,el1_bon_hachage,co1_bon_hachage,co1_hachage_original] # list of hash function that can be used

    for i in range(0,numberOfHashFunctions): # For each hash function (depend on the number of hash function chose by the user )

        for element in lst_file:   

            index = (hashFunctions[i](element,sizeFilter)) # calculate the hash function of the word
            bloomFilter[index] = 1  # the result of the hash function is the index, and we replace the value 0 of this index by the value 1

    return bloomFilter

def compareFiles(numberOfHashFunctions,lst_file,bloomFilter,sizeFilter):


    lst_common_words = [] # list of common words between the two files

    hashFunctions = [le1_bon_hashage,le2_bon_hachage,el1_bon_hachage,co1_bon_hachage,co1_hachage_original] # list of hash function that can be used

        
    for element in lst_file: # for each word of the file

        count = 0

        for i in range(0,numberOfHashFunctions): # For the number of hash functions chose by the user

            index = (hashFunctions[i](element,sizeFilter)) # Calculate the hash function of the word
            

            if bloomFilter[index] == 1: # If the index value is 1, we add one to the counter
                count += 1

        if count == numberOfHashFunctions: # If at the end the valeu of the counter = number of hash functions used , this is a common word
            
             lst_common_words.append(element) # We add the common word to the list of common words


    return [lst_common_words,len(lst_common_words)] # return the number of common words and the list 

        







