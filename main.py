import func
# User prompts and validate choices
# Goes to the correct algorithm that the user chooses

while True:
    numFeatures = input("Please enter total number of features: ")
    try:
        val = int(numFeatures)
        break
    except ValueError:
        print("Please enter a integer")

while True:
    numberAlgorithm = input("\nForward Selection(1)\nBacward Elimination(2)\nSpecial Algorithm(3)\nEnter:")
    try:
        val = int(numberAlgorithm)
        break
    except ValueError:
        print("Please enter a integer")

if(numberAlgorithm == 1):
    func.forwardSelection(numFeatures)

elif(numberAlgorithm == 2):
    func.backwardSelection(numFeatures)