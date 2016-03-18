from sklearn import svm
from sklearn import cross_validation
import pandas as pd
import numpy as np

if __name__ == "__main__":
	data = pd.read_csv("../data/data.csv", index_col="entity")
	columns = data.columns
	M = data.shape[0]
	msk = np.random.rand(M) < 0.8
	train = data[msk]
	test = data[~msk]
	
	#X = train[columns[5:]]
	#X_test = test[columns[5:]]
	X = data[columns[5:]]
	for i in range(5):
		#Y = train["label%d" % i]
		Y = data["label%d" % i]
		clf = svm.SVC()
		scores = cross_validation.cross_val_score(clf, X, Y, cv=5)
	
		#Y_test = clf.predict(X_test)
		#results = (Y_test == test["label%d" % i])
		#print 1.0*sum(results)/len(results)
		print scores.mean()
