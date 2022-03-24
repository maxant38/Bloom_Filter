from bitarray import bitarray

#786307
#n = 23000
#p = 0.00001 (1 in 100000)
#m = 3168072 (386.73KiB)
#k = 3

size =  3168072; # taille de notre filtre de bloom
bloomFilter = bitarray(size)
bloomFilter.setall(0)            # set all elements in a to 0



