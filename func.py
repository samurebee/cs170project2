import random

def forwardSelection(numOfFeatures):

    features = []
    highestAccuracy = round(random.random() * 100,1) 
    featuresWithHighestAccuracy = []
    accuracyFlag = 0
    print("Using no features and \"random\" evaluation, I get an accuracy of ", highestAccuracy, "%.\n", sep = "")

    print("Beginning Search.\n")

    for i in range(0, numOfFeatures):
        features.append(i+1)

    while(len(features) != 0):

        for i in range(0,len(features)):
            accuracy = round(random.random() * 100,1) 
            print("Using feature(s) {", end ="")
            for j in range(0,len(featuresWithHighestAccuracy)):
                print(featuresWithHighestAccuracy[j], ",", sep = "", end="")
            print(features[i], "} accuracy is ", accuracy, "%.", sep = "")
            if(accuracy > highestAccuracy):
                feature = features[i]
                accuracyFlag = 1
                highestAccuracy = accuracy
        if(accuracyFlag == 0):
            print("\n(Warning, Accuracy has decreased!)")
            print("Finished Search!! The best feature subset is {", end="")
            for i in range(0,len(featuresWithHighestAccuracy)):
                print(featuresWithHighestAccuracy[i], sep = "", end="")
                if(i != len(featuresWithHighestAccuracy) - 1):
                    print(",", sep = "", end="")
            print("}, which has an accuracy of ", highestAccuracy, "%.\n", sep = "",)
            break
        else:
            features.remove(feature)
            featuresWithHighestAccuracy.append(feature)
            print("\n Feature Set {", end="")
            for i in range(0,len(featuresWithHighestAccuracy)):
                print(featuresWithHighestAccuracy[i], sep = "", end="")
                if(i != len(featuresWithHighestAccuracy) - 1):
                    print(",", sep = "", end="")
            print("} was best, accuracy is ", highestAccuracy, "%.\n", sep = "",)
            accuracyFlag = 0