
from WordLength import *
from Palindromes import *
import xml.etree.ElementTree as ET
from xml.dom.minidom import parse
import xml.dom.minidom
from nltk.corpus import udhr


#THIS FUNCTION TAKES A TEXT FILE AND RETURN A LIST OF TYPES
def extracTypes(file):
    typefile = open(file, "rt", encoding="utf-8")
    typefile = typefile.read()
    typefile = typefile.split()
    typefile = set(list(typefile))
    print(typefile)

#THIS FUNCTION PRODUCES A LIST OF DIPHTONGS AND RELATED FREQUENCY
def dittonghifr(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    dyphmap = {}
    if file == "latincorpus.txt":
        outfile = "dittonghilat.txt"
    elif file == "greekcorpus.txt":
        outfile = "dittonghigre.txt"
    elif file == "stringaoriginale.txt":
        outfile = "dittonghiorig.txt"
    elif file == "czc.txt":
        outfile = "dittonghiczc.txt"
    elif file == "hng.txt":
        outfile = "dittonghihng.txt"
    elif file == "bohemian.txt":
        outfile = "dittonghibohem.txt"
    else:
        outfile = "dittonghifrequency"+str(file).replace(".txt","")+".txt"
    for word in infile:
        i=0
        while i < len(word) - 1:
            dyph = word[i] + word[i+1]
            if dyph not in dyphmap:
                dyphmap.update({dyph: 1})
            else:
                dyphmap[dyph] += 1 
            i += 1
    dyphmap = dict(sorted(dyphmap.items(), key=lambda item: item[1]))
    print(dyphmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in dyphmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION GENERATES A DOCUMENT WHICH IS THE INPUT  BACKWARDS
def dokuback(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    outfile = "backwards"+str(file).replace(".txt","")+".txt"
    with open(outfile, "wt",  encoding="utf-8") as b: 
        b.write(infile[::-1])

#THIS FUNCTION RETURNS A BACKWARDS DIPHTONGS LIST OF FREQUENCIES -  THE FILE IS PROCESSED STARTING FROM THE BOTTOM

def dittonghifrback(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    dyphmap = {}
    if file == "latincorpus.txt":
        outfile = "dittonghilat.txt"
    elif file == "greekcorpus.txt":
        outfile = "dittonghigre.txt"
    elif file == "stringaoriginale.txt":
        outfile = "dittonghiorig.txt"
    elif file == "czc.txt":
        outfile = "dittonghiczc.txt"
    elif file == "hng.txt":
        outfile = "dittonghihng.txt"
    elif file == "bohemian.txt":
        outfile = "dittonghibohem.txt"
    else:
        outfile = "dittonghifrequency"+str(file).replace(".txt","")+".txt"
    for word in infile:
        i= len(word) - 1
        while i > 0:
            dyph = word[i] + word[i-1]
            if dyph not in dyphmap:
                dyphmap.update({dyph: 1})
            else:
                dyphmap[dyph] += 1 
            i -= 1
    dyphmap = dict(sorted(dyphmap.items(), key=lambda item: item[1]))
    print(dyphmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in dyphmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION TAKES A TEXT FILE AS INPUT AND OUTPUTS A LIST OF ALL DIPHTHONGS WITH THE WORD POSITION THEY APPEAR IN
def dittonghipos(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    dyphmap = {}
    if file == "latincorpus.txt":
        outfile = "dittonghilatpos.txt"
    elif file == "greekcorpus.txt":
        outfile = "dittonghigrepos.txt"
    else:
        outfile = "dittonghiorigpos.txt"
    for word in infile:
        i=0
        while i < len(word) - 1:
            dyph = word[i] + word[i+1]
            if dyph not in dyphmap:
                dyphmap.update({dyph: str(i) + '/' +  str(len(word) - 1)})
            else:
                dyphmap[dyph] =  str(dyphmap[dyph]) + '-' + str(i) + '/' +  str(len(word) - 1)
            i += 1
    #dyphmap = dict(sorted(dyphmap.items(), key=lambda item: item[1]))
    print(dyphmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in dyphmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION PRODUCES A LIST OF THRIPHTONGS AND RELATED FREQUENCY
def trittonghifr(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    triphmap = {}
    if file == "latincorpus.txt":
        outfile = "trittonghilat.txt"
    elif file == "greekcorpus.txt":
        outfile = "trittonghigre.txt"
    else:
        outfile = "trittonghifrequency"+str(file).replace(".txt","")+".txt"
    for word in infile:
        i=0
        while i < len(word) - 2:
            triph = word[i] + word[i+1] + word[i+2]
            if triph not in triphmap:
                triphmap.update({triph: 1})
            else:
                triphmap[triph] += 1 
            i += 1
    triphmap = dict(sorted(triphmap.items(), key=lambda item: item[1]))
    print(triphmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in triphmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION PRODUCES A LIST OF THRIPHTONGS AND RELATED FREQUENCY OF A FILE READ BACKWARDS

def trittonghifrback(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    triphmap = {}
    if file == "latincorpus.txt":
        outfile = "trittonghilat.txt"
    elif file == "greekcorpus.txt":
        outfile = "trittonghigre.txt"
    else:
        outfile = "trittonghifrequencyback"+str(file).replace(".txt","")+".txt"
    for word in infile:
        i=len(word) - 2
        while i > 0:
            triph = word[i] + word[i-1] + word[i-2]
            if triph not in triphmap:
                triphmap.update({triph: 1})
            else:
                triphmap[triph] += 1 
            i -= 1
    triphmap = dict(sorted(triphmap.items(), key=lambda item: item[1]))
    print(triphmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in triphmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION TAKES A TEXT FILE AS INPUT AND OUTPUTS A LIST OF ALL TRIPHTHONGS WITH THE WORD POSITION THEY APPEAR IN
def trittonghipos(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    tryphmap = {}
    if file == "latincorpus.txt":
        outfile = "trittonghilatpos.txt"
    elif file == "greekcorpus.txt":
        outfile = "trittonghigrepos.txt"
    else:
        outfile = "trittonghiorigpos.txt"
    for word in infile:
        i=0
        while i < len(word) - 2:
            tryph = word[i] + word[i+1] + word[i+2]
            if tryph not in tryphmap:
                tryphmap.update({tryph: str(i) + '/' +  str(len(word) - 1)})
            else:
                tryphmap[tryph] =  str(tryphmap[tryph]) + '-' + str(i) + '/' +  str(len(word) - 1)
            i += 1
    #dyphmap = dict(sorted(dyphmap.items(), key=lambda item: item[1]))
    print(tryphmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in tryphmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION TAKES A TEXT FILE AS INPUT AND OUTPUTS A LIST OF ALL SUFFIX TRIPHTHONGS 
def trittonghisuff(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    suffmap = {}
    if file == "latincorpus.txt":
        outfile = "trittonghilatsuff.txt"
    elif file == "greekcorpus.txt":
        outfile = "trittonghigresuff.txt"
    else:
        outfile = "trittonghiorigsuff.txt"
    for word in infile:
        leng = len(word)
        if leng > 2:
            suff = word[leng-1] + word[leng-2] + word[leng-3]
        #else:
            #suff = word
        if suff not in suffmap:
            suffmap.update({suff: 1})
        else:
            suffmap[suff] += 1 
    #dyphmap = dict(sorted(dyphmap.items(), key=lambda item: item[1]))
    print(suffmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in suffmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION TAKES A TEXT FILE AS INPUT AND OUTPUTS A LIST OF ALL PREFIX TRIPHTHONGS 
def trittonghipref(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    prefmap = {}
    if file == "latincorpus.txt":
        outfile = "trittonghilatpref.txt"
    elif file == "greekcorpus.txt":
        outfile = "trittonghigrepref.txt"
    else:
        outfile = "trittonghiorigpref.txt"
    for word in infile:
        if len(word)>2:
            pref = word[0] + word[1] + word[2]
        #else:
            #pref = word
        if pref not in prefmap:
            prefmap.update({pref: 1})
        else:
            prefmap[pref] += 1 
    #dyphmap = dict(sorted(dyphmap.items(), key=lambda item: item[1]))
    print(prefmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in prefmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION TAKES A TEXT FILE AS INPUT AND OUTPUTS A LIST OF ALL SUFFIX TRIPHTHONGS 
def dittonghisuff(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    suffmap = {}
    if file == "latincorpus.txt":
        outfile = "dittonghilatsuff.txt"
    elif file == "greekcorpus.txt":
        outfile = "dittonghigresuff.txt"
    else:
        outfile = "diittonghiorigsuff.txt"
    for word in infile:
        leng = len(word)
        if leng > 2:
            suff = word[leng-2] + word[leng-1]
        else:
            suff = word
        if suff not in suffmap:
            suffmap.update({suff: 1})
        else:
            suffmap[suff] += 1 
    suffmap = dict(sorted(suffmap.items(), key=lambda item: item[1]))
    print(suffmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in suffmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION TAKES A TEXT FILE AS INPUT AND OUTPUTS A LIST OF ALL PREFIX TRIPHTHONGS 
def dittonghipref(file):
    infile = open(file, "rt",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    prefmap = {}
    if file == "latincorpus.txt":
        outfile = "dittonghilatpref.txt"
    elif file == "greekcorpus.txt":
        outfile = "dittonghigrepref.txt"
    else:
        outfile = "dittonghiorigpref.txt"
    for word in infile:
        if len(word)>2:
            pref = word[0] + word[1] 
        else:
            pref = word
        if pref not in prefmap:
            prefmap.update({pref: 1})
        else:
            prefmap[pref] += 1 
    prefmap = dict(sorted(prefmap.items(), key=lambda item: item[1]))
    print(prefmap)

    with open(outfile, "wt",  encoding="utf-8") as f: 
        for key, value in prefmap.items(): 
            f.write('%s:%s\n' % (key, value))

#THIS FUNCTION BOILS DOWN ALL THE PREVIOUS FUNCTIONS TO A SINGLE ONE. THE AMOUNT OF CHARACTERS AND THE 
#POSITION SHALL BE INPUT AS PARAMETER AS WELL
#ASSIGN "n-x" TO THE POS PARAMETER, WHERE X IS AN INTEGER, IF YOU WANT TO START FROM THE ENDING POSITION: OF COURSE IN THIS CASE THE VALUE OF X MUST BE EQUAL OR BIGGER THAN THE VALUE OF CHARS
#ASSIGN -1 TO POS IF YOU DO NOT WANT TO START FROM A POSITION BUT YOU WANT THE LOOP PASSING THROUGH ALL WORDS
#FROM THE BEGINNING

def wordChunks(file, chars, pos :str): 
    infile = open(file, "r",  encoding="utf-8")
    infile = infile.read()
    infile = infile.split()
    chunkmap = {}
    outfile = "wordChunks.txt"
    for word in infile:
        if str(pos)[0] == "n":
            pos = str(len(word) - int(pos[-1]))
            pos = int(pos)
        if int(pos) >= 0:
            pos = int(pos)
            if len(word) > chars + pos:
                i = pos
                j = 1
                chunk = word[i]
                while j < chars:
                    #while i + chars < len(word):
                    chunk = chunk + word[i+1]
                    i += 1
                    j += 1
                if chunk not in chunkmap:
                    chunkmap.update({chunk: 1})
                else:
                    chunkmap[chunk] += 1
            else:
                continue
        else:
            if len(word)> chars - 1:
                chunk = word[0]
                z=1
                i =0
                while i < len(word) - chars:
                    while z < chars:
                        chunk = chunk + word[z]
                        z += 1
                    if chunk not in chunkmap:
                        chunkmap.update({chunk: 1})
                    else:
                        chunkmap[chunk] += 1
                    i+=1
               
    chunkmap = dict(sorted(chunkmap.items(), key=lambda item: item[1]))
    print(chunkmap)

    with open(outfile, "a",  encoding="utf-8") as f: 
        f.write('Chunks list of length ' + str(chars) + ' and position '+ str(pos) +'\n')
        for key, value in chunkmap.items(): 
            f.write('%s:%s\n' % (key, value))
    
#THIS FUNCTION LOOPS THROUGH A PARTICULAR WORD LIST SEEKING FOR A PATTERN. IT TAKES THE NUMBER OF CHRACTERS AND THE PATTERN AS PARAMETERS. 'K' means consonant, 'Y' vowel and 'U' all different letters
#TO BE FIXED AND UPDATED WITH COPTIC
def patternsearch(wordlength, corpus, pattern):
    wordlist = []
    wordlist = allwordslength(wordlength, corpus)
    global patternsearcht 
    patternsearcht = open("patternsearch.txt", "a",  encoding="utf-8")
    output = ""
    if corpus == "greekcorpus.txt" or corpus == "copticbible.txt":
        if pattern == 'KK':
            for word in list(wordlist):
                if re.search(r'([^αευιοηω])\1',word):   
                    output = output + " , " + str(word)
        elif pattern == 'YY':
            for word in list(wordlist):
                if re.match(r'([αευιοηω])\1',word):     
                    output = output + " , " + word
        elif pattern == 'U':
            for word in list(wordlist):
                if re.match(r'^(?:([Α-Ωα-ω])(?!.*\1))*$',word):    
                    output = output + " , " + word
        elif pattern == 'DEFED':
            for word in list(wordlist):
                if len(word) == 5 and isPalindrome(word):    #workaround for greek DEFED
                    output = output + " , " + word
        elif pattern == 'TOAT':
            for word in list(wordlist):
                if re.match(r'\b(?=.{4})(?=(?:[\u0370-\u03ff]))(.)(.)[\u0370-\u03ff]\1\b',word):    #deprecated
                    output = output + " , " + word
        elif pattern == 'RTOA':
            for word in list(wordlist):
                if re.match(r'[\u0370-\u03ff\t]{4}',word):    #workaround for greek RTOA
                    output = output + " , " + word
        print("List of all words with length " + str(wordlength) + " and pattern " + str(pattern) + ":\n" + output)
        patternsearcht.write("List of all words with length " + str(wordlength) + " and pattern " + str(pattern) + ":\n" + output + "\n")
    elif corpus == "latincorpus.txt":
        if pattern == 'KK':
            for word in list(wordlist):
                if re.search(r'([^aeiou])\1',word):   
                    output = output + " , " + str(word)
        elif pattern == 'YY':
            for word in list(wordlist):
                if re.match(r'([aeiou])\1',word):     
                    output = output + " , " + word
        elif pattern == 'U':
            for word in list(wordlist):
                if re.match(r'^(?:([A-Za-z])(?!.*\1))*$',word):    
                    output = output + " , " + word
        elif pattern == 'DEFED':
            for word in list(wordlist):
                if re.match(r'\b(?=.{5})(?=(?:[a-z]))(.)(.)[a-z]\2\1\b', word):    
                    output = output + " , " + word
        elif pattern == 'TOAT':
            for word in list(wordlist):
                if re.match(r'\b(?=.{4})(?=(?:[a-z]))(.)(.)[a-z]\1\b',word):    
                    output = output + " , " + word
        elif pattern == 'RTOA':
            for word in list(wordlist):
                if re.match(r'\b(?=.{4})(?=(?:[a-z]))(.)(.)[a-z]\b',word):    
                    output = output + " , " + word
        print("List of all words with length " + str(wordlength) + " and pattern " + str(pattern) + ":\n" + output)
        patternsearcht.write("List of all words with length " + str(wordlength) + " and pattern " + str(pattern) + ":\n" + output + "\n")
    #OUTPUT THE RESULTS TO A TXT FILE
    #output = output.split(',')
    #patternsearch = open("patternsearch.txt", "wt",  encoding="utf-8")
    #    #for each line in the input file
    #for word in output:
	   # #read replace the string and write to output file
    #    patternsearch.write(word + ' ')

    #patternsearcht.close()

#THIS FUNCTION TAKES A HTML/XML FILE AS INPUT AND PRODUCES A TEXT FILE AS OUTPUT WITHOUT TAGGING
def xmlParse(xmlfile):
    #tree = ET.parse(xmlfile)
    #root = tree.getroot()
    #path = r"C:\Users\Palma\Desktop\cantiere\epigrafesantamarialanova\epigraphsolver\"
    dom = xml.dom.minidom.parse(r"C:\Users\\Palma\\Desktop\\cantiere\\epigrafesantamarialanova\\epigraphsolver\\" + xmlfile)
    file = dom.documentElement
    seg = dom.getElementsByTagName("orth")
    file = open('copticlexicon.txt','w',  encoding="utf-8")
    for item in seg:
        sent = item.firstChild.data
        #print(sent,sep='')
        file.write(sent)

    file.close()



#LEXICAL VARIETY IN CORPUS
def typetokenratio(text):
    string = open(text, 'r',  encoding="utf-8")
    string = string.read()
    string = string.split()
    #typetokenratio = len(set(list(greek_corpus.words())[50:149]))/100
    typetokenratio = len(set(list(string)))/len(list(string))
    print("Types' amount:")
    print(len(set(list(string))))
    print("Tokens' amount:")
    print(len(list(string)))
    print("Type-token ratio:")
    print(typetokenratio) # ---> 0.85 on 100 words


#THIS FUNCTIONS PRODUCES A WORD LIST OF GIVEN LENGTH FROM A TEXT INPUT
def generateWords(text, length):
    string = open(text, 'r',  encoding="utf-8")
    string = string.read()
    output = open("generateWords"+str(length)+".txt", 'a',  encoding="utf-8")
    for char in string:
        i = 0
        word = ""
        while i < length:
            word += string[string.index(char)+i]
            i+=1
        output.write(word + "\n")
        string = string[1:]
        if len(string) < length:
            break
