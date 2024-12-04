import func

def specialAlgorithm(dataset_path):
    df = func.getData(dataset_path)
    num_features = df.shape[1] - 1  # Exclude the class label
    print(f"Dataset loaded with {num_features} features.")

    print("\nRunning Forward Selection:")
    func.forwardSelection(num_features, df)

    print("\nRunning Backward Elimination:")
    func.backwardSelection(num_features, df)


while True:
    try:
        userInput = input("Type in the name of the file to test: ")
        dataset_path = userInput.strip()
        with open(dataset_path, 'r') as f:
            print(f"File '{dataset_path}' found and ready for processing.")
        break
    except FileNotFoundError:
        print("File not found. Please try again.")

while True:
    numberAlgorithm = input(
        "\nChoose an algorithm:\n"
        "1. Forward Selection\n"
        "2. Backward Elimination\n"
        "3. Special Algorithm (All Tests)\n"
        "Enter your choice: "
    )
    try:
        numberAlgorithm = int(numberAlgorithm)
        if numberAlgorithm in [1, 2, 3]:
            break
        else:
            print("Please choose 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid integer (1, 2, or 3).")

df = func.getData(dataset_path)
numFeatures = df.shape[1] - 1

if numberAlgorithm == 1:
    func.forwardSelection(numFeatures, df)
elif numberAlgorithm == 2:
    func.backwardSelection(numFeatures, df)
elif numberAlgorithm == 3:
    specialAlgorithm(dataset_path)
