str_manip = input("Enter a sentence.")

len_str_manip = len(str_manip)
print(len_str_manip)

last_letter = str_manip[-1]
new_word = str_manip.replace(last_letter, '@')
print(new_word)

print(str_manip[:-4:-1])

print(str_manip[:3] + str_manip[-2::1])
