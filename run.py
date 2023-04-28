import json


print("Welcome to Trivia Quiz!")
username = input("Insert Username: ")
print("Hey", username, "\nFor every question you will have three options and\nfor every correct answear you will get one point!")


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------------------------------")
        print(key)

        # Options are displayed under every question.
        for i in options[question_num-1]:
            print(i)

        # User input
        guess = input("Enter (A, B or C): ")
        guess = guess.upper()
        guesses.append(guess)

        # Incrementing score by one.
        correct_guesses += check_answer(questions.get (key),guess)
        question_num += 1

    # Displays final score to the user.
    display_score(correct_guesses, guesses)


# Check correct answer.
def check_answer(answear, guess):
    """
    Checking if answer is equal to guess.
    """
    if answear == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG ANSEWR!")
        return 0


def display_score(correct_guesses, guesses):
    """
    User will be provided with a display of their total score at the end of the game.
    """
    print("____________________________________________")
    print("RESULTS")
    print("____________________________________________")
    print("Correct Answers:", end="")

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
    print("Your score is: "+str(score)+"%")


def play_again():
    pass


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
    "12. What Nicholas Sparks book about a young socialite and her long-time crush was made into a movie starring Ryan Gosling and Rachel McAdams?": "B",
    "13. In one of the most popular Dr. Seuss books, what won't Sam-I-Am eat? ": "B"

}

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

"""
Calling the new game function.
"""
new_game()