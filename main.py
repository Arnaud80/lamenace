from tkinter import *
from PIL import ImageTk, Image


def load_questions():
    try:
        questions_file = open("resources/questions.csv", "r")  # Open the file
    except FileNotFoundError:
        print("File resources/questions.csv doesn't exist, please create it with this format : ")
        print("question;image.jpg;answer1,answer2,answer3")
    else:
        lines = questions_file.read().splitlines()
        question_list = []

        for line in lines:
            split = line.split(";")
            question_list.append({
                "question": split[0],
                "proposal": split[1],
                "answer": split[2],
                "picture": split[3]
            })

        questions_file.close()
        return question_list


def check_answer(num, checkbox_status):
    good_answers = questions[num]["answer"].split(',')
    user_answers = []

    letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i'}

    count = 0

    for checkbox in checkbox_status:  # Add user answer in array user_answers
        if checkbox.get() == 1:
            user_answers.append(letters[count])
        count += 1

    # print("your answers = " + ", ".join(user_answers))
    # print("good answers = " + ", ".join(good_answers))

    global user_score
    if user_answers == good_answers:  # Compare user_answers with good_answer, and update the score
        user_score += point_for_good_answer
    else:
        user_score += point_for_wrong_answer

    # print("Your new score is ", user_score, " / ", total)
    display_question(num + 1)


def display_question(num):
    # We delete element in the frame to delete the welcoming messages
    for widgets in frame.winfo_children():
        widgets.destroy()

    if num < len(questions):
        # Question
        label_question = Label(frame, text=questions[num]["question"], font=("Courrier", 20), bg='#41B77F',
                               fg='#FFFFFF')
        label_question.pack()

        # Create an object of tkinter ImageTk
        img = Image.open("resources/images/" + questions[num]["picture"])
        img = img.resize((200, 200))
        picture = ImageTk.PhotoImage(img)
        # Create a Label Widget to display the text or Image
        label_image = Label(frame, image=picture)
        label_image.image = picture  # Anchor the image to the label
        label_image.pack()

        # Proposals
        label_proposals = []
        checkbox_proposals = []
        checkbox_status = []
        proposals = questions[num]["proposal"].split(",")
        answers = questions[num]["answer"].split(",")
        count_proposal = 0

        for proposal in proposals:
            checkbox_status.append(IntVar())
            checkbox_proposals.append((Checkbutton(frame, text=proposal, variable=checkbox_status[count_proposal],
                                                   onvalue=1, offvalue=0,
                                                   font=("Courrier", 10), selectcolor='black', fg='white', bg='#41B77F')))
            checkbox_proposals[count_proposal].pack()
            # label_proposals.append(Label(frame, text=proposal, font=("Courrier", 10), bg='#41B77F', fg='#FFFFFF'))
            # label_proposals[count_proposal].pack()
            count_proposal += 1

        # Add Button
        q_button = Button(frame, text="OK", font=("Courrier", 15), bg='white', fg='#41B77F',
                          command=lambda: check_answer(num, checkbox_status))
        q_button.pack(pady=20, fill=X)
    else:
        # Message End of the game
        label_end = Label(frame, text="End of the game", font=("Courrier", 30), bg='#41B77F',
                          fg='#FFFFFF')
        label_end.pack()

        # Create an object of tkinter ImageTk
        img = Image.open("resources/images/gameover.png")
        img = img.resize((300, 300))
        picture = ImageTk.PhotoImage(img)
        # Create a Label Widget to display the text or Image
        label_image = Label(frame, image=picture)
        label_image.image = picture  # Anchor the image to the label
        label_image.pack()

        # Text to display the score
        txt_score = "Your score is " + str(user_score) + " / " + str(total)
        label_score = Label(frame, text=txt_score, font=("Courrier", 30), bg='#41B77F',
                            fg='#FFFFFF')
        label_score.pack()


# We load the questions
questions = load_questions()

# Game variables initialization
user_score = 0
point_for_good_answer = 5
point_for_no_answer = 0
point_for_wrong_answer = -2
total = point_for_good_answer * len(questions)

# Window creation
window = Tk()

# Window personalisation
window.title("La Menace")
window.geometry("1080x720")  # Default size
window.wm_minsize(480, 360)  # Size min
window.iconbitmap("resources/images/logo.ico")  # Logo on the window
window.config(background='#41B77F')  # Background color

# Frame creation
frame = Frame(window, bg="#41B77F")  # To add a border, bd=1, relief=SUNKEN)

# text
label_title = Label(frame, text="Welcome in the game 'La Menace'", font=("Courrier", 40), bg='#41B77F', fg='#FFFFFF')
label_title.pack()
label_subtitle = Label(frame, text="By Jean KOUAKOU", font=("Courrier", 25), bg='#41B77F', fg='#FFFFFF')
label_subtitle.pack()

# Add Button
yt_button = Button(frame, text="Lancer le jeu", font=("Courrier", 25), bg='white', fg='#41B77F',
                   command=lambda: display_question(0))
yt_button.pack(pady=20, fill=X)

# Add frame in window
frame.pack(expand=YES)

# Display the window
window.mainloop()
