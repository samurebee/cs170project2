import func
# User prompts and validate choices
# Goes to the correct algorithm that the user chooses

numFeatures = input("Please enter total number of features: ")

numberAlgorithm = input("\nForward Selection(1)\nBacward Elimination(2)\nSpecial Algorithm(3)\nEnter:")

if(numberAlgorithm == 1):
    func.forwardSelection(numFeatures)

elif(numberAlgorithm == 2):
    func.backwardSelection(numFeatures)