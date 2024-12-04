import func
import time
 
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
        "Enter your choice: "
    )
    try:
        numberAlgorithm = int(numberAlgorithm)
        if numberAlgorithm in [1, 2]:
            break
        else:
            print("Please choose 1 or 2.")
    except ValueError:
        print("Please enter a valid integer (1 or 2).")

df = func.getData(dataset_path)
numFeatures = df.shape[1] - 1

if numberAlgorithm == 1:
    start_time = time.time()
    func.forwardSelection(numFeatures, df)
    end_time = time.time()
    print(f"Time to run forward selection for {dataset_path} is {round(end_time - start_time, 2)} seconds" )
elif numberAlgorithm == 2:
    start_time = time.time()
    func.backwardSelection(numFeatures, df)
    end_time = time.time()
    print(f"Time to run backward selection for {dataset_path} is {round(end_time - start_time, 2)} seconds" )
# elif numberAlgorithm == 3:
#     specialAlgorithm(dataset_path)
