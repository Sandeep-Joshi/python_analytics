"""
Using Logistic Regression to classify sentences into positive / negative
This script solves the assignment for Week 9 "Improving classification accuracy".

THERE ARE SEVERAL OTHER MODELS (i.e., CLASSIFIERS) THAT ACHIEVE AN ACCURACY SCORE OF > 60%

@author: george valkanas (gvalkana)
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        tokens=line.strip().split('\t')
        reviews.append(tokens[0].lower())    
        if ( len( tokens ) == 2):
          labels.append(int(tokens[1]))
        else:
          labels.append( 0 )
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('train.txt')
rev_test,labels_test=loadData('test.txt')

#Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)

#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

logreg = LogisticRegression()
logreg.fit( counts_train,labels_train )

#use the classifier to predict
fw = open( 'predictions.txt', 'w' )
predicted=logreg.predict(counts_test)
for i in predicted:
    fw.write( str(i) + '\n' )
fw.close()

#print the accuracy
print accuracy_score(predicted,labels_test)