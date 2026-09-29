import random
import time
import string
import pyperclip

def estimate_hack_time(length):
    if length <= 6:
        return "Instantly"
    elif length == 7:
        return "6 minutes"
    elif length == 8:
        return "132 years"
    elif length == 9:
        return "12,000 years"
    elif length == 10:
        return "1 million years"
    elif length == 11:
        return "112 million years"
    elif length == 12:
        return "10 billion years"
    else:
        return "Trillions of years"

def create_password(length):
    time.sleep(0.5)
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    must = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(symbols)
    ]

    all_stuff = letters + numbers + symbols
    length_left = length - 3
    rest = [random.choice(all_stuff) for _ in range(length_left)]

    combined = must + rest
    random.shuffle(combined)

    return "".join(combined)

app_running = True

while app_running:
    print("Enter character length for password (5-25 + q to quit): ")

    while True:
        try:
            user_input = input("You: ")
            if user_input == "q":
                app_running = False
                print("app quit")
                break
            else:
                length = int(user_input)
            
            if length < 5 or length > 25:
                raise ValueError("Number must be between 5 and 25!")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
            print("Enter character length for password (5-25): ")
    
    if app_running == False:
        break


    print(f"Your character length is {length}.")
    print("Creating password...")
    
    result = create_password(length)
    print(result)

    pyperclip.copy(result)
    print("Password auto copied to clipboard.")

    print("Estimating time to hack...")
    time.sleep(0.5)
    hack_time = estimate_hack_time(length)
    print(f"Estimated time your password would be hacked in: {hack_time}")

