from nltk.util import ngrams
import re
import nltk.data
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle' 
tagger=nltk.data.load( _POS_TAGGER )


# open the file
f = open('input.txt')
text = f.read().strip()
f.close()

fileWriter = open('negations.txt', 'w')

#split sentences
sentences = re.split('[\.\n]', text)

# for each sentence
ifFirst = False
for sentence in sentences:
    if len(sentence.strip()) < 1:
        continue
    print sentence
    if ifFirst:
        fileWriter.write('\n')
    ifFirst = True

    adjectives = set()  # adjectives in this sentence

    sentence=re.sub('[^A-Za-z\d]', ' ', sentence)#replace chars that are not letters or numbers with a space
    sentence = re.sub(' +', ' ', sentence).strip()#remove duplicate spaces

    #tokenize the sentence
    term_orig = sentence.split()
    terms = sentence.lower().split();
    tagged_terms = tagger.tag(terms)  #do POS tagging on the tokenized sentence
    threegrams = ngrams(term_orig, 3)  # compute 3-grams

    for pair in tagged_terms:
        #if the word is an adjective
        if pair[1].startswith('JJ'):
            adjectives.add(pair[0])

    #for each 3gram
    flag = False
    spl_ex_fl = False
    for tg in threegrams:
        if spl_ex_fl:
            spl_ex_fl = False
            continue
        print tg
        ex_fl = False

        for i in range(2):
            if tg[i].lower().startswith('not'):
                for k in range(2 - i):
                    # print tg[i+k+1]
                    if tg[i+k+1].lower() in adjectives:
                        if flag:
                            fileWriter.write(',')
                        fileWriter.write(tg[i+k+1])
                        ex_fl = flag = True
                        if i > 0:
                            spl_ex_fl = True
                        break
            # if ex_fl: # this flag makes early exit if on pair in trigram is found otherwise two prints
            #     break

fileWriter.close()
