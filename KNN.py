"""
A simple script that demonstrates how we classify textual data with sklearn.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import logistic_regression_path


# read the reviews and their polarities from a given file
def loadData(fname, ifTwo = True):
    reviews = []
    labels = []
    f = open(fname)
    for line in f:
        if ifTwo:
            review, rating = line.strip().split('\t')
            labels.append(int(rating))
        else:
            review = line.strip()
        reviews.append(review.lower())
    f.close()
    return reviews, labels

rev_train, labels_train = loadData('train.txt')
rev_test, labels_test = loadData('test.txt', False)

# Build a counter based on the training dataset
counter = CountVectorizer()
counter.fit(rev_train)

# count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)  # transform the training data
counts_test = counter.transform(rev_test)  # transform the testing data

# build a 3-NN classifier on the training data
KNN = KNeighborsClassifier(3)  # gives better prediction
KNN.fit(counts_train, labels_train)

# use the classifier to predict
predicted = KNN.predict(counts_test)

# print the accuracy
# print accuracy_score(predicted, labels_test)
# print predicted
# print predicted class types to a file
fileWriter = open('predictions.txt', 'w')
for pred in predicted:
    fileWriter.write(str(pred) + "\n")
