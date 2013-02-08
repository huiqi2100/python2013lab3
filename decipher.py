# Filename: decipher.py
# Author: Koh Hui Qi
# Date Created: 8 Feb 2013

from collections import Counter

try:
    # open input file
    file = open("MYSTERY.IN", 'r')
    # open external file
    ext = open("OUTPUT.TXT", 'w')
    for line in file:
        for charac in line:
            # convert each character to unicode and shift it by x (-5)
            uni = ord(charac) - 5 
            # convert back to character
            letter = chr(uni)
            # output results to external file
            ext.write(letter)
    # close files
    ext.close()
    file.close()

    # open external file to read results
    filen = open("OUTPUT.TXT", 'r')
    for line in filen:
        para = line

    # append each word into paragraph list
    paralist = para.split(' ')


    # list of common words
    common = ['and', 'to', 'the', 'of', 'a', 'our', 'in', 'will', 'we', 'We',
              'for', 'as', 'is', 'on', 'are', 'growth', 'can']

    # find top 3 most frequent words that appear
    mostf = Counter(paralist).most_common(len(common)+3)
    for e in mostf:
        for w in common:
            if e == w:
                mostf.remove(e)

    print(mostf)
    # close external file
    filen.close()
    
except IOError:
    print("Error! Cannot read file MYSTERY.IN")
