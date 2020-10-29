import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pickle
import datetime



class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.dbfilename = 'assignment3.dat'
        self.initUI()
        self.scoredb = []
        self.doScoreDB()
        self.writeScoreDB()

    def initUI(self):
        label1 = QLabel('Name: ', self)
        label2 = QLabel('Age: ', self)
        label3 = QLabel('Score: ', self)
        label4 = QLabel('Amount: ', self)
        label5 = QLabel('Key: ', self)
        label6 = QLabel('Result: ', self)


        self.Name = QLineEdit()
        self.Age = QLineEdit()
        self.Score = QLineEdit()
        self.Amount = QLineEdit()

        self.cb = QComboBox()
        self.cb.addItem('Name')
        self.cb.addItem('Age')
        self.cb.addItem('Score')


        btn1 = QPushButton('Add')
        btn2 = QPushButton('Del')
        btn3 = QPushButton('Find')
        btn4 = QPushButton('Inc')
        btn5 = QPushButton('show')

        self.Result = QTextEdit()

        line1 = QHBoxLayout()
        line1.addStretch(1)
        line1.addWidget(label1)
        line1.addWidget(self.Name)
        line1.addWidget(label2)
        line1.addWidget(self.Age)
        line1.addWidget(label3)
        line1.addWidget(self.Score)

        line2 = QHBoxLayout()
        line2.addStretch(1)
        line2.addWidget(label4)
        line2.addWidget(self.Amount)
        line2.addWidget(label5)
        line2.addWidget(self.cb)

        line3 = QHBoxLayout()
        line3.addStretch(1)
        line3.addWidget(btn1)
        line3.addWidget(btn2)
        line3.addWidget(btn3)
        line3.addWidget(btn4)
        line3.addWidget(btn5)

        line4 = QHBoxLayout()
        line4.addWidget(label6)

        line5 = QHBoxLayout()
        line5.addWidget(self.Result)

        layout = QVBoxLayout()
        layout.addLayout(line1)
        layout.addLayout(line2)
        layout.addLayout(line3)
        layout.addStretch(1)
        layout.addLayout(line4)
        layout.addLayout(line5)

        self.setLayout(layout)

        self.setWindowTitle('Assignment6')
        self.setGeometry(100, 100, 500, 300)
        self.show()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scdb = []
            return

        try:
            self.scdb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()

    def doScoreDB(self):
        while (True):
            try:
                inputstr = (input("Score DB > "))
                if inputstr == "": continue
                parse = inputstr.split(" ")
                if self.btn1.setCheckable(True):
                    record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                    self.scdb += [record]
                elif self.btn2.setCheckable(True):
                    for p in sorted(self.scdb, key=lambda person: person['Name']):
                        for p in self.scdb:
                            if p['Name'] == parse[1]:
                                self.scdb.remove(p)
                elif self.btn5.setCheckable(True):
                    sortKey = 'Name' if len(parse) == 1 else parse[1]
                    self.showScoreDB(self.scdb, sortKey)
                elif self.btn3.setCheckable(True):
                    for p in self.scdb:
                        if p['Name'] == parse[1]:
                            for attr in sorted(p):
                                self.Result.append(attr + "=" + str(p[attr]), end=' ')
                            pass
                elif self.btn4.setCheckable(True):
                    for p in self.scdb:
                        if p['Name'] == parse[1]:
                            p['Score'] += int(parse[2])
                else:
                    self.Result.append("Invalid command: " + parse[0])
            except:
                self.Result.append('UnKnown Error')

    def showScoreDB(self, keyname):
        for p in sorted(self.scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                self.Result.append(attr + "=" + str(p[attr]), end=' ')
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
