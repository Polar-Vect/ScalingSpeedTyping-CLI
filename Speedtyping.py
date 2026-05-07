import time
import random

print("This Game was created by Adrian-weber7 and extended by Polar")


waitTime = 1
combo = 0

while "a":
    rand =  ["The quick brown fox jumps over the lazy dog.",
        "Programming in Python is fun and rewarding.",
        "I want to improve my typing speed every day.",
        "Data science is a very interesting field of study.",
        "Artificial intelligence is changing the world fast.",
        "Can you hear the sound of the ocean waves?",
        "The weather is beautiful for a walk in the park.",
        "I need to drink more water during the day.",
        "Coding requires a lot of patience and focus.",
        "Success is the result of hard work and learning.",
        "Practice makes perfect when it comes to typing.",
        "She sells seashells by the seashore.",
        "How many words can you type in one minute?",
        "The mountain top was covered in thick white snow.",
        "Innovation distinguishes between a leader and a follower.",
        "Do not count the days, make the days count.",
        "Technology is a useful servant but a dangerous master.",
        "The capital of France is a city called Paris.",
        "Would you like to have a cup of coffee with me?",
        "The internet connects people from all over the world.",
        "Keyboard shortcuts can save you a lot of time.",
        "The project deadline is scheduled for next Friday.",
        "A journey of a thousand miles begins with a single step.",
        "Please make sure to save your files before exiting.",
        "Life is what happens when you are making other plans.",
        "The galaxy is vast and full of mysterious stars.",
        "I love the smell of fresh rain on hot asphalt.",
        "To be or not to be, that is the question.",
        "Knowledge is power, but character is more important.",
        "The electric car is parked in front of the house.",
        "Don't forget to include the 'import time' statement.",
        "My favorite color is deep blue, like the night sky.",
        "Can you solve this complex mathematical equation?",
        "Every cloud has a silver lining, so stay positive.",
        "The quick movement of the keys creates a rhythm.",
        "I am currently writing a script to measure time.",
        "Wait, did you remember to close the brackets?",
        "The user interface should be simple and clean.",
        "Open source software is great for the community.",
        "Cyber security is vital in the digital age.",
        "Learning a new language is always a good idea.",
        "The coffee shop is open from 7 AM to 10 PM.",
        "Check your code for any syntax errors or bugs.",
        "Music has the power to heal the soul and mind.",
        "Is this your first time building a typing app?",
        "The sun sets in the west and rises in the east.",
        "Keep calm and continue coding your project.",
        "Efficiency is doing things right; effectiveness is doing right things.",
        "The world is a book and those who do not travel read only one page.",
        "Congratulations, you have finished the typing test!"]
    
    sentence = random.choice(rand)
    
    print(f"Your sentence : {sentence}")
    print("3")
    time.sleep(waitTime)
    print("2")
    time.sleep(waitTime)
    print("1")
    time.sleep(waitTime)
    print("GO !")
    starting_time = time.time()

    user = input("Type here : ").lower()
    end_time=time.time()
    if user == sentence.lower():
        duration = end_time - starting_time
        print(f"Your Time is : {duration:.2f} Seconds")
        print("Everything is correct!")
        time.sleep(0.7)
        print("New round !")
        time.sleep(2)
        combo += 1
        if waitTime > 0.05:
            waitTime -= 0.05

    else:
        duration = end_time - starting_time
        print(f"Your Time is : {duration:.2f} Seconds")
        print("You made a mistake")
        if combo > 1:
            print(f"You had a combo of {combo}🔥")
        choice = int(input("Press 1 if you want to play again and 2 if not : "))
        if choice == 1:
            pass
        elif choice == 2:
            break
