from tkinter import *
from PIL import ImageTk, Image

def loadQuestions():
    try:
        questionsFile = open("ressources/questions.csv", "r")  # Open the file
    except FileNotFoundError:
        print("File ressources/questions.csv doesn't exist, please create it with this format : ")
        print("question;image.jpg;answer1,answer2,answer3")
    else:
        lines = questionsFile.read().splitlines()
        questions = []

        for line in lines:
            split = line.split(";")
            questions.append({
                "question": split[0],
                "proposal": split[1],
                "answer": split[2],
                "picture": split[3]
            })

        questionsFile.close()
        return questions


def displayQuestion(num):
    # We delete element in the frame to delete the welcoming messages
    for widgets in frame.winfo_children():
        widgets.destroy()

    if(num < len(questions)):
        # Question
        label_question = Label(frame, text=questions[num]["question"], font=("Courrier", 20), bg='#41B77F', fg='#FFFFFF')
        label_question.pack()

        # Create an object of tkinter ImageTk
        img = Image.open("ressources/images/" + questions[num]["picture"])
        img = img.resize((200,200))
        picture = ImageTk.PhotoImage(img)
        # Create a Label Widget to display the text or Image
        label_image = Label(frame, image=picture)
        label_image.image = picture # Anchor the image to the label
        label_image.pack()

        # Proposals
        label_proposals = []
        proposals = questions[num]["proposal"].split(",")
        countProposal=0
        for proposal in proposals:
            label_proposals.append(Label(frame, text=proposal, font=("Courrier", 10), bg='#41B77F', fg='#FFFFFF'))
            label_proposals[countProposal].pack()
            countProposal += 1

        # Add Button
        q_button = Button(frame, text="OK", font=("Courrier", 15), bg='white', fg='#41B77F',
                           command=lambda: displayQuestion(num+1))
        q_button.pack(pady=20, fill=X)
    else:
        # Message End of the game
        label_end = Label(frame, text="End of the game", font=("Courrier", 30), bg='#41B77F',
                               fg='#FFFFFF')
        label_end.pack()

        # Create an object of tkinter ImageTk
        img = Image.open("ressources/images/gameover.png")
        img = img.resize((300, 300))
        picture = ImageTk.PhotoImage(img)
        # Create a Label Widget to display the text or Image
        label_image = Label(frame, image=picture)
        label_image.image = picture  # Anchor the image to the label
        label_image.pack()


# We load the questions
questions = loadQuestions()

# Window creation
window = Tk()

# Window personalisation
window.title("La Menace")
window.geometry("1080x720")# Default size
window.wm_minsize(480, 360) # Size min
window.iconbitmap("ressources/images/logo.ico") # Logo on the window
window.config(background='#41B77F') # Background color

# Frame creation
frame = Frame(window, bg="#41B77F") #To add a border, bd=1, relief=SUNKEN)

# text
label_title = Label(frame, text="Welcome in the game 'La Menace'", font=("Courrier",40), bg='#41B77F', fg='#FFFFFF')
label_title.pack()
label_subtitle = Label(frame, text="By Jean KOUAKOU", font=("Courrier",25), bg='#41B77F', fg='#FFFFFF')
label_subtitle.pack()

# Add Button
yt_button = Button(frame, text="Lancer le jeu", font=("Courrier",25), bg='white', fg='#41B77F', command=lambda: displayQuestion(0))
yt_button.pack(pady=20, fill=X)

# Add frame in window
frame.pack(expand=YES)

# Display the window
window.mainloop()

