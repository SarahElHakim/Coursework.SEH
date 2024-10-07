# Ask their time in the swimming event.

# Ask their time in the cycling event.

# Ask their time in the running event.

# Calculate their total time.

# Print their award based on the qualifying criteria.

swimmingTime = input("Enter your swimming time in minutes.")
cyclingTime = input("Enter your cycling time in minutes.")
runningTime = input("Enter your running time in minutes.")

totalTime = int(swimmingTime) + int(cyclingTime) + int(runningTime)
print(totalTime)


if totalTime >= 111:
    print("No award")
elif  totalTime >= 106:
    print("Honoray scroll")
elif totalTime >= 101:
    print("Honoray half colours")
else: 
    print("Honorary colours")