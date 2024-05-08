from gui_project1 import *
import csv

def voting(answer, name) -> bool:
    """
    This function tests to see whether the name entered is in  the file votes.csv
    and does this by grabbing the name, removing the whitespace, and putting all the
    words in lowercase to make sure there aren't other forms of the same voted id in the
    votes.csv file. If the name is not in the file, then name and the vote are added
    as a line to the csv file. If not, then nothing is added to the csv file. The variable
    returned is a boolean variable that is automatically set to true, and only sets to false
    when the voted id is in the csv file already.
    """
    test_name = name.replace(" ","")
    test_name_2 = test_name.lower()
    test = True
    with open('votes.csv', 'r+') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            for item in row:
                item_strip = item.replace(" ", "")
                item_lower = item_strip.lower()
                if item_lower == test_name_2:
                    test = False
        if test:
            writer = csv.writer(read_file)
            real_answer, rule = voting_numbers(answer)
            if rule:
                writer.writerow([name, real_answer])
    return test

def voting_numbers(answer, rule=False) -> tuple[str, bool]:
    """
    This function collects an answer and a boolean value rule , and
    checks the value of the answer to output a name and the same rule.
    If the value of answer is 1-3, the actual_answer is marked as the name of the
    candidate assigned to that value and returns both the name of the candidate, and the boolean
    rule now set to true. Otherwise, nothing happens and the actual_answer becomes an empty string, and
    the rule stays set to False.
    """
    actual_answer = ""
    if answer == 1:
        actual_answer = "Bianca"
        rule = True
    elif answer == 2:
        actual_answer = "Edward"
        rule = True
    elif answer == 3:
        actual_answer = "Felicia"
        rule = True
    return actual_answer, rule

def translate(answered) -> int:
    """
    This function takes in a string and attempts to translate it into an integer,
    if an error occurs in attempting that then the value of the variable is sat to
    0, and then the variable answered is returned.
    """
    try:
        return int(answered)
    except:
        answered = 0
    finally:
        return answered

def total(self) -> None:
    """
    This function will create a dictionary with our candidates and start them out with
    zero votes. The function will then search through the csv file and add 1 to their
    value every time the candidate's name appears in the file. Then the GUI will be
    sent an output screen where each of the candidate's total votes are displayed.
    """
    name_count = {"Bianca": 0, "Edward": 0, "Felicia": 0}
    with open('votes.csv', 'r') as reader:
            real_reader = csv.reader(reader)
            for row in real_reader:
                if row[1] in name_count.keys():
                    name_count[row[1]] += 1
            self.label_nine.config(text=f'Bianca: {name_count.get('Bianca')}, Edward: {name_count.get('Edward')}, Felicia: {name_count.get('Felicia')}', fg="blue")

def get_voting(self) -> None:
    """
    This function will output different phrases to the GUI screen based on certain conditions.
    If person chose a candidate then the first if statement will go, and then if the voter id
    is not in the csv file, then the name and vote will be added and a Thanks for Voting! phrase
    will be output to the GUI. Otherwise, the output will be displayed as You Already Voted!.
    If a candidate was not chosen, then the GUI screen will output Please Select a Candidate!
    """
    radio_answer = self.radio_answer.get()
    radio_answer = translate(radio_answer)
    input_name = self.input_name.get()
    if 1 <= radio_answer <= 3:
        if voting(radio_answer, input_name):
            self.input_name.delete(0, END)
            self.radio_answer.set(0)
            self.label_nine.config(text=f'Thanks for voting {voting_numbers(radio_answer)[0]}!', fg='black')
        else:
            self.input_name.delete(0, END)
            self.radio_button1.deselect()
            self.radio_button2.deselect()
            self.radio_button3.deselect()
            self.label_nine.config(text="You have already voted!", fg="red")
    else:
        self.label_nine.config(text="Please Select a Candidate!", fg="red")
