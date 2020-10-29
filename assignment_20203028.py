import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pickle
import datetime

dbfilename = 'assignment3.dat'

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        scoredb = self.readScoreDB()
        self.doScoreDB(scoredb)
        self.writeScoreDB(scoredb)

    def initUI(self):
        label1 = QLabel('Name: ', self)
        label1.move(20,5)
        label2 = QLabel('Age: ', self)
        label2.move(220, 5)
        label3 = QLabel('Score: ', self)
        label3.move(420, 5)
        label4 = QLabel('Amount: ', self)
        label4.move(235, 50)
        label5 = QLabel('Key: ', self)
        label5.move(420, 50)
        label6 = QLabel('Result: ', self)
        label6.move(20, 140)


        Name = QLineEdit(self)
        Name.move(60,5)
        Age = QLineEdit(self)
        Age.move(250, 5)
        Score = QLineEdit(self)
        Score.move(460, 5)
        Amount = QLineEdit(self)
        Amount.move(290, 50)

        cb = QComboBox(self)
        cb.addItem('Name')
        cb.addItem('Age')
        cb.addItem('Score')
        cb.move(460,50)


        btn1 = QPushButton('Add')
        btn2 = QPushButton('Del')
        btn3 = QPushButton('Find')
        btn4 = QPushButton('Inc')
        btn5 = QPushButton('show')

        te = QTextEdit()
        te.setAcceptRichText(False)
        te.resize(100,100)
        te.move(300,160)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        hbox.addWidget(btn5)
        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox)
        vbox.addStretch(3)

        self.setLayout(vbox)
        self.setWindowTitle('Assignment6')
        self.setGeometry(100, 100, 600, 300)
        self.show()

    def readScoreDB(self):
        try:
            fH = open(dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", dbfilename)
            return []

        scdb = []
        try:
            scdb = pickle.load(fH)
        except:
            print("Empty DB: ", dbfilename)
        else:
            print("Open DB: ", dbfilename)
        fH.close()
        return scdb

    # write the data into person db
    def writeScoreDB(scdb):
        fH = open(dbfilename, 'wb')
        pickle.dump(scdb, fH)
        fH.close()

    def doScoreDB(scdb, self):
        while (True):
            try:
                inputstr = (input("Score DB > "))
                if inputstr == "": continue
                parse = inputstr.split(" ")
                if self.btn1.setCheckable(True):
                    record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                    scdb += [record]
                elif self.btn2.setCheckable(True):
                    for p in sorted(scdb, key=lambda person: person['Name']):
                        for p in scdb:
                            if p['Name'] == parse[1]:
                                scdb.remove(p)
                elif self.btn5.setCheckable(True):
                    sortKey = 'Name' if len(parse) == 1 else parse[1]
                    self.showScoreDB(scdb, sortKey)
                elif self.btn3.setCheckable(True):
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            for attr in sorted(p):
                                print(attr + "=" + str(p[attr]), end=' ')
                            print()
                elif self.btn4.setCheckable(True):
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            p['Score'] += int(parse[2])
                else:
                    print("Invalid command: " + parse[0])
            except:
                print('UnKnown Error')

    def showScoreDB(scdb, keyname):
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end=' ')
            print()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())