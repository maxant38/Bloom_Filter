# Bloom_Filter

## But du TP :
implementer un filtre de Bloom culer approximativement l’intersection capable de caldes contenus de deux fichiers contenant des chaˆınes de caract`eres en anglais (codage ASCII).

## Binôme : 
Caille Maxence <br>
Courtois Justin

## Explications :
### Lancement : 
Le programme se lance depuis main.py en lançant la fonction main() avec les arguments suivants : main('texte_Shakespeare.txt','word2.txt',11194232,5)

### Première étape : 
On crée un filtre de bloom avec la fonction createEmptyBloomFilter() qui prend en paramètre la taille de notre filtre. 
Cette fonction renvoie un bitearray à 0 de la taille souhaitée.

### Deuxième étape :
On stocke les mots des fichiers à comparer dans deux listes distinctes grâce à la fonction readingFile() de readingFile.py.

### Troisième étape : 
On remplit le filtre de bloom avec le premier via fillBloomFilter(). On passe en paramètres nos deux listes ainsi que k=5, et une taille valant 235886
Cette fonction calcule le hash de chaque mot via 5 fonctions de hash différentes. A chaque résultat, la valeur du bite dans le bitearray passe à 1. 
Cette fonction retourne l'état actuel du filtre de Bloom. 

### Quatrième étape : 
On compare les textes via la fonction compareFiles pour obtenir les mots communs.
Cette fonction va, pour chaque fonction de hash, calculer le hash des mots du second fichier. Si ce hash corresspond à une valeur 1 dans notre filtre de Bloom,
on incrémente la valeur de 1. Si on arrive à 5 ici, notre nombre de fonction de hash, on est donc en présence d'un mot en commun et on ajoute ce mot à notre liste. 

Nous retournons cette liste et sa longueur. 