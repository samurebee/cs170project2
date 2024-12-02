import random
import pandas as pd
import time

def inputFeatures(features, numOfFeatures):
    for i in range(0, numOfFeatures):
        features.append(i+1) #adding features 0 to numOfFeatures into features list

def printFeatures(features):
    for i in range(0,len(features)):
        print(features[i], sep = "", end="")
        if(i != len(features) - 1):
            print(",", sep = "", end="")

def printWarning(features, highestAccuracy):
    print("\n(Warning, Accuracy has decreased!)")
    print("Finished Search!! The best feature subset is {", end="")
    printFeatures(features)
    print("}, which has an accuracy of ", highestAccuracy, "%.\n", sep = "",)

def printBest(features, highestAccuracy):
    print("\n Feature Set {", end="")
    printFeatures(features)
    print("} was best, accuracy is ", highestAccuracy, "%.\n", sep = "",)

def forwardSelection(numOfFeatures):

    features = [] # list to know what features could be added
    highestAccuracy = round(random.random() * 100,1) # no features has highest accuracy so far.
    featuresWithHighestAccuracy = [] # when adding a feature the feature that gives the highest accuracy is added here
    accuracyFlag = 0 # used to see if the accuracy increases
    print("Using no features and \"random\" evaluation, I get an accuracy of ", highestAccuracy, "%.\n", sep = "")

    print("Beginning Search.\n")

    # add feature numbers here based on number of features chosen by user
    inputFeatures(features, numOfFeatures)

    # loop until there are no more features to add
    while(len(features) != 0):
        # loop until there are no more features to compare
        for i in range(0,len(features)):
            accuracy = round(random.random() * 100,1) # assign accuracy to feature or set of features
            print("Using feature(s) {", end ="")
            for j in range(0,len(featuresWithHighestAccuracy)):
                print(featuresWithHighestAccuracy[j], ",", sep = "", end="")
            print(features[i], "} accuracy is ", accuracy, "%.", sep = "")
            # checks if there is a set of features with a higher accuracy
            if(accuracy > highestAccuracy):
                feature = features[i]
                accuracyFlag = 1 # accuracy increased
                highestAccuracy = accuracy # modify highest accuracy
        # if accuracy does not increase finish the search
        if(accuracyFlag == 0):
            printWarning(featuresWithHighestAccuracy, highestAccuracy)
            break
        # if accuracy increases print set of features with highest accuracy so far and continue search
        else:
            features.remove(feature)
            featuresWithHighestAccuracy.append(feature)
            printBest(featuresWithHighestAccuracy, highestAccuracy)
            accuracyFlag = 0

def backwardSelection(numOfFeatures):

    highestAccuracy = round(random.random() * 100,1) 
    featuresWithHighestAccuracy = []
    accuracyFlag = 0
    print("Using all features and \"random\" evaluation, I get an accuracy of ", highestAccuracy, "%.\n", sep = "")

    print("Beginning Search.\n")

    # populate with all available features
    inputFeatures(featuresWithHighestAccuracy, numOfFeatures)

    while(len(featuresWithHighestAccuracy) != 0):
        # iterate through each feature to check accuracy without it
        for i in range(0,len(featuresWithHighestAccuracy)):
            accuracy = round(random.random() * 100,1) 
            print("Removing feature", featuresWithHighestAccuracy[i])
            print("Using feature(s) {", end ="")
            # display remaining features
            for j in range(0,len(featuresWithHighestAccuracy)):
                if (i != j):
                    print(featuresWithHighestAccuracy[j], sep = "", end="")
                    if(i == len(featuresWithHighestAccuracy) - 1 and j == len(featuresWithHighestAccuracy) - 2):
                        break
                    if(j != len(featuresWithHighestAccuracy) - 1):
                        print(",", sep = "", end="")
            print("} accuracy is ", accuracy, "%.", sep = "")
            # check if config has higher accuracy than previous best
            if(accuracy > highestAccuracy):
                feature = featuresWithHighestAccuracy[i]
                accuracyFlag = 1
                highestAccuracy = accuracy
        # if no better accuracy print warning and stop search
        if(accuracyFlag == 0):
            printWarning(featuresWithHighestAccuracy, highestAccuracy)
            break
        else:
            featuresWithHighestAccuracy.remove(feature)
            printBest(featuresWithHighestAccuracy, highestAccuracy)
            accuracyFlag = 0

def calculateEuclideanDistance(features, test, train):
    distance = 0
    if(isinstance(features,int)):
        for i in range(0,features):
            distance += (test[i+1] - train[i+1]) ** 2
    else:
        for i in range(0,len(features)):
            distance += (test[features[i]] - train[features[i]]) ** 2
    return distance ** 0.5

def getData(userInput):
    df = pd.read_csv(userInput, sep="\s+", header = None)
    df_normalized = df.copy()
    startTime = time.time()
    for column in df_normalized:
        if (column != 0):
            df_normalized[column] = (df[column] - df[column].mean()) / df[column].std()
    endTime = time.time()
    print("Time to normalize data:", round(endTime-startTime,2), "seconds")
    return df_normalized

def NNClassifier(featuresToUse, userInput):
    accuracy = 0
    count = 0
    nearestNeighbor = 0
    lowestDistance = 0
    df_normalized = getData(userInput)
    if(isinstance(featuresToUse,str)):
        print("Using all features in", userInput)
    elif((isinstance(featuresToUse,list)) and len(featuresToUse) == 0):
        print("Using no features in", userInput)
    else:
        print("Using features [", end="")
        printFeatures(featuresToUse)
        print("] in", userInput)
    startTime = time.time()
    for i in range(0,df_normalized.shape[0]):
        if((isinstance(featuresToUse,list)) and len(featuresToUse) == 0):
            break
        flag = 0
        test = df_normalized.loc[i]
        for j in range(0,df_normalized.shape[0]):
            train = df_normalized.loc[j]
            if (i != j):
                if(isinstance(featuresToUse,str)):
                    distance = calculateEuclideanDistance(df_normalized.shape[1]-1, test, train)
                else:
                    distance = calculateEuclideanDistance(featuresToUse, test, train)
                if (flag == 0):
                    nearestNeighbor = j
                    lowestDistance = distance
                    flag = 1
                if(distance < lowestDistance):
                    nearestNeighbor = j
                    lowestDistance = distance
        if (test[0] == df_normalized.loc[nearestNeighbor][0]):
            count += 1
    accuracy = (count/df_normalized.shape[0]) * 100
    endTime = time.time()
    print("Time to calculate accuracy:", round(endTime-startTime,2), "seconds")
    print("Accuracy: ", accuracy, "%", sep="")