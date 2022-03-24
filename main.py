import ReadingFile
import mainFunctions

def main(text1 = None, text2 = None, m=1, k=1):

    bloomFilterEmpty = mainFunctions.createEmptyBloomFilter(m)

    lst_texteOne  = ReadingFile.readingFile(text1)
    lst_texteTwo  = ReadingFile.readingFile(text2)

     
    bloomFilterFill =  mainFunctions.fillBloomFilter(k,lst_texteOne,m,bloomFilterEmpty)

    results = mainFunctions.compareFiles(k,bloomFilterFill,lst_texteTwo,m)

    return print("There are {results[1]} common words. And here is the list {results[0]}" )


if __name__ == "__main__":
    main()

