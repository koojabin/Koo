from random import randint

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLCDNumber
from PyQt5.QtWidgets import QPushButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
import time
import sys

board = [[0 for i in range(10)] for j in range(10)]
count = 1
for i in range(0,10):
    board[0][i] = -1
    board[i][0] = -1
    board[9][i] = -1
    board[i][9] = -1

class othello(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('othello')
        self.setWindowIcon(QIcon('othello_icon.png'))

        #시작 버튼
        self.StartButton = QPushButton('start')
        self.StartButton.clicked.connect(self.buttonClicked)

        #그리드 버튼
        self.BoardButton = [[0 for i in range(10)] for j in range(10)]
        for i in range(1,9):
            for j in range(1,9):
                self.BoardButton[i][j] = QPushButton()
                self.BoardButton[i][j].setMaximumHeight(1000)
                self.BoardButton[i][j].setText(str(i) + str(j))
                self.BoardButton[i][j].setStyleSheet('QPushButton {color: white;}')
                self.BoardButton[i][j].setFont(QFont('Arial', 1))
                self.BoardButton[i][j].clicked.connect(self.buttonClicked)


        self.PlayerLable = QLabel('Player: ', )
        self.TimerLabel = QLabel('Timer: ',)
        self.ComLable = QLabel('Com: ',)

        self.PlayerScore = QLineEdit()
        self.PlayerScore.setReadOnly(True)
        self.TimerLine = QLineEdit()
        self.TimerLine.setReadOnly(True)
        self.ComScore = QLineEdit()
        self.ComScore.setReadOnly(True)

        OthelloBoard = QPixmap('othelloBoard.jpeg')
        OthelloBoard_img = QLabel()
        OthelloBoard_img.setPixmap(OthelloBoard)

        self.StartBox = QHBoxLayout()
        self.StartBox.addWidget(self.StartButton)

        BoardBox1 = QHBoxLayout()
        for i in range(1,9):
            BoardBox1.addWidget(self.BoardButton[1][i])
        BoardBox2 = QHBoxLayout()
        for i in range(1, 9):
            BoardBox2.addWidget(self.BoardButton[2][i])
        BoardBox3 = QHBoxLayout()
        for i in range(1, 9):
            BoardBox3.addWidget(self.BoardButton[3][i])
        BoardBox4 = QHBoxLayout()
        for i in range(1, 9):
            BoardBox4.addWidget(self.BoardButton[4][i])
        BoardBox5 = QHBoxLayout()
        for i in range(1, 9):
            BoardBox5.addWidget(self.BoardButton[5][i])
        BoardBox6 = QHBoxLayout()
        for i in range(1, 9):
            BoardBox6.addWidget(self.BoardButton[6][i])
        BoardBox7 = QHBoxLayout()
        for i in range(1, 9):
            BoardBox7.addWidget(self.BoardButton[7][i])
        BoardBox8 = QHBoxLayout()
        for i in range(1, 9):
            BoardBox8.addWidget(self.BoardButton[8][i])

        # BoardBox = QHBoxLayout()
        # BoardBox.addWidget(OthelloBoard_img)     #오델로판 이미지

        ScoreTimerBox = QHBoxLayout()
        ScoreTimerBox.addWidget(self.PlayerLable)
        ScoreTimerBox.addWidget(self.PlayerScore)
        ScoreTimerBox.addWidget(self.TimerLabel)
        ScoreTimerBox.addWidget(self.TimerLine)
        ScoreTimerBox.addWidget(self.ComLable)
        ScoreTimerBox.addWidget(self.ComScore)

        ShowBox = QVBoxLayout()
        ShowBox.addLayout(self.StartBox)
        ShowBox.addLayout(BoardBox1)
        ShowBox.addLayout(BoardBox2)
        ShowBox.addLayout(BoardBox3)
        ShowBox.addLayout(BoardBox4)
        ShowBox.addLayout(BoardBox5)
        ShowBox.addLayout(BoardBox6)
        ShowBox.addLayout(BoardBox7)
        ShowBox.addLayout(BoardBox8)
        ShowBox.addLayout(ScoreTimerBox)

        self.setGeometry(300, 300, 350, 700)
        self.setLayout(ShowBox)


        # self.tableWidget = QTableWidget(self)
        # self.tableWidget.resize(1000,1000)
        # self.tableWidget.setRowCount(8)
        # self.tableWidget.setColumnCount(8)

        #BoardSize = QLabel('Width: '+str(OthelloBoard.width())+ ',Height: '+str(OthelloBoard.height())) 오델로판의 크기

        # grid = QGridLayout()                      #그리드를 이용해 배치하다가 크기가 달라 인덱스 배치가 이상하게 되어 박스레이아웃 이용
        # self.setLayout(grid)
        # grid.addWidget(StartButton, 0, 0)
        # grid.addWidget(OthelloBoard_img, 1, 0)
        # grid.addWidget(QLabel('Player: '), 2, 0)
        # grid.addWidget(QLineEdit(), 2, 1)
        # grid.addWidget(QLabel('timer: '), 2, 2)
        # grid.addWidget(QLineEdit(), 2, 3)
        # grid.addWidget(QLabel('Com: '), 2, 4)
        # grid.addWidget(QLineEdit(), 2, 5)



    def buttonClicked(self):
        key = self.sender().text()
        boardindex = -1
        if key != 'start':
            boardindex = int(key)
            index_i = int(boardindex/10)
            index_j = int(boardindex%10)
            print(board[index_i][index_j])
        if key == 'start': #게임 스타
            turn(self)
            self.StartButton.setEnabled(False)
            GameStart(self)

        if boardindex != -1:

            if board[index_i][index_j] == 3:
                board[index_i][index_j] = 1
                self.BoardButton[index_i][index_j].setStyleSheet('background:black')
                PlayerChangeButton(self, index_i, index_j)
                for i in range(1, 9):
                    for j in range(1, 9):
                        if board[i][j] == 3 or board[i][j] == 4:
                            board[i][j] = 0
                            self.BoardButton[i][j].setStyleSheet('background:None')
                ComShowClicked(self)
                ComAI(self)
        GameScore(self)
        PlayerShowClicked(self)

def ComAI(self):
    comcount = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 4:
                comcount += 1
    x = randint(0,3)
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 4:
                x -= 1
                if x == 0:
                    board[i][j] = 2
                    self.BoardButton[i][j].setStyleSheet('background:green')
                    ComChangeButton(self, i, j)

def ComChangeButton(self, i, j):
    dir_x = 0
    dir_y = 0
    if board[i-1][j] == 1:
        dir_x -= 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_x -= 1
        if board[i+dir_x][j+dir_y] == 2:
            dir_x = -1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_x -= 1
        dir_x = 0
    if board[i+1][j] == 1:
        dir_x += 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_x += 1
        if board[i+dir_x][j+dir_y] == 2:
            dir_x = 1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_x += 1
        dir_x = 0
    if board[i][j-1] == 1:
        dir_y -= 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_y -= 1
        if board[i+dir_x][j+dir_y] == 2:
            dir_y = -1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_x -= 1
        dir_y = 0
    if board[i][j+1] == 1:
        dir_y += 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_y += 1
        if board[i+dir_x][j+dir_y] == 2:
            dir_y = 1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_y += 1
        dir_y = 0
    if board[i-1][j-1] == 1:
        dir_x -= 1
        dir_y -= 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_x -= 1
            dir_y -= 1
        if board[i+dir_x][j+dir_y] == 2:
            dir_x = -1
            dir_y = -1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_x -= 1
                dir_y -= 1
        dir_x = 0
        dir_y = 0
    if board[i-1][j+1] == 1:
        dir_x -= 1
        dir_y += 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_x -= 1
            dir_y += 1
        if board[i+dir_x][j+dir_y] == 2:
            dir_x = -1
            dir_y = 1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_x -= 1
                dir_y += 1
        dir_x = 0
        dir_y = 0
    if board[i+1][j-1] == 1:
        dir_x += 1
        dir_y -= 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_x += 1
            dir_y -= 1
        if board[i+dir_x][j+dir_y] == 2:
            dir_x = 1
            dir_y = -1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_x += 1
                dir_y -= 1
        dir_x = 0
        dir_y = 0
    if board[i+1][j+1] == 1:
        dir_x += 1
        dir_y += 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_x += 1
            dir_y += 1
        if board[i+dir_x][j+dir_y] == 2:
            dir_x = +1
            dir_y = +1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_x += 1
                dir_y += 1

def ComShowClicked(self):
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 4 or board[i][j] == 3:
                board[i][j] = 0
    dir_x = 0
    dir_y = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 2:
                if board[i - 1][j] == 1:
                    dir_x -= 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x -= 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                if board[i + 1][j] == 1:
                    dir_x += 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x += 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                if board[i][j - 1] == 1:
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_y -= 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 4
                    dir_y = 0
                if board[i][j + 1] == 1:
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_y += 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 4
                    dir_y = 0
                if board[i - 1][j - 1] == 1:
                    dir_x -= 1
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x -= 1
                        dir_y -= 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                    dir_y = 0
                if board[i - 1][j + 1] == 1:
                    dir_x -= 1
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x -= 1
                        dir_y += 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                    dir_y = 0
                if board[i + 1][j - 1] == 1:
                    dir_x += 1
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x += 1
                        dir_y -= 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                    dir_y = 0
                if board[i + 1][j + 1] == 1:
                    dir_x += 1
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x += 1
                        dir_y += 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                    dir_y = 0

def PlayerChangeButton(self, i, j): #버튼의 색깔을 바꾸어준
    dir_x = 0
    dir_y = 0
    if board[i-1][j] == 2:
        dir_x -= 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_x -= 1
        if board[i+dir_x][j+dir_y] == 1:
            dir_x = -1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_x -= 1
        dir_x = 0
    if board[i+1][j] == 2:
        dir_x += 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_x += 1
        if board[i+dir_x][j+dir_y] == 1:
            dir_x = 1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_x += 1
        dir_x = 0
    if board[i][j-1] == 2:
        dir_y -= 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_y -= 1
        if board[i+dir_x][j+dir_y] == 1:
            dir_y = -1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_x -= 1
        dir_y = 0
    if board[i][j+1] == 2:
        dir_y += 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_y += 1
        if board[i+dir_x][j+dir_y] == 1:
            dir_y = 1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_y += 1
        dir_y = 0
    if board[i-1][j-1] == 2:
        dir_x -= 1
        dir_y -= 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_x -= 1
            dir_y -= 1
        if board[i+dir_x][j+dir_y] == 1:
            dir_x = -1
            dir_y = -1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_x -= 1
                dir_y -= 1
        dir_x = 0
        dir_y = 0
    if board[i-1][j+1] == 2:
        dir_x -= 1
        dir_y += 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_x -= 1
            dir_y += 1
        if board[i+dir_x][j+dir_y] == 1:
            dir_x = -1
            dir_y = 1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_x -= 1
                dir_y += 1
        dir_x = 0
        dir_y = 0
    if board[i+1][j-1] == 2:
        dir_x += 1
        dir_y -= 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_x += 1
            dir_y -= 1
        if board[i+dir_x][j+dir_y] == 1:
            dir_x = 1
            dir_y = -1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_x += 1
                dir_y -= 1
        dir_x = 0
        dir_y = 0
    if board[i+1][j+1] == 2:
        dir_x += 1
        dir_y += 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_x += 1
            dir_y += 1
        if board[i+dir_x][j+dir_y] == 1:
            dir_x = +1
            dir_y = +1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_x += 1
                dir_y += 1

def GameStart(self): #시작할  흑백 돌 랜덤 배치
    x = randint(1, 11)
    for i in range(4, 6):
        for j in range(4, 6):
            if (x % 2 == 0):
                if (i == j):
                    self.BoardButton[i][j].setStyleSheet('background:black')
                    self.BoardButton[i][j].setEnabled(False)
                    board[i][j] = 1  # 검은색은 1
                else:
                    self.BoardButton[i][j].setStyleSheet('background:green')
                    self.BoardButton[i][j].setEnabled(False)
                    board[i][j] = 2  # 흰색은 2
            else:
                if (i == j):
                    self.BoardButton[i][j].setStyleSheet('background:green')
                    self.BoardButton[i][j].setEnabled(False)
                    board[i][j] = 2
                else:
                    self.BoardButton[i][j].setStyleSheet('background:black')
                    self.BoardButton[i][j].setEnabled(False)
                    board[i][j] = 1

def PlayerShowClicked(self): #배치 가능한 곳을 보여줌
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 3 or board[i][j] == 4:
                board[i][j] = 0
                self.BoardButton[i][j].setStyleSheet('background:None')
    dir_x = 0
    dir_y = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 1:
                if board[i - 1][j] == 2:
                    dir_x = -1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_x -= 1
                    if board[i+dir_x][j+dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                if board[i + 1][j] == 2:
                    dir_x += 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_x += 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                if board[i][j - 1] == 2:
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_y -= 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_y = 0
                if board[i][j + 1] == 2:
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_y += 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_y = 0
                if board[i - 1][j - 1] == 2:
                    dir_x -= 1
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_x -= 1
                        dir_y -= 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                    dir_y = 0
                if board[i - 1][j + 1] == 2:
                    dir_x -= 1
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_x -= 1
                        dir_y += 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                    dir_y = 0
                if board[i + 1][j - 1] == 2:
                    dir_x += 1
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_x += 1
                        dir_y -= 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                    dir_y = 0
                if board[i + 1][j + 1] == 2:
                    dir_x += 1
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_x += 1
                        dir_y += 1
                    if board[i + dir_x][j + dir_y] == 0:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                    dir_y = 0

def GameScore(self):
    playerScore = 0
    comScore = 0
    for i in range(1,9):
        for j in range(1,9):
            if board[i][j] == 1:
                playerScore += 1
            elif board[i][j] ==2:
                comScore += 1
    self.PlayerScore.setText(str(playerScore))
    self.ComScore.setText(str(comScore))

def turn(self):
   if (count % 2 != 0):
       self.PlayerLable.setStyleSheet("color : blue;"
                                      "background-color: #87CEFA;"
                                      "border-style: solid;"
                                      "border-width: 3px;"
                                      "border-color: #1E90FF")
   else:
       self.ComLable.setStyleSheet("color : blue;"
                                      "background-color: #87CEFA;"
                                      "border-style: solid;"
                                      "border-width: 3px;"
                                      "border-color: #1E90FF")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    othe = othello()
    othe.show()
    sys.exit(app.exec_())
