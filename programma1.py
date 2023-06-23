import sys
import nltk

def CalcoloStatistiche(frasi):
    numFrasi = 0 #inizializzo a 0
    numTokens = 0
    tokensTOT = []
    for frase in frasi: #per sapere quante sono le frasi
        #print(frase)
        tokens = nltk.word_tokenize(frase)
        #print(tokens)
        numFrasi+=1
        tokensTOT+=tokens #per avere tutti i tokens

    numTokens=len(tokensTOT)


    return numFrasi, numTokens, tokensTOT
    
def lungMediaFrasiEToken(numFrasi, tokensTOT):
    lungMediaFrasi = len(tokensTOT)/numFrasi
    lungTotToken = 0
    #calcola la lunghezza totale dei caratteri nei token,
    for token in tokensTOT:
        lungTotToken += len(token)
    lungMediaToken = lungTotToken/len(tokensTOT)

    return lungMediaFrasi, lungMediaToken
    
"""calcolate la grandezza del vocabolario e la ricchezza lessicale calcolata attraverso la Type Token Ratio
(TTR), in entrambi i casi calcolati nei primi 5000 token;"""
def lungVocabolarioETTR_5000(tokensTOT):
    #restituisce la lunghezza del vocabolario e la TTR per i primi 5000 token
    vocabolario5000 = list(set(tokensTOT[:5000]))
    lungVocabolario = len(vocabolario5000)
    TTR = lungVocabolario/5000

    return lungVocabolario, TTR


def main(file1, file2):
    fileInput1 = open(file1, mode="r", encoding="utf-8") #apertuta file1
    fileInput2 = open(file2, mode="r", encoding="utf-8") #apertura file2
    raw1 = fileInput1.read() #lettura file1
    raw2= fileInput2.read() #lettura file2
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') #divide il testo in inglese in frasi
   
    frasi1 = sent_tokenizer.tokenize(raw1)
    frasi2 = sent_tokenizer.tokenize(raw2)
    
    numfrasi1, numtokens1, tokens1 = CalcoloStatistiche(frasi1)
    numfrasi2, numtokens2, tokens2 = CalcoloStatistiche(frasi2)

    print("Programma 1 - Confrontate i due testi sulla base delle seguenti informazioni statistiche : ")
    print()
    print(" PRIMO PUNTO --> Il numero di frasi e di token : ")

    print()
    print("  - Il file " + file1 + " contiene " + str(numfrasi1) + " frasi" + " mentre il file " + file2 + " contiene " + str(numfrasi2) + " frasi.")

    print()
    print("  - Il file " + file1 + " contiene " + str(numtokens1) + " tokens" + " mentre il file " + file2 + " contiene " + str(numtokens2) + " tokens.")
    
    lungMediaFrasi1, lungMediaToken1 = lungMediaFrasiEToken(numFrasi1, tokensTOT1)
    lungMediaFrasi2, lungMediaToken2 = lungMediaFrasiEToken(numFrasi2, tokensTOT2)
    print("Nel primo testo, la lunghezza media delle frasi è pari a", lungMediaFrasi1, "token, mentre la lunghezza media dei token è pari a", lungMediaToken1, "caratteri.")
    print("Nel secondo testo, la lunghezza media delle frasi è pari a", lungMediaFrasi2, "token, mentre la lunghezza media dei token è pari a", lungMediaToken2, "caratteri.")
    print()
    
    lungVocabolario1_5000, TTR1 = lungVocabolarioETTR_5000(tokensTOT1)
    lungVocabolario2_5000, TTR2 = lungVocabolarioETTR_5000(tokensTOT2)
    print("Contando solo i primi 5000 token, il vocabolario del primo testo è lungo", lungVocabolario1_5000,
      "parole tipo, mentre la type-token ratio è pari a", TTR1, ".")
    print("Contando solo i primi 5000 token, il vocabolario del secondo testo è lungo", lungVocabolario2_5000,
      "parole tipo, mentre la type-token ratio è pari a", TTR2, ".")
    print()

      

main(sys.argv[1], sys.argv[2])
