from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()
print(knn)
iris = datasets.load_iris()

print(type(iris))
print(iris)


knn.fit(iris.data, iris.target)
predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print(predictedLabel)