from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.question = "sfdfsdf"
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.canvas = Canvas(
            width=300, height=250,  highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text=self.question, font=("Arial", 20, 'italic'), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Create a label
        self.label = Label(text="Score: 0", font=(
            'Arial'), fg='white', bg=THEME_COLOR)
        self.label.grid(column=1, row=0)
        # self.label.config(padx=20, pady=20, )

        # create buttons
        self.true_button = Button(image=true_img,
                                  highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.true_button.config(padx=20, pady=20)

        self.false_button = Button(image=false_img,
                                   highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.false_button.config(padx=20, pady=20)

        # wywalanie pierwzego pytania
        get_next_question(self)
        self.window.mainloop()


def get_next_question(self):
    q_text = self.quiz.next_question()
    self.canvas.itemconfig(self.question_text, text=q_text)
