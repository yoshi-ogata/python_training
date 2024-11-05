quote = "I love python"

#index starts from 0 including a space
print(quote[2])
print(quote[3])
print(quote[0])

#slice operator
#quote[start:end:skip] #end is not included
print(quote[2:6])
print(quote[2:])

#skip
print(quote[2:10:2])

#negative index
print(quote[-1])

#whole string
print(quote[0:])
print(quote[:])

#reverse string
print(quote[::-1])

name = " Yoshi"
print(name.upper())
print(name.lower())

#trim spaces
print(name.strip())


# Task
secret_message = "   Programming in Python is not only powerful but also fun!   "

# Expected Output

# "PYTHON-POWERFUL"

word1 = secret_message[18:24]
word2 = secret_message[37:45]
print(f"{word1}-{word2}".upper())

#chain
clean_message = secret_message.upper()
print(f"{clean_message[18:24]}-{clean_message[37:45]}")

# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"
word3 = flipped_message[-1:]
word4 = word3[18:24]
word5 = word3[37:45]
print(f"{word4} 🗡️ {word5} 🌸".lower())

flipped_message_reverse = flipped_message[::-1]
print(f"{flipped_message_reverse[0:6]} 🗡️  {flipped_message_reverse[12:20]} 🌸 ".lower())


