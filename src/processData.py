import pandas as pd
import numpy as np

def loadData(file_name):
	infile = open(file_name)
	dataDict = {}
	featureSet = set()
	for line in infile.readlines():
		vec = line.strip().split('\t')
		if len(vec) == 1:
			continue
		dataDict[vec[0][28:]] = []
		for v in vec[1:]:
			featureSet.add(v[30:])
			dataDict[vec[0][28:]].append(v[30:])
	return dataDict, featureSet

if __name__ == "__main__":
	dict1, set1 = loadData("../data/comedianFeature.txt")
	dict2, set2 = loadData("../data/comicscreatorFeature.txt")
	dict3, set3 = loadData("../data/fashiondesignerFeature.txt")
	dict4, set4 = loadData("../data/painterFeature.txt")
	dict5, set5 = loadData("../data/photographerFeature.txt")
	dictList = [dict1, dict2, dict3, dict4, dict5]
	setList = [set1, set2, set3, set4, set5]
	featureSet = set()
	for i in range(5):
		featureSet.update(setList[i])
	entitySet = set()
	D = {}
	for d in dictList:
		entitySet.update(d.keys())
		D.update(d)
	index = list(entitySet)
	labelDict = {}
	for i in range(5):
		label = pd.Series([dictList[i].has_key(x) for x in index], index=index)
		labelDict["label%d" % i] = label
	for feature in featureSet:
		label = pd.Series([(feature in D[x]) for x in index], index=index)
		labelDict[feature] = label
	data = pd.DataFrame(labelDict)
	data.to_csv("../data/data.csv", index_label="entity")

