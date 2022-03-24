import ReadingFile
import mainFunctions

def main(text1,text2,m,k):

    bloomFilterEmpty = mainFunctions.createEmptyBloomFilter(m)

    lst_texteOne  = ReadingFile.readingFile(text1)
    lst_texteTwo  = ReadingFile.readingFile(text2)
     
    bloomFilterFill =  mainFunctions.fillBloomFilter(k,lst_texteOne,bloomFilterEmpty,m)

    print(bloomFilterFill)



    results = mainFunctions.compareFiles(k,lst_texteTwo,bloomFilterFill,m)

    return print(f"There are {results[1]} common words. And here is the list {results[0]}" )

#texte_Shakespeare.txt

if __name__ == "__main__":
    main('test.txt','text.txt',30,2)

