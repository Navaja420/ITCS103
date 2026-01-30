#function to compute average
def com_ave (numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

#function to compare word length and average
def compare_length_and_average(word_length, average, word):
    if word_length > average:
        print(f"The length of the word '{word}' is grater than the average.")
    elif word_length < average:
        print(f"The length of the word '{word}' is less than the average.")
    else:
        print(f"The length of the word '{word}' is equal to the average.")

#main program
word = input("Enter a word--> ")
length = len(word)

numbers = []

for i in range(length):
    num = int(input(f"Enter a number {i+1} --> "))
    numbers.append(num)

average = com_ave(numbers)

print(numbers)
print("The length of the word is", length)
print("The average of the numbers is", average)


compare_length_and_average(length, average, word)

