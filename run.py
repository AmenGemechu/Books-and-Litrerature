import json
import logo
import os
import time
import sys
import tty 
import termios 
import csv


def print_slow(text):
    """
    Prints text slowly with type-writer effect.
    """
    file_descriptor = sys.stdin.fileno()
    old_settings = termios.tcgetattr(file_descriptor)
    try:
        # set terminal to raw to prevent user from interuptings
        tty.setraw(file_descriptor)
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.04)
    finally:
        # restore terminal settings
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
    print()
    

def get_user_name():
    """
    Get username
    Error handeling restricts input length to min 3 & max 10 characters 
    """
    while True:
        name = input()
        if len(name) > 2 and len(name) < 10:
            break
        else:
            print("User name should be min 3 and max 10 characters long.")
    name = name.upper()
    """
    Storing the user and the last score in a file using cvs_file 
    it allowes the user to continue from its last score.
    """
    global last_score

    # Error handeling if file doesn't exist
    # if not os.path.exists("levels.txt"):
    #   csv_file("levels.tx", 'w').close()

    with open("userdata.txt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')

        global line_count
        line_count = 0
        found = False
        for row in csv_reader:
            if name == row[0]:
                found = True
                break
            line_count += 1

        if found is True:
            print(f"match in raw: {+ line_count}")
            last_score = row[1]
            print(f'\t{row[0]} {row[1]}.')
            print(f'Processed {line_count} lines.')
            csv_file.close()

        if found is False:
            last_score = 0
            line_count += 1

            # Creating user data for new users.
            with open("userdata.txt", "a") as myfile:
                myfile.write("\n" + str(name) + ":" + str(last_score))
            myfile.close()           
    return name


def new_game():
    """
    Calling the new game function.
    Defining guesses and correct guesses globaly to be used across functions.
    Error handeling for invalid entry.
    """
    global guesses
    guesses = []
    global correct_guesses
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------------------------------")
        print_slow(key)

        # Options are displayed under every question.
        for i in options[question_num-1]:
            print(i)

        # User input
        while True:
            guess = input("Enter (A, B or C): ")
            guess = guess.upper()
            
            if "A" in guess or "B" in guess or "C" in guess:
                guesses.append(guess)
                break
            else:
                print(f"You entered {guess} please enter A, B or C")

        # Incrementing score by one.
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1


# Check correct answer.
def check_answer(answear, guess):
    """
    Checking if answer is equal to guess.
    Incrementing and Decrementing Score accordingly.
    """
    if answear == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG ANSEWR!")
        return 0


def play_again():
    """
    Play again function lets the user play another round of the game
    if they wish to or exit the program.
    """
    while True:
        score = int((correct_guesses/len(questions))*100)
        print("____________________________________________")
        print_slow("Your score is: "+str(score)+"%")
        print("")
        
        print(f"last_score: {last_score}")
        combined_score = score + int(last_score)
      
        with open("userdata.txt") as csv_file:
            file_content = csv_file.read()
            replaced_content = file_content.replace(str(name) + ":" + str(last_score), str(name) + ":" + str(combined_score))
        csv_file.close()
        
        with open("userdata.txt", 'w') as csv_file:
            csv_file.write(replaced_content)

        print_slow(f"Your combined Score is {combined_score}")
        response = input("Do you want to play again? /n Enter 'yes' or 'no'")
        response = response.upper()

        if response == "YES":
            print_slow("New game Starting...")
            return True
        elif response == "NO":
            display_score(correct_guesses, guesses)
            return False
        else:
            print_slow("Invalid Entry, Please Enter 'Yes' or 'No'.")
        

def display_score(correct_guesses, guesses):
    """
    User will be provided with their score at the end of the game.
    """
    print("____________________________________________")
    print_slow("RESULTS")
    print("____________________________________________")

    # Displays all the values within the dictionary.
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("____________________________________________")
    print("Your Answer: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # Calculating and multiplying score by 100 to display it by percentage.
    score = int((correct_guesses/len(questions))*100)
    print("____________________________________________")
    print("Your score is: "+str(score)+"%")


# Storing questions & correct answers using dictionary keys and values.
questions = {
    "1. Which horror author penned the apocalyptic novel 'The Stand'? ": "A",
    "2. Which book is about a band of rabbits became a bestseller in 1972? ": "B",
    "3. The classic 1877 novel 'Black Beauty' is about what kind of animal? ": "A",
    "4. Who was the first author to use a 'typemachine' or typewriter in writing a manuscript?": "C",    
    "5. What is 1988 book by Salman Rushdie is considered blasphemous by many Muslim countries?": "C",    
    "6. Which mystery writer holds the Guinness World Record for the most translated works?": "B",     
    "7. What book holds the record for the fastest selling book in history? ": "A", 
    "8. 'Call me Ishmael' is the first line from what classic novel?": "B",     
    "9. What Charles Dickens novel begins with the sentence, 'It was the best of times, it was the worst of times'": "C",     
    "10. What popular young adult book series sends 'tributes' to participate in a televised competition in which they fight to the death? ": "C",
    "11. Jacob Black is a character in what Stephenie Meyer book series? ": "A",
    "12. What Nicholas Sparks book was about a young socialite and her long-time crush was made into a movie starring Ryan Gosling and Rachel McAdams?": "B",
    "13. In one of the most popular Dr. Seuss books, what won't Sam-I-Am eat? ": "B"
}

# Storing multiple choice options using lists.
options = [
    ["A. Stephen King", "B. Shirley Jackson", "C. Clive Barker"],
    ["A. The Bug Book", "B. Watership Down", "C. The Sinking Spell"],
    ["A. Horse", "B. Dog", "C. Cow"],
    ["A. Jane Auston", "B. Geore Orwell", "C. Mark Twain"],
    ["A. The Da Vinch code", "B. The Fatal Lozenge", "C. The Satanic Verses"],
    ["A. Pablo Coelho", "B. Agatha Christie", "C. Carlo Collodi"],
    ["A. Harry Potter and the Deathly Hallows", "B. The Lord of the Rings", "C. The Alchemist"],
    ["A. To kill a mockingbird", "B. Moby Dick", "C. The great Gatsby"],
    ["A. The Pickwick Papers", "B. A Christmas Carol", "C. A Tale of Two Cities"],
    ["A. The host", "B. The chemist", "C. The Hunger Games"],
    ["A. Twilight", "B. Speed", "C.Divergent"],
    ["A. Shotgun Wedding", "B. The Notebook", "C. Purple hearts"],
    ["A. Eggs and becon", "B. Green eggs and ham", "C. Pancake"],
]


os.system('clear')
logo.logo_welcome_page()
print_slow("Welcome to Books & Litrature Quiz!")
print_slow("Please enter your User name:")
name = get_user_name()
print_slow(f"Hello there, {name}!")
try:
    last_score
    print_slow(f"Your last Score was, {last_score}")
except:
    print()

new_game()

# Play again function
while play_again():
    new_game()
print_slow("Thanks for being here :) See you next time!")