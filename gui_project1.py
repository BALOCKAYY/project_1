from tkinter import *
import logic_project1


class Gui:
    """
    The GUI class is used to store all the data regarding the
    layout and design of the interface, but also the connecting logic
    for what happens when certain events occur on the
    GUI. These events are handled by a different module called
    logic_project1.py which handles the logic relating to
    events on the GUI.
    """
    def __init__(self, window) -> None:
        """
        This function sets up the GUI by creating a
        pop-up where the user can submit their voter id's
        as well as pick a candidate to vote for. The input would
        accept a first and last name as a string and check to see if the
        person has voted before. If they have then an error
        pops up, but if not then the users vote is taken in and added
        to the total for a candidate.
        """
        self.window = window
        self.frame_one = Frame(self.window)
        self.label_name = Label(self.frame_one, text="Voter ID: ".ljust(10))
        self.input_name = Entry(self.frame_one, width = 20)
        self.real_name = self.input_name.get()
        self.label_name.pack(side='left')
        self.input_name.pack()
        self.frame_one.pack()

        self.frame_two = Frame(self.window)
        self.label_name = Label(self.frame_two, text="")
        self.label_name.pack()
        self.frame_two.pack()

        self.frame_three = Frame(self.window)
        self.label_name = Label(self.frame_three, text="Candidates:")
        self.label_name.pack()
        self.frame_three.pack()

        self.frame_four = Frame(self.window)
        self.radio_answer = IntVar(value=0)
        self.radio_button1 = Radiobutton(self.frame_four, text="Bianca", variable=self.radio_answer, value=1)
        self.radio_button2 = Radiobutton(self.frame_four, text="Edward", variable=self.radio_answer, value=2)
        self.radio_button3 = Radiobutton(self.frame_four, text="Felicia", variable=self.radio_answer, value=3)
        self.radio_button1.pack()
        self.radio_button2.pack()
        self.radio_button3.pack()
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.label_name = Label(self.frame_five, text="")
        self.label_name.pack()
        self.frame_five.pack()
        self.frame_six = Frame(self.window)
        self.submit_button = Button(self.frame_six, text="SUBMIT VOTE", command=lambda: logic_project1.get_voting(self))
        self.submit_button.pack()
        self.frame_six.pack()

        self.frame_eight = Frame(self.window)
        self.total_button = Button(self.frame_eight, text="TOTAL", command= lambda: logic_project1.total(self))
        self.total_button.pack()
        self.frame_eight.pack()

        self.frame_eight_point_five = Frame(self.window)
        self.frame_eight_point_five_label = Label(self.frame_eight_point_five, text=' ')
        self.frame_eight_point_five_label.pack()
        self.frame_eight_point_five.pack()

        self.frame_nine = Frame(self.window)
        self.label_nine = Label(self.frame_nine, text='')
        self.label_nine.pack()
        self.frame_nine.pack()







