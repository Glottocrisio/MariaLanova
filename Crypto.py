shift = 1
#THIS SMALL FUNCTIONS PERFORMS A CESAR ATTACK ON THE ORIGINAL STRING FILE
def caesar(plainText, shift):
  plainText = open(plainText, "rt", encoding="utf-8")
  cipherText = ""
  plainText = plainText.read()
  for ch in str(plainText):
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print("Your " + "(Shift " + str(shift) + ") ciphertext is: ", cipherText + "\n")
  return cipherText

#while shift<27:
#    caesar("stringaoriginale.txt", shift)
#    shift +=1

#THIS SMALL FUNCTION REMOVES ALL SPACES IN AN INPUT TEXT OUTPUTTING THE TRIMMED STRING

def RemoveSpaces(epigraph):
    epigraph = open(epigraph, "rt", encoding="utf-8")
    epigraph = epigraph.read()
    trimmedString = epigraph.replace(' ', '').replace('\n','').replace('\t','')
    print(trimmedString)

#THIS SMALL FUNCTIONS CREATES A NEW STRING IN WHICH LETTERS ARE SKIPPED
def skipletters(skip, text):
    text = open(text, "rt", encoding="utf-8")
    text = text.read()
    out = ""
    count = 0
    for letter in text:
        count += 1
        if count == skip:
            out = out + letter
            count = 0
    out = out + "\n"
    print(out)


#THIS FUNCTION SORTS ALPHABETICALLY THE LETTERS OF ALL WORDS IN THE TEXT.
#THE AIM OF THIS OPERATION IS TO DETECT ANAGRAMS

def SortText(text):
    text = open(text, "rt", encoding="utf-8")
    #output file to write the result to
    sortedtext = open("sortedwords_anagram.txt", "wt",  encoding="utf-8")
    #sortedtextgr = open("sortedwords_anagramgreek.txt", "wt",  encoding="utf-8")
    text = text.read()
    sortedString = ""
    #wordarr = []
    #len2 = []
    #len3 = []
    #len4 = []
    #len5 = []
    #len6 = []
    #len7 = []
    #len8 = []
    #len9 = []
    #len10 = []
    #len11 = []
    #len12 = []
    #len13 = []
    #len14 = []
    #len15 = []
    #len16 = []
    #len17 = []
    #len18 = []
    #len19 = []
    text = text.split()
    for word in text:
        word = sorted(set(word))
        wordsort = ''.join(word)
        sortedString = sortedString + " " + wordsort
    sortedtext.write(sortedString)
    #for word in text:
    #    if len(word) == 2:
    #        len2.append(word)
    #    if len(word) == 3:
    #        len3.append(word)
    #    if len(word) == 4:
    #        len4.append(word)
    #    if len(word) == 5:
    #        len5.append(word)
    #    if len(word) == 6:
    #        len6.append(word)
    #    if len(word) == 7:
    #        len7.append(word)
    #    if len(word) == 8:
    #        len8.append(word)
    #    if len(word) == 9:
    #        len9.append(word)
    #    if len(word) == 10:
    #        len10.append(word)
    #    if len(word) == 11:
    #        len11.append(word)
    #    if len(word) == 12:
    #        len12.append(word)
    #    if len(word) == 13:
    #        len13.append(word)
    #    if len(word) == 14:
    #        len14.append(word)
    #    if len(word) == 15:
    #        len15.append(word)
    #    if len(word) == 16:
    #        len16.append(word)
    #    if len(word) == 17:
    #        len17.append(word)
    #    if len(word) == 18:
    #        len18.append(word)
    #    if len(word) == 19:
    #        len19.append(word)
    #print(len2)
    #print(len3)
    #print(len4)
    #print(len5)
    #print(len6)
    #print(len7)
    #print(len8)
    #print(len9)
    #print(len10)
    #print(len11)
    #print(len12)
    #print(len13)
    #print(len14)
    #print(len15)
    #print(len16)
    #print(len17)
    #print(len18)
    #print(len19)
    #text.close()
    sortedtext.close()
    print(sortedString)  

#THIS FUNCTION LOOPS THROUGH A TXT FILE TO FIND A WORD MATCHING WITH THE ONE INPUTTED WORD AS PARAMETER
#I.E.: WORD=POLO ___ FILE= BEBE; MARMELADE; MOUSE; POSTER; FATA ---> RESULT: FATA
def matchWord(word, file):
    m = open(file, "rt", encoding="utf-8")
    #output file to write the result to
    mw = open("matchWord.txt", "a",  encoding="utf-8")
    #mwf = open("matchWordFile.txt", "a")
    m = m.read().split()
    superword=""
    superwordfile = ""
    superchar = ['1','2','3','4','5','6','7','8','9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M']
    for char in word:
        superword = superword + superchar[list(word).index(char)]
    print(superword)
    #for each word in the input file
    for wort in m:
        for char in wort:
            superwordfile = superwordfile + superchar[list(wort).index(char)]
        with open("matchWordFile.txt", "a", encoding="utf-8") as mwf:
           mwf.write(superwordfile + '\t' + str(wort)  + '\n') #+ ' ' + wort 
        superwordfile = ""
    mwf = open("matchWordFile.txt", "rt", encoding="utf-8")
    mwf = mwf.read().split()
    for wort in mwf:
        if wort == superword:
            next_word = mwf[mwf.index(wort) + 1]
            mw.write(wort + '\t' + next_word + '\n')
            mwf.remove(wort)
    mw.close()
