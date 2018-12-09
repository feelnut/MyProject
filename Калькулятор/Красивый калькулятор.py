import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QLCDNumber


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Kalkulator.ui', self)
        self.setWindowTitle('Калькулятор')
        self.LCD.setDigitCount(15)
        self.checkalt = False

        self.str, self.znak, self.strall, self.numbers = '', [], '', []

        self.d.clicked.connect(self.df)
        self.s.clicked.connect(self.sf)
        self.p.clicked.connect(self.pf)
        self.ra.clicked.connect(self.raf)
        self.zap.clicked.connect(self.zapf)
        self.r.clicked.connect(self.rf)
        self.zero.clicked.connect(self.zerof)
        self.one.clicked.connect(self.onef)
        self.two.clicked.connect(self.twof)
        self.three.clicked.connect(self.threef)
        self.four.clicked.connect(self.fourf)
        self.five.clicked.connect(self.fivef)
        self.six.clicked.connect(self.sixf)
        self.seven.clicked.connect(self.sevenf)
        self.eight.clicked.connect(self.eightf)
        self.nine.clicked.connect(self.ninef)
        self.C.clicked.connect(self.Cf)
        self.sqrt.clicked.connect(self.sqrtf)
        self.sqr.clicked.connect(self.sqrf)
        self.delete1.clicked.connect(self.deletef)
        self.fact.clicked.connect(self.factf)
        self.drob.clicked.connect(self.drobf)
        self.procent.clicked.connect(self.procentf)
        self.tentotwo.clicked.connect(self.tentotwof)
        self.tentoeight.clicked.connect(self.tentoeightf)
        self.tentosixteen.clicked.connect(self.tentosixteenf)
        self.twototen.clicked.connect(self.twototenf)
        self.eighttoten.clicked.connect(self.eighttotenf)
        self.sixteentoten.clicked.connect(self.sixteentotenf)
        self.alt.clicked.connect(self.altf)

    def df(self):
        try:
            self.numbers.append(float(self.str))
            self.str = ''
            if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + self.znak)
                del self.znak[len(self.znak) - 1]
                self.znak.append('/')
            else:
                self.znak.append('/')
            self.primer.setText(self.strall)
        except ValueError:
            self.LCD.display('Error')

    def raf(self):
        try:
            self.numbers.append(float(self.str))
            self.str = ''
            if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + self.znak)
                del self.znak[len(self.znak) - 1]
                self.znak.append('-')
            else:
                self.znak.append('-')
            self.primer.setText(self.strall)
        except ValueError:
            self.LCD.display('Error')

    def sf(self):
        try:
            self.numbers.append(float(self.str))
            self.str = ''
            if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + self.znak)
                del self.znak[len(self.znak) - 1]
                self.znak.append('+')
            else:
                self.znak.append('+')
            self.primer.setText(self.strall)
        except ValueError:
            self.LCD.display('Error')

    def pf(self):
        try:
            self.numbers.append(float(self.str))
            self.str = ''
            if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + self.znak)
                del self.znak[len(self.znak) - 1]
                self.znak.append('*')
            else:
                self.znak.append('*')
            self.primer.setText(self.strall)
        except ValueError:
            self.LCD.display('Error')

    def altf(self):
        if self.checkalt:
            self.checkalt = False
            self.alt.setStyleSheet("QPushButton {\n"
                                   "color: #000000;\n"
                                   "}")
        else:
            self.checkalt = True
            self.alt.setStyleSheet("QPushButton {\n"
                                   "color: #FF0000;\n"
                                   "}")

    def ninef(self):
        self.str += '9'
        self.strall += '9'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def eightf(self):
        self.str += '8'
        self.strall += '8'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def sevenf(self):
        self.str += '7'
        self.strall += '7'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def sixf(self):
        if self.checkalt == False:
            self.str += '6'
            self.strall += '6'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)
        else:
            self.str += 'F'
            self.strall += 'F'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)

    def fivef(self):
        if self.checkalt == False:
            self.str += '5'
            self.strall += '5'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)
        else:
            self.str += 'E'
            self.strall += 'E'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)

    def fourf(self):
        if self.checkalt == False:
            self.str += '4'
            self.strall += '4'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)
        else:
            self.str += 'D'
            self.strall += 'D'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)

    def threef(self):
        if self.checkalt == False:
            self.str += '3'
            self.strall += '3'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)
        else:
            self.str += 'C'
            self.strall += 'C'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)

    def twof(self):
        if self.checkalt == False:
            self.str += '2'
            self.strall += '2'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)
        else:
            self.str += 'B'
            self.strall += 'B'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)

    def onef(self):
        if self.checkalt == False:
            self.str += '1'
            self.strall += '1'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)
        else:
            self.str += 'A'
            self.strall += 'A'
            self.primer.setText(self.strall)
            self.LCD.display(self.str)

    def zerof(self):
        self.str += '0'
        self.strall += '0'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def Cf(self):
        self.str, self.znak, self.strall, self.numbers = '', [], '', []
        self.LCD.display(0)
        self.primer.setText('')

    def zapf(self):
        self.str += '.'
        self.strall += '.'
        self.LCD.display(self.str)
        self.primer.setText(self.strall)

    def procentf(self):
        self.strall += '%'
        self.primer.setText(self.strall)
        try:
            self.LCD.display(float(self.str) / 100)
            self.str, self.znak, self.strall, self.numbers = '', [], '', []
        except ValueError:
            self.LCD.display('Error')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
