#This is for practice - Chatbox
Bot_name = "Bob"
print(f"Hello I'm {Bot_name}🧑, Looking for some help? 👀")
user_name = input("Enter your name: ")
print(f"{Bot_name}: Hey there {user_name} 🙋‍♂️")
while True:
    user_input = input("You: ").lower()
    if user_input == "quit":
        print(f"{Bot_name}: See you later {user_name}, Have a great day!☀️🧖")
        break

    if user_input in ["hi", 'hello', 'hey']:
        print(f"{Bot_name}: Hey {user_name}, What's up there!😉")
    elif user_input in ["bye", "goodbye"]:
        print(f"{Bot_name}: Goodbye, Have a great day!😊, {user_name}")
    elif user_input in ["good", "not bad", "same as ever"]:
        print(f"{Bot_name}: Good to hear that from you.🥰")
    elif user_input in ["good, How' about you?", "how's about you?"]:
        print(f"{Bot_name}: So far so good!😃👌")
    elif user_input in ["thanks", "yep", "thank you"]:
        print(f"{Bot_name}: It's my pleasure, I'm ready to go along with you {user_name}💯! What can I help?🤠")
    elif user_input in ["yes", "yes please", "why not?", "ok"]:
        print(F"{Bot_name}: Here we go again!😎")
        print("What would you like to do?")
    elif user_input in ['+', 'add']:
        print(f"{Bot_name}: Sure! What would you like to add {user_name}?➕")

        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            print(f"{Bot_name}: The sum is {num1 + num2}✨")
        except ValueError:
            print(f"{Bot_name}: Oh. Dear! You just miss a bit😐 please try again.😉")

    elif user_input in ["-", "minus", "subtract"]:
        print(f"{Bot_name}: Oh!😮, Let's go!🚀")
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            print(f"{Bot_name}: The answer is {num1 + num2}✨")
        except ValueError:
            print(f"{Bot_name}: Oops, something went wrong. Let's go again!")


    elif user_input in ["x", "multiply"]:
        print(f"{Bot_name}: Wow!😮, OK🔥")
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            print(f"{Bot_name}: The answer is {num1 * num2}✨")
        except ValueError:
            print(f"{Bot_name}: Oops, something went wrong. Let's go again!")

    elif user_input in ["/", "divide"]:
        print(f"{Bot_name}: Yeah!😮, Let's do it!👊")
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            print(f"{Bot_name}: The answer is {num1 / num2}✨")
        except ValueError:
            print(f"{Bot_name}: Oops, something went wrong. Let's go again!")

    else:
        print(f"{Bot_name}: Hey there, It look like you entered the wrong thing {user_name}, Would you like to try again?✨")




