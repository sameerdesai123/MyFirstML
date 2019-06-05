from sklearn import tree
features = [[130,0], [120, 0], [150, 1], [180, 1], [140, 0]]
labels = ["Apple", "Apple", "Orange", "Orange", "Apple"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[190, 1]]))
