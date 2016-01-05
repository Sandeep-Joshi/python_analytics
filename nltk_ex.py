import nltk.data
from nltk.util import ngrams
from nltk.corpus import stopwords
import re


#read the input
# f=open('article.txt')
f=open('input.txt')
text=f.read().strip().lower()
f.close()

fileWriter = open('trigrams.txt', 'w')

#split sentences
sentences=re.split('\.', text)
# print 'NUMBER OF SENTENCES: '+ str(len(sentences))

# all2grams=set()

# for each sentence
for sentence in sentences:

    nouns=set()#adjectives in this sentence
    # adverbs=set()#adverbs in this sentences
    
    sentence=re.sub('[^a-z\d]',' ',sentence)#replace chars that are not letters or numbers with a space
    sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

    #tokenize the sentence
    terms = sentence.split()

    # remove stopwords
    # print terms
    # print len(terms)
    # terms = [word for word in terms if not word in stopwords.words('english')]
    # print len(terms)
    # print terms
    
    tagged_terms=nltk.pos_tag(terms)#do POS tagging on the tokenized sentence
    
    for pair in tagged_terms: 
        
        #if the word is a noun
        if pair[1].startswith('NN'):
            nouns.add(pair[0])

    threegrams = ngrams(terms, 3)  # compute 3-grams

    # print nouns
    
    #for each 3gram
    for tg in threegrams:
        sum = 0
        row = ''
        flag = True
        for i in range(3):
            # check for stop words
            if tg[i] in nouns:
                sum += 1
            if tg[i] in stopwords.words('english'):
                # print 'out', tg
                flag = False
                break

            row += tg[i] + ' '
        if sum >= 2 and flag:
            print sum, tg, row
            fileWriter.write(tg[0] + ' ' + tg[1] + ' ' + tg[2] + '\n')
            # fileWriter.write(row + '\n')

fileWriter.close()

