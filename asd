#board리스트 -1: 바둑판 밖 0: 아무것도 놓여있지 않은 상태 1: 플레이어의 바둑알이 놓여져있는 상태 2: 컴퓨터의 바둑알이 놓여져있는 상태 
#           3: 플레이어가 바둑알을 놓을 수 있는 곳 4: 컴퓨터가 바둑알을 놓을수 있는 곳

from random import randint
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLCDNumber
from PyQt5.QtWidgets import QPushButton, QLabel, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
import time
import sys

board = [[0 for i in range(10)] for j in range(10)] #바둑알이 8*8판을 나가서 인덱스에러 방지를 위하여 10*10으로 만들고 0으로 초기화 해줌
count = 1
for i in range(0,10): #둘레에 -1값을 넣어줌으로써 board의 값이 -1이면 나가지 못하게 함으로써 오류
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



    def buttonClicked(self): #버튼이 클릭되면 발생
        key = self.sender().text()
        boardindex = -1 #BoardButton을 누르면 값을 바꿔줌으로써 눌렸을 때만 실행되게 해주기 위한 변수 
        if key != 'start':  #BoardButton이 눌렸을 때 실행
            boardindex = int(key)
            index_i = int(boardindex/10) #BoardButton의 행과 열의 인덱스를 저장
            index_j = int(boardindex%10)
        if key == 'start':  #스타트버튼을 누르면 실행
            turn(self)  #자기 턴임을 보여줌
            self.StartButton.setEnabled(False)  #스타트버튼을 비활성화함으로써 다시 클릭이 안되게 만듬
            GameStart(self)

        if boardindex != -1: #BoardButton이 눌렸을 때 실행
            if board[index_i][index_j] == 3:    #플레이어가 둘 수 있는 곳이 있는지 확인
                board[index_i][index_j] = 1
                self.BoardButton[index_i][index_j].setStyleSheet('background:black')
                PlayerChangeButton(self, index_i, index_j)
                PlayerClear(self)
                GameEndMission(self) #플레이어가 바둑알을 두고 게임이 끝났는지 확인
                ComShowClicked(self)
                for i in range(1, 9):   
                    for j in range(1, 9):
                        if board[i][j] == 4:    #컴퓨터가 둘 수 있는 곳이 확인
                            ComAI(self)
                            break
                    if board[i][j] == 4:
                        break
                GameEndMission(self)    #컴퓨터가 바둑알을 두고 게임이 끝났는지 확인
                while True: #플레이어가 둘 곳이 없을 때 컴퓨터에게 턴이 다시 돌아가 컴퓨터가 다시 두게 함
                    PlayerShowClicked(self)
                    a = 0
                    for i in range(1,9):
                        for j in range(1,9):
                            if board[i][j] == 3:
                                a = 1
                    if a == 1:
                        break
                    elif a == 0:
                        ComShowClicked(self)
                        ComAI(self)
                        ComClear(self)
                        GameEndMission(self)
                ComClear(self)
        GameScore(self)
        PlayerShowClicked(self)

def PlayerClear(self):  #플레이어의 턴이 끝나고 플레이어가 둘 수 있던 곳의 값들을 초기화
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 3:
                board[i][j] = 0
                self.BoardButton[i][j].setStyleSheet('background:None')

def ComClear(self): #컴퓨터의 턴이 끝나고 플레이어가 둘 수 있던 곳의 값들을 초기화
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 4:
                board[i][j] = 0
                self.BoardButton[i][j].setStyleSheet('background:None')

def ComAI(self):
    print('aaa')
    comcount = 0
    for i in range(1, 9):   #컴퓨터가 둘 수 있는 곳의 수를 count함
        for j in range(1, 9):
            if board[i][j] == 4:
                comcount += 1
    x = randint(1,comcount) #컴퓨터가 둘 곳을 랜덤으로 뽑음
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 4:
                x -= 1
                if x == 0:
                    board[i][j] = 2
                    self.BoardButton[i][j].setStyleSheet('background:green')
                    ComChangeButton(self, i, j)


def ComChangeButton(self, i, j):    #자신이 바둑알을 둔 곳의 상하좌우, 대각선을 검사해주고 있다면 그 방향으로 dir을 저장해주고 상대편의 돌이 나오지 않을 때까지 그 방향으로 계속 진행
    print('bbb')                    #자기의 색깔이 나온다면 지금까지 왔던 길의 알을 자기의 색깔로 바꾸어줌. 그리고 다음 if문을 위해 dir값 초기화
    dir_x = 0
    dir_y = 0
    if board[i-1][j] == 1:
        dir_x -= 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_x -= 1
        if board[i+dir_x][j+dir_y] == 2 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 2 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 2 and board[i+dir_x][j+dir_y] != -1:
            dir_y = -1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_y -= 1
        dir_y = 0
    if board[i][j+1] == 1:
        dir_y += 1
        while board[i+dir_x][j+dir_y] == 1:
            dir_y += 1
        if board[i+dir_x][j+dir_y] == 2 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 2 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 2 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 2 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 2 and board[i+dir_x][j+dir_y] != -1:
            dir_x = +1
            dir_y = +1
            while board[i + dir_x][j + dir_y] == 1:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:green')
                board[i + dir_x][j + dir_y] = 2
                dir_x += 1
                dir_y += 1
            dir_x = 0
            dir_y = 0

def ComShowClicked(self):   #자신이 둘 수있는 곳을 보여줌
    print('ccc')
    for i in range(1, 9):   #자신이 전에 저장해준 값을 초기화 해줌
        for j in range(1, 9):
            if board[i][j] == 4:
                board[i][j] = 0
    dir_x = 0
    dir_y = 0
    for i in range(1, 9):   #ChangeButton함수와 비슷함. 하지만 ShowClicked함수는 끝에 board의 값이 0이여야지 둘 수 있는 곳이기 때문에 조건의 값이 0임
        for j in range(1, 9):
            if board[i][j] == 2:
                if board[i - 1][j] == 1:
                    dir_x -= 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x -= 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                if board[i + 1][j] == 1:
                    dir_x += 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x += 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                if board[i][j - 1] == 1:
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_y -= 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 4
                    dir_y = 0
                if board[i][j + 1] == 1:
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_y += 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 4
                    dir_y = 0
                if board[i - 1][j - 1] == 1:
                    dir_x -= 1
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x -= 1
                        dir_y -= 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                    dir_y = 0
                if board[i - 1][j + 1] == 1:
                    dir_x -= 1
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x -= 1
                        dir_y += 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                    dir_y = 0
                if board[i + 1][j - 1] == 1:
                    dir_x += 1
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x += 1
                        dir_y -= 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                    dir_y = 0
                if board[i + 1][j + 1] == 1:
                    dir_x += 1
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 1:
                        dir_x += 1
                        dir_y += 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 4
                    dir_x = 0
                    dir_y = 0

def PlayerChangeButton(self, i, j): #위에 함수와 값만 다르고 기능은 같음
    print('ddd')
    dir_x = 0
    dir_y = 0
    if board[i-1][j] == 2:
        dir_x -= 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_x -= 1
        if board[i+dir_x][j+dir_y] == 1 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 1 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 1 and board[i+dir_x][j+dir_y] != -1:
            dir_y = -1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_y -= 1
        dir_y = 0
    if board[i][j+1] == 2:
        dir_y += 1
        while board[i+dir_x][j+dir_y] == 2:
            dir_y += 1
        if board[i+dir_x][j+dir_y] == 1 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 1 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 1 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 1 and board[i+dir_x][j+dir_y] != -1:
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
        if board[i+dir_x][j+dir_y] == 1 and board[i+dir_x][j+dir_y] != -1:
            dir_x = +1
            dir_y = +1
            while board[i + dir_x][j + dir_y] == 2:
                self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:black')
                board[i + dir_x][j + dir_y] = 1
                dir_x += 1
                dir_y += 1
        dir_x = 0
        dir_y = 0

def GameStart(self): #시작할 가운데 부분의 흑백 돌을 대각선 방향으로 랜덤 배치
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

def PlayerShowClicked(self): #위에 함수와 값만 다르고 기능은 같음
    print('eee')
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 3:
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
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                if board[i + 1][j] == 2:
                    dir_x += 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_x += 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                if board[i][j - 1] == 2:
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_y -= 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_y = 0
                if board[i][j + 1] == 2:
                    dir_y += 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_y += 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_y = 0
                if board[i - 1][j - 1] == 2:
                    dir_x -= 1
                    dir_y -= 1
                    while board[i + dir_x][j + dir_y] == 2:
                        dir_x -= 1
                        dir_y -= 1
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
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
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
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
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
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
                    if board[i+dir_x][j+dir_y] == 0 and board[i+dir_x][j+dir_y] != -1:
                        board[i+dir_x][j+dir_y] = 3
                        self.BoardButton[i + dir_x][j + dir_y].setStyleSheet('background:yellow')
                    dir_x = 0
                    dir_y = 0

def GameScore(self):    #board의 인덱스를 다 검사해주며 플레이어와 컴퓨터의 score를 보여줌
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

def turn(self): #자신의 턴일때 색깔을 나타냄
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

def GameEnd(self): #게임이 종료될 때 누가 승리하였는지 보여주고 다시 할것인지 종료할지 정함
   EndBox = QMessageBox()
   EndBox.setWindowTitle("Game End!")
   if self.PlayerScore.text() > self.ComScore.text():
       EndBox.setText("You Win!")
       EndBox.setInformativeText("One More?")
   elif self.ComScore.text() > self.PlayerScore.text():
       EndBox.setText("You Lose!")
       EndBox.setInformativeText("One More?")
   else:
       EndBox.setText("Draw!")
       EndBox.setInformativeText("One More?")
   EndBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
   EndBox.setDefaultButton(QMessageBox.Yes)

   retval = EndBox.exec_()

   if retval == QMessageBox.Yes: #종료한다면 초기화를 해줌 <<이건 아직 미완성임
       self.StartButton.setEnabled(True)
       GameStart(self)
       for i in range(1, 9):
           for j in range(1, 9):
               board[i][j] = 0
               self.BoardButton[i][j].setStyleSheet('background:None')

   else:
       sys.exit()

def GameEndMission(self): #게임이 끝났는지 더 할 수 있는지 검사
    end = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 0:
                end = 1
    if end == 0:
        return GameEnd(self)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    othe = othello()
    othe.show()
    sys.exit(app.exec_())
