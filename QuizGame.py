###################
#
#   Imports
#
##################

import pgzrun  # Pygame Zero library used to run the game

###################
#
#   Game Window Size
#
##################

WIDTH = 1280
HEIGHT = 720

###################
#
#   UI Boxes (Rectangles)
#
##################

# Main question box and timer box
main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)

# Answer boxes
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

# Move boxes to their positions on the screen
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

# Group answer boxes into a list for easy iteration
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

###################
#
#   Game State Variables
#
##################

score = 0            # Number of correct answers
time_left = 10       # Countdown timer for each question

###################
#
#   Questions Format:
#   [Question text, Option1, Option2, Option3, Option4, Correct option index]
#
##################

q1 = ["What is the capital of France?",
      "London", "Paris", "Berlin", "Tokyo", 2]
q2 = ["What is 5 + 7?",
      "12", "10", "14", "8", 1]
q3 = ["What is the seventh month of the year?",
      "April", "May", "June", "July", 4]
q4 = ["Which planet is closest to the sun?",
      "Saturn", "Neptune", "Mecury", "Venus", 3]
q5 = ["Where are the pyramids?",
      "India", "Egypt", "Morocoo", "Canada", 2]

# Load all questions into a list and pop the first one
questions = [q1, q2, q3, q4, q5]
question = questions.pop(0)

###################
#
#   Draw Function - Renders the UI
#
##################

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    # Draw answer boxes
    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    # Display timer and question text
    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    # Display answer options
    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1

###################
#
#   End Game Function
#
##################

def game_over():
    global question, time_left
    message = "Game Over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]  # Display message as a fake "question"
    time_left = 0

###################
#
#   Handle Correct Answer
#
##################

def correct_answer():
    global question, score, time_left
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()

###################
#
#   Mouse Click Handling
#
##################

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:  # Check if selected answer is correct
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1

###################
#
#   Timer Countdown Logic
#
##################

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

# Schedule timer to decrease every second
clock.schedule_interval(update_time_left, 1.0)

###################
#
#   Start the Game Loop
#
##################

pgzrun.go()
