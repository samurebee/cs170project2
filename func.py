import random

def forwardSelection(numOfFeatures):

    features = [] # list to know what features could be added
    highestAccuracy = round(random.random() * 100,1) # no features has highest accuracy so far.
    featuresWithHighestAccuracy = [] # when adding a feature the feature that gives the highest accuracy is added here
    accuracyFlag = 0 # used to see if the accuracy increases
    print("Using no features and \"random\" evaluation, I get an accuracy of ", highestAccuracy, "%.\n", sep = "")

    print("Beginning Search.\n")

    # add feature numbers here based on number of features chosen by user
    for i in range(0, numOfFeatures):
        features.append(i+1)

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
            print("\n(Warning, Accuracy has decreased!)")
            print("Finished Search!! The best feature subset is {", end="")
            for i in range(0,len(featuresWithHighestAccuracy)):
                print(featuresWithHighestAccuracy[i], sep = "", end="")
                if(i != len(featuresWithHighestAccuracy) - 1):
                    print(",", sep = "", end="")
            print("}, which has an accuracy of ", highestAccuracy, "%.\n", sep = "",)
            break
        # if accuracy increases print set of features with highest accuracy so far and continue search
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