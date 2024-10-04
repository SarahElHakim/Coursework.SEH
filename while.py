total = 0
count = 0

while True:
    guess = int(input("Please enter a number: "))
    if guess > 0 or guess < -1:
        count += 1
        total += guess
    elif guess == 0:
        print ("Invalid input. ")
    elif guess == -1:
        break

average = total / count
print(average)
