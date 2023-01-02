from game import *

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
                   command=lambda: display_question(0, game))
yt_button.pack(pady=20, fill=X)

# Add frame in window
frame.pack(expand=YES)

questions = load_questions() # We load the questions

game = {
    "questions": questions,
    "user_score": 0,
    "point_for_good_answer": 1,
    "point_for_wrong_answer": 0,
    "total": len(questions),
    "wrong_answers": [],
    "frame": frame,
}

# Display the window
window.mainloop()
