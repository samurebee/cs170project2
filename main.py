import func
# User prompts and validate choices
# Goes to the correct algorithm that the user chooses

# while True:
#     numFeatures = input("Please enter total number of features: ")
#     try:
#         numFeatures = int(numFeatures)
#         break
#     except ValueError:
#         print("Please enter a integer")

# while True:
#     numberAlgorithm = input("\nForward Selection(1)\nBacward Elimination(2)\nSpecial Algorithm(3)\nEnter:")
#     try:
#         numberAlgorithm = int(numberAlgorithm)
#         break
#     except ValueError:
#         print("Please enter a integer")

# if(numberAlgorithm == 1):
#     func.forwardSelection(numFeatures)

# elif(numberAlgorithm == 2):
#     func.backwardSelection(numFeatures)

userInput = input("Type in the name of the file to test: ")
func.NNClassifier([3,5,7], userInput)