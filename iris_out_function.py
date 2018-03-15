#   time:       2018-3-15
#   author:     songshu
#   function:   predict the class of the iris data according to the provied data
#   version:    Python: 3.6.1
#               scikit-learn: 0.18.1
import csv
import random
import math
import operator
from sklearn.metrics import accuracy_score

def transform_data(fileName, split, trainSet = [], testSet = []):
    with open(fileName, newline='') as csvfile:
        raw_data = csv.reader(csvfile, delimiter=',', quotechar='|')
        for data in raw_data:
            if random.random() < split:
                trainSet.append(data)
            else:
                testSet.append(data)

def get_distance(data_1 = [], data_2 = []):
    sum = 0
    for i in range(len(data_1)-1):
        sum += math.pow((float(data_1[i]) - float(data_2[i])), 2)
    return math.sqrt(sum)

def get_neighbor(k, trainSet=[], test_data=[], best_suitable=[]):
    tempSet = []
    for data in trainSet:
        # caculate the distance
        distance = get_distance(data, test_data)
        # add to the set
        tempSet.append((data, distance))
    # sort the set
    tempSet.sort(key=operator.itemgetter(1))
    # get the k set
    for i in range(k):
        best_suitable.append(tempSet[i][0])

def get_label(k, dataSet = []):
    sum = {}
    for data in dataSet:
        if data[-1] in sum:
            sum[data[-1]] = sum[data[-1]] + 1
        else:
            sum[data[-1]] = 1
    # find the max
    sum['songshu'] = 1
    temp = sum.items()
    temp = sorted(sum.items(), key=operator.itemgetter(1), reverse=True)
    return temp[0][0]

def main():
    print('main')
# prepare the data
    fileName = r'iris.data'
    trainSet = []
    testSet = []
    split = 0.67
    # transform the data file to the suitable data form
    transform_data(fileName, split, trainSet, testSet)
# generate predictions
    predictions = []
    label_list = []
    for test_data in testSet:
    # processing circulation from the first to the end
        # get the best suitable data
        best_suitable = []
        k = 3
        get_neighbor(k, trainSet, test_data, best_suitable)
        # caculate the predicted label
        temp = get_label(k, best_suitable)
        predictions.append(temp)
        label_list.append(test_data[-1])
    # caculate the accuracy of the prediction
    score = accuracy_score(predictions, label_list)
    print(score)
if __name__ == '__main__':
    main()