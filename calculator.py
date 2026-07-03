from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(600, 200, 400, 400)
        self.error = False
        self.ui()

    def ui(self):
        font = QFont("Halvetica", 25)
        mainLayout = QVBoxLayout()
        hbox = QHBoxLayout()
        self.result = QLineEdit()
        self.result.setStyleSheet("background-color:green; color:white")
        self.result.setFont(font)
        self.grid = QGridLayout()
        self.clear = QPushButton("Clear")
        self.clear.setStyleSheet("background-color: yellow")
        self.clear.clicked.connect(self.clear_button)
        self.delete = QPushButton("<")
        self.delete.clicked.connect(self.delete_button)
        self.delete.setStyleSheet("background-color: yellow")
        self.make_buttons()
        hbox.addWidget(self.clear)
        hbox.addWidget(self.delete)
        mainLayout.addWidget(self.result)
        mainLayout.addLayout(self.grid)
        mainLayout.addLayout(hbox)
        self.setLayout(mainLayout)
        self.setStyleSheet("QPushButton{font: 17pt Comic Sans Ms; padding: 10px}")
        self.show()

    def make_buttons(self):
        button_map = (
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
        )
        for i in range(len(button_map)):
            for j in range(len(button_map[i])):
                btn = QPushButton(button_map[i][j])
                btn.clicked.connect(self.arthmetic_button)
                if j < 3:
                    btn.setStyleSheet("background-color: rgb(150, 50, 150)")
                else:
                    btn.setStyleSheet("background-color: rgb(180, 100, 50)")
                self.grid.addWidget(btn, i, j)

    def arthmetic_button(self):
        id = self.sender()
        symbol = id.text()
        if self.error:
            self.clear_button()
            self.error = False
        if symbol in ('+', '-', '*', '/'):
            if (self.result.text()[-1] != symbol):
                new = self.result.text() + symbol
                self.result.setText(new)
        elif symbol == '.':
            if len(self.result.text()) == 0:
                new = '0' + self.result.text()
                self.result.setText(new)
            if self.result.text()[-1] != symbol:
                new = self.result.text() + symbol
                self.result.setText(new)
        elif symbol == '=':
            if self.result.text()[-1] == '.':
                new = self.result.text() + '0'
                self.result.setText(new)
            elif self.result.text()[-1] in ('+', '-', '*', '/'):
                new = self.result.text() * 2
                self.result.setText(new[:-1])
            try:
                result = str(eval(self.result.text()))
                self.result.setText(result)
            except:
                self.error = True
                self.result.setText("ERROR")
        else:
            text = self.result.text()
            if text or (not text and symbol != '0'):
                new = self.result.text() + symbol
                self.result.setText(new)

    def clear_button(self):
        self.result.setText('')

    def delete_button(self):
        if self.result.text():
            self.result.setText(self.result.text()[:-1])

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
