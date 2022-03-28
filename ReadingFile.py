def readingFile(fichier):
    lst_file=[] # a list that countains the words of the file
    f = open(fichier,'r')
    words = f.readlines()
    for i in range (0,len(words)):
        words[i] = words[i][:-1] # we erase the useless caractere (/n i.e line break)
        lst_file.append(words[i])
    return lst_file