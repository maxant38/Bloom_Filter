import ReadingFile
import mainFunctions

def main(text1,text2,m,k):

    bloomFilterEmpty = mainFunctions.createEmptyBloomFilter(m) # We create the bloom filter

    lst_texteOne  = ReadingFile.readingFile(text1) # put words of the file one in a list 
    lst_texteTwo  = ReadingFile.readingFile(text2) # put words of the file two in a list 
     
    bloomFilterFill =  mainFunctions.fillBloomFilter(k,lst_texteOne,bloomFilterEmpty,m) # Fill the bloom filter with the words of the file one

    results = mainFunctions.compareFiles(k,lst_texteTwo,bloomFilterFill,m) # Use the "filled bloom filter" to find the common words

    return print(f"There are {results[1]} common words. And here is the list {results[0]}" ) # Display the result



if __name__ == "__main__":
    main('texte_Shakespeare.txt','word2.txt',11194232,5)

# for these files  
#n = 235886
#p = 0.00001 (1 in 100000)
#m = 11194232 (1.33MiB)
#k = 5
# Website for choosing the parameters : https://hur.st/bloomfilter/?n=235886&p=0.00001&m=&k=5
