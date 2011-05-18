#-------------------------------------------------------------------------------
# Name:        Mapper
# Purpose:     Implementation of Map/Reduce Algorithm
#
# Author:      Carlos Balbuena
#
# Created:     17/05/2011
# Copyright:   Based On MichaelNoll Implementation
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import sys

# Lee entrada desde STDIN(Standard Input)
for line in sys.stdin:
    # Quitar espacios al comienzo y al final de la cadena
    line = line.strip()
    # Obtener todas las palabras
    words = line.split()
    # Escribe los resultados al STDOUT
    for word in words:
        print '%s\t%s' % (word, 1)