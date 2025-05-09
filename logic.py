from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Runs the radio_clicked function anytime a candidate is chosen.
        Runs the vote functions when the vote button is clicked.
        """
        super().__init__()
        self.setupUi(self)
        self.jane.toggled.connect(self.radio_clicked)
        self.joe.toggled.connect(self.radio_clicked)
        self.john.toggled.connect(self.radio_clicked)
        self.button_vote.clicked.connect(lambda: self.vote())

    def radio_clicked(self, enabled):
        """
        Asks the user to verify there selection.
        :param enabled: Is checked when a candidate is clicked.
        :return: A message to verify there choice
        """
        if enabled:
            self.label_message.setText("Please verify candidate and select vote!")


    def vote(self):
        """
        Sends the users Student ID number and there vote selection to a csv file
        """
        student_id = ''
        student_id = self.id.text()


        try:
            if student_id == '':
                raise ValueError
        except ValueError:
            self.label_message.setText("Please enter in a Student ID")
            return

        try:
            if len(student_id) != 8:
                raise ValueError
            student_id = int(student_id)
        except ValueError:
            self.label_message.setText("Invalid ID. Must be 8 digits.")
            self.label_message.setStyleSheet("color: red;")
            return


        vote: str = ""
        if self.john.isChecked():
            vote = 'John'
        elif self.joe.isChecked():
            vote = 'Joe'
        elif self.jane.isChecked():
            vote = 'Jane'
        elif vote == '':
            self.label_message.setText("Please select a candidate.")
            self.label_message.setStyleSheet("color: red;")
            return

        with open("results.csv", 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row and str(student_id) == row[0]:
                    self.label_message.setText("This student has already voted.")
                    self.label_message.setStyleSheet("color: red;")
                    return

        with open('results.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([student_id, vote])
            self.label_message.setText("Vote submitted!")
            self.label_message.setStyleSheet("color: blue;")

        self.id.clear()

        if self.candidates.checkedButton() is not None:
            self.candidates.setExclusive(False)
            self.candidates.checkedButton().setChecked(False)
            self.candidates.setExclusive(True)








