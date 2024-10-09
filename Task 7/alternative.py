# Ask user for a sentence.
my_sentence = input("Enter a sentence")

result = ""

# Loop the length of input sentence.
for i in range(0,len(my_sentence)):
    if i % 2 == 0:                         
        # If the index is even, then append the letter uppercased to the result.
        result += my_sentence[i].upper()   
    else:                                  
        # If the index is odd, then append the letter lowercased to the result.
        result += my_sentence[i].lower()  
print(result)

# Split the sentence for every space.
list_of_words = my_sentence.split(" ")

# Loop the length of the list of words.
for i in range(0, len(list_of_words)):            
    if i % 2 == 0:                                  
        # If the index is even, then append the word uppercased to the result.              
        list_of_words[i] = list_of_words[i].upper()
    else:                                           
        # If the index is odd, then append the word lowercased to the result.
        list_of_words[i] = list_of_words[i].lower()

# Print the list of words joined by a space.
print(" ".join(list_of_words))             