def readingFile(fichier):
    lst_file=[]
    f = open(fichier,'r')
    words = f.readlines()
    for i in range (0,len(words)):
        words[i] = words[i][:-1]
        lst_file.append(words[i])
    return lst_file