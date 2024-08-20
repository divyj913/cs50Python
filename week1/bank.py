greeting = input("Greeting: ")
greeting.split()
word = "Hello"
word1 = "hello"
first_word = greeting[0]
if word in greeting or word1 in greeting:
    print("$0")
elif first_word == "h" or first_word == "H":
    print("$20")
else:
    print("$100")
