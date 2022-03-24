import ReadingFile
import mainFunctions

def main(text1,text2,m,k):

    bloomFilterEmpty = mainFunctions.createEmptyBloomFilter(m)

    lst_texteOne  = ReadingFile.readingFile(text1)
    lst_texteTwo  = ReadingFile.readingFile(text2)
     
    bloomFilterFill =  mainFunctions.fillBloomFilter(k,lst_texteOne,bloomFilterEmpty,m)

    results = mainFunctions.compareFiles(k,lst_texteTwo,bloomFilterFill,m)

    return print(f"There are {results[1]} common words." )
# And here is the list {results[0]}

#texte_Shakespeare.txt

if __name__ == "__main__":
    main('texte_Shakespeare.txt','word2.txt',11194232,5)

#n = 235886
#p = 0.00001 (1 in 100000)
#m = 11194232 (1.33MiB)
#k = 5
# check here : https://hur.st/bloomfilter/?n=235886&p=0.00001&m=&k=5
