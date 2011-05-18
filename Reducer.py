#-------------------------------------------------------------------------------
# Name:        Reducer
# Purpose:     Implementation of Map/Reduce Algorithm
#
# Author:      Carlos Balbuena
#
# Created:     17/05/2011
# Copyright:   Based On MichaelNoll Implementation
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from operator import itemgetter
import sys

word2count = {}

# La cadena de entrada se obtiene a traves de STDIN.
for line in sys.stdin:

    #Quitar espacios al comienzo y fin de la cadena.
    line = line.strip()

    #Parsear cadena
    word, count = line.split('\t', 1)
    try:
        #Obtener contador de palabra
        count = int(count)
        #Acumular contador de palabra en diccinario con la palabra (word) como key
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        pass

sorted_word2count= sorted(word2count.items(), key=itemgetter(0))

for word, count in sorted_word2count:
    print '%s\t%s' % (word, count)

