import pandas as pd
import time
import numpy as np


# def inputFeatures(features, numOfFeatures):
#     for i in range(1, numOfFeatures + 1):  # Feature indices start at 1
#         features.append(i)


def printFeatures(features):
    for i, feature in enumerate(features):
        print(feature, end=", " if i < len(features) - 1 else "")


def printWarning(features, highestAccuracy):
    print("\n(Warning: Accuracy decreased!)")
    print(f"Finished Search! The best feature subset is {{", end="")
    printFeatures(features)
    print(f"}}, with an accuracy of {highestAccuracy:.2f}%")

def printBest(features, highestAccuracy):
    print(f"\nFeature set {{", end="")
    printFeatures(features)
    print(f"}} is best, accuracy is {highestAccuracy:.2f}%\n")




def calculateEuclideanDistance(features, test, train):
    distance = 0
    for feature in features:
        distance += (test[feature] - train[feature]) ** 2
    return np.sqrt(distance)


def leaveOneOutValidation(features, df):
    correct = 0
    for i in range(len(df)):
        test_instance = df.iloc[i]
        train_data = df.drop(index=i)

        nearest_neighbor = None
        smallest_distance = float('inf')

        for _, train_instance in train_data.iterrows():
            distance = calculateEuclideanDistance(features, test_instance, train_instance)
            if distance < smallest_distance:
                smallest_distance = distance
                nearest_neighbor = train_instance

        if nearest_neighbor[0] == test_instance[0]:  # Compare class labels
            correct += 1

    return correct / len(df) * 100


def getData(userInput):
    df = pd.read_csv(userInput, sep="\s+", header=None)
    start_time = time.time()
    for column in df.columns[1:]:  # Normalize all columns except the target
        df[column] = (df[column] - df[column].mean()) / df[column].std()
    end_time = time.time()
    print("Time to normalize data:", round(end_time - start_time, 2), "seconds")
    return df


def forwardSelection(numOfFeatures, df):
    featuresWithHighestAccuracy = []
    highestAccuracy = 0
    features = list(range(1, numOfFeatures + 1))

    print(f"Using no features and \"leave-one-out\" evaluation, accuracy is {highestAccuracy:.2f}%.\n")
    print("Beginning search.\n")

    while features:
        bestFeatureThisLevel = None
        for feature in features:
            currentFeatures = featuresWithHighestAccuracy + [feature]
            accuracy = leaveOneOutValidation(currentFeatures, df)
            print(f"Using feature(s) {currentFeatures}, accuracy is {accuracy:.2f}%")

            if accuracy > highestAccuracy:
                highestAccuracy = accuracy
                bestFeatureThisLevel = feature

        if bestFeatureThisLevel:
            features.remove(bestFeatureThisLevel)
            featuresWithHighestAccuracy.append(bestFeatureThisLevel)
            printBest(featuresWithHighestAccuracy, highestAccuracy)
        else:
            printWarning(featuresWithHighestAccuracy, highestAccuracy)
            break


def backwardSelection(numOfFeatures, df):
    featuresWithHighestAccuracy = list(range(1, numOfFeatures + 1))
    highestAccuracy = leaveOneOutValidation(featuresWithHighestAccuracy, df)

    print(f"Using all features and \"leave-one-out\" evaluation, accuracy is {highestAccuracy:.2f}%.\n")
    print("Beginning search.\n")

    while len(featuresWithHighestAccuracy) > 1:
        bestFeatureThisLevel = None
        for feature in featuresWithHighestAccuracy:
            currentFeatures = [f for f in featuresWithHighestAccuracy if f != feature]
            accuracy = leaveOneOutValidation(currentFeatures, df)
            print(f"Using feature(s) {currentFeatures}, accuracy is {accuracy:.2f}%")

            if accuracy > highestAccuracy:
                highestAccuracy = accuracy
                bestFeatureThisLevel = feature

        if bestFeatureThisLevel:
            featuresWithHighestAccuracy.remove(bestFeatureThisLevel)
            printBest(featuresWithHighestAccuracy, highestAccuracy)
        else:
            printWarning(featuresWithHighestAccuracy, highestAccuracy)
            break
