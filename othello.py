from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
import sys

class othello(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('othello')
        self.setWindowIcon(QIcon('othello_icon.png'))

        StartButton = QPushButton('start', self)
        self.BoardButton = [[0 for i in range(8)] for j in range(8)]
        for i in range(0,8):
            for j in range(0,8):
                self.BoardButton[i][j] = QPushButton()

        PlayerLable = QLabel('Player: ', self)
        TimerLabel = QLabel('Timer: ', self)
        ComLable = QLabel('Com: ', self)

        PlayerScore = QLineEdit(self)
        TimerLine = QLineEdit(self)
        ComScore = QLineEdit(self)

        OthelloBoard = QPixmap('othelloBoard.jpeg')
        OthelloBoard_img = QLabel()
        OthelloBoard_img.setPixmap(OthelloBoard)

        StartBox = QHBoxLayout()
        StartBox.addWidget(StartButton)

        BoardBox1 = QHBoxLayout()
        for i in range(0,8):
            BoardBox1.addWidget(self.BoardButton[0][i])
        BoardBox2 = QHBoxLayout()
        for i in range(0, 8):
            BoardBox2.addWidget(self.BoardButton[1][i])
        BoardBox3 = QHBoxLayout()
        for i in range(0, 8):
            BoardBox3.addWidget(self.BoardButton[2][i])
        BoardBox4 = QHBoxLayout()
        for i in range(0, 8):
            BoardBox4.addWidget(self.BoardButton[3][i])
        BoardBox5 = QHBoxLayout()
        for i in range(0, 8):
            BoardBox5.addWidget(self.BoardButton[4][i])
        BoardBox6 = QHBoxLayout()
        for i in range(0, 8):
            BoardBox6.addWidget(self.BoardButton[5][i])
        BoardBox7 = QHBoxLayout()
        for i in range(0, 8):
            BoardBox7.addWidget(self.BoardButton[6][i])
        BoardBox8 = QHBoxLayout()
        for i in range(0, 8):
            BoardBox8.addWidget(self.BoardButton[7][i])

        # BoardBox = QHBoxLayout()
        # BoardBox.addWidget(OthelloBoard_img)     #오델로판 이미지

        ScoreTimerBox = QHBoxLayout()
        ScoreTimerBox.addWidget(PlayerLable)
        ScoreTimerBox.addWidget(PlayerScore)
        ScoreTimerBox.addWidget(TimerLabel)
        ScoreTimerBox.addWidget(TimerLine)
        ScoreTimerBox.addWidget(ComLable)
        ScoreTimerBox.addWidget(ComScore)

        ShowBox = QVBoxLayout()
        ShowBox.addLayout(StartBox)
        ShowBox.addLayout(BoardBox1)
        ShowBox.addLayout(BoardBox2)
        ShowBox.addLayout(BoardBox3)
        ShowBox.addLayout(BoardBox4)
        ShowBox.addLayout(BoardBox5)
        ShowBox.addLayout(BoardBox6)
        ShowBox.addLayout(BoardBox7)
        ShowBox.addLayout(BoardBox8)
        ShowBox.addLayout(ScoreTimerBox)

        self.setGeometry(300, 300, 350, 300)
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

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    othe = othello()
    othe.show()
    sys.exit(app.exec_())
