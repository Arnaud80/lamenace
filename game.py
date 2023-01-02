import tkinter
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
            if len(split) != 4:  # If the line doesn't have 4 parameter, we display the line in error and exit program
                print("Format error at line : " + line)
                exit(0)
            else:
                question_list.append({
                    "question": split[0],
                    "proposal": split[1],
                    "answer": split[2],
                    "picture": split[3]
                })

        questions_file.close()
        return question_list


def check_answer(num, checkbox_status, game):
    good_answers = game["questions"][num]["answer"].split(',')
    user_answers = []

    letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i'}

    count = 0

    for checkbox in checkbox_status:  # Add user answer in array user_answers
        if checkbox.get() == 1:
            user_answers.append(letters[count])
        count += 1

    if user_answers == good_answers:  # Compare user_answers with good_answer, and update the score
        game["user_score"] += game["point_for_good_answer"]
    else:
        game["user_score"] += game["point_for_wrong_answer"]
        game["wrong_answers"].append(num)

    display_question(num + 1, game)


def display_question(num, game):
    # We delete element in the frame to delete the welcoming messages
    for widgets in game["frame"].winfo_children():
        widgets.destroy()

    if num < len(game["questions"]):
        # Question
        label_question = Label(game["frame"], text=game["questions"][num]["question"], font=("Courrier", 20),
                               bg='#41B77F',
                               fg='#FFFFFF', wraplength=800)
        label_question.pack()

        # Create an object of tkinter ImageTk
        img = Image.open("resources/images/" + game["questions"][num]["picture"])
        img = img.resize((200, 200))
        picture = ImageTk.PhotoImage(img)
        # Create a Label Widget to display the text or Image
        label_image = Label(game["frame"], image=picture)
        label_image.image = picture  # Anchor the image to the label
        label_image.pack()

        # Proposals
        checkbox_proposals = []
        checkbox_status = []
        proposals = game["questions"][num]["proposal"].split(",")
        game["questions"][num]["answer"].split(",")
        count_proposal = 0

        for proposal in proposals:
            checkbox_status.append(IntVar())
            checkbox_proposals.append(
                (Checkbutton(game["frame"], text=proposal, variable=checkbox_status[count_proposal],
                             onvalue=1, offvalue=0,
                             font=("Courrier", 10), selectcolor='black', fg='white',
                             bg='#41B77F')))
            checkbox_proposals[count_proposal].pack()
            count_proposal += 1

        # Add Button
        q_button = Button(game["frame"], text="OK", font=("Courrier", 15), bg='white', fg='#41B77F',
                          command=lambda: check_answer(num, checkbox_status, game))
        q_button.pack(pady=20, fill=X)
    else:
        # Message End of the game
        label_end = Label(game["frame"], text="End of the game", font=("Courrier", 30), bg='#41B77F',
                          fg='#FFFFFF')
        label_end.pack()

        # Create an object of tkinter ImageTk
        img = Image.open("resources/images/gameover.png")
        img = img.resize((200, 200))
        picture = ImageTk.PhotoImage(img)
        # Create a Label Widget to display the text or Image
        label_image = Label(game["frame"], image=picture)
        label_image.image = picture  # Anchor the image to the label
        label_image.pack()

        # Text to display the score
        txt_score = "Your score is " + str(game["user_score"]) + " / " + str(game["total"])
        label_score = Label(game["frame"], text=txt_score, font=("Courrier", 30), bg='#41B77F',
                            fg='#FFFFFF')
        label_score.pack()
        label_explanation = Label(game["frame"], text="Voici les réponses où vous avez répondu faux :",
                                  font=("Courrier", 30),
                                  bg='#41B77F',
                                  fg='#FFFFFF')
        label_explanation.pack()

        txt_wronganswers = ""
        for wrong_answer in game["wrong_answers"]:
            txt_wronganswers += game["questions"][wrong_answer]["question"] + "\n"
            txt_wronganswers += game["questions"][wrong_answer]["proposal"] + "\n"
            txt_wronganswers += game["questions"][wrong_answer]["answer"] + "\n\n"

        txt_height = len(game["wrong_answers"]) * 10 * 4

        canvas = Canvas(game["frame"], width=1024, scrollregion=(0, 0, 500, 800 + txt_height))  # Create a canvas object
        vbar = Scrollbar(game["frame"], orient=VERTICAL)  # Create a scrollbar
        vbar.pack(side=RIGHT, fill=Y)  # Set the scrollbar at the right of the Canvas
        vbar.config(command=canvas.yview)
        canvas.config(yscrollcommand=vbar.set)
        # Add a text in Canvas
        # canvas.winfo_x() + game["frame"].winfo_width() / 2 + game["frame"].winfo_x(), canvas.winfo_y() + game["frame"].winfo_height()
        canvas.create_text(canvas.winfo_x() + game["frame"].winfo_width() / 2 + game["frame"].winfo_x(), txt_height,
                               text=txt_wronganswers, justify=tkinter.CENTER,
                               width=1024, font=("Courrier", 10))
        canvas.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH, anchor=tkinter.CENTER)
