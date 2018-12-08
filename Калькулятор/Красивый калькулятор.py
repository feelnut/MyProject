import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QLCDNumber


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Kalkulator.ui', self)
        self.setWindowTitle('Ничо такой считовод')

        self.LCD.setDigitCount(15)
        self.str, self.znak, self.strall, self.numbers = '', [], '', []

        self.open.clicked.connect(self.openf)
        self.close.clicked.connect(self.closef)
        self.d.clicked.connect(self.df)
        self.s.clicked.connect(self.sf)
        self.p.clicked.connect(self.pf)
        self.ra.clicked.connect(self.raf)
        self.zap.clicked.connect(self.zapf)
        self.zero.clicked.connect(self.zerof)
        self.r.clicked.connect(self.rf)
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

    def procentf(self):
        self.znak = '%'
        self.strall += '%'
        self.primer.setText(self.strall)
        try:
            self.num1 = float(self.str) / 100
            self.LCD.display(self.num1)
        except ValueError:
            self.LCD.display('Error')

    def df(self):
        try:
            self.numbers.append(float(self.str))
        except ValueError:
            self.LCD.display('Error')
        self.str = ''
        self.znak = '/'
        if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
            self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + self.znak)
        else:
            self.strall += '/'
        self.primer.setText(self.strall)

    def raf(self):
        try:
            self.numbers.append(float(self.str))
        except ValueError:
            self.LCD.display('Error')
        self.str = ''
        self.znak = '-'
        if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
            self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + self.znak)
        else:
            self.strall += '-'
        self.primer.setText(self.strall)

    def sf(self):
        try:
            self.numbers.append(float(self.str))
        except ValueError:
            self.LCD.display('Error')
        self.str = ''
        self.znak = '+'
        if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
            self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + self.znak)
        else:
            self.strall += '+'
        self.primer.setText(self.strall)

    def pf(self):
        try:
            self.numbers.append(float(self.str))
        except ValueError:
            self.LCD.display('Error')
        self.str = ''
        self.znak = '*'
        if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
            self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + self.znak)
        else:
            self.strall += '*'
        self.primer.setText(self.strall)

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
        self.str += '6'
        self.strall += '6'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def fivef(self):
        self.str += '5'
        self.strall += '5'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def fourf(self):
        self.str += '4'
        self.strall += '4'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def threef(self):
        self.str += '3'
        self.strall += '3'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def twof(self):
        self.str += '2'
        self.strall += '2'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def onef(self):
        self.str += '1'
        self.strall += '1'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def zerof(self):
        self.str += '0'
        self.strall += '0'
        self.primer.setText(self.strall)
        self.LCD.display(self.str)

    def Cf(self):
        self.num1 = 0
        self.num2 = 0
        self.str = ''
        self.LCD.display(0)

    def drobf(self):
        try:
            self.num1 = float(self.str)
            self.LCD.display(1 / self.num1)
        except ValueError:
            self.LCD.display('Error')

    def sqrtf(self):
        try:
            self.num1 = int(self.str)
            if self.num1 < 0:
                raise ValueError
            self.LCD.display(self.num1 ** 0.5)
        except ValueError:
            self.LCD.display('Error')

    def sqrf(self):
        try:
            self.num1 = int(self.str)
            self.LCD.display(self.num1 ** 2)
        except ValueError:
            self.LCD.display('Error')

    def deletef(self):
        self.str = self.str[:len(self.str) - 1]
        if self.str:
            self.LCD.display(self.str)
        else:
            self.LCD.display(0)

    def zapf(self):
        self.str += '.'
        self.LCD.display(self.str)

    def openf(self):
        self.str += '('
        self.LCD.display(self.str)

    def closef(self):
        self.str += ')'
        self.LCD.display(self.str)

    def factf(self):
        try:
            self.num1 = int(self.str)
            if self.num1 < 1 or self.num1 > 12:
                raise ValueError
            else:
                factorial = 1
                for i in range(2, self.num1 + 1):
                    factorial *= i
                self.LCD.display(factorial)
        except ValueError:
            self.LCD.display('Error')

    def rf(self):
        count = 0
        for i in range(len(self.str)):
            if self.str[i] in ['*', '/', '+']:
                count += 1
        if count > 1:
            self.LCD.display('Error')
        else:
            if count == 0 and '-' not in self.str:
                self.LCD.display(self.str)
            else:
                if '*' in self.str:
                    try:
                        num1, num2 = [x for x in self.str.split('*')]
                        num1 = float(num1)
                        if num2[0] == '(' and num2[len(num2) - 1] == ')':
                            num2 = float(num2[1:len(num2) - 1])
                        else:
                            num2 = float(num2)
                        self.str = ''
                        self.LCD.display(num1 * num2)
                    except ValueError:
                        self.LCD.display('Error')
                elif '/' in self.str:
                    try:
                        num1, num2 = [x for x in self.str.split('/')]
                        num1 = float(num1)
                        if num2[0] == '(' and num2[len(num2) - 1] == ')':
                            num2 = float(num2[1:len(num2) - 1])
                        else:
                            num2 = float(num2)
                        self.str = ''
                        if num2 == 0:
                            self.LCD.display('Error')
                        else:
                            self.LCD.display(num1 / num2)
                    except ValueError:
                        self.LCD.display('Error')
                elif '+' in self.str:
                    try:
                        num1, num2 = [x for x in self.str.split('+')]
                        num1 = float(num1)
                        if num2[0] == '(' and num2[len(num2) - 1] == ')':
                            num2 = float(num2[1:len(num2) - 1])
                        else:
                            num2 = float(num2)
                        self.str = ''
                        self.LCD.display(num1 + num2)
                    except ValueError:
                        self.LCD.display('Error')
                else:
                    if self.str[0] == '-' and self.str.count('-') == 1:
                        self.LCD.display(self.str)
                    elif self.str[0] != '-' and self.str.count('(') == 0:
                        try:
                            num1, num2 = [float(x) for x in self.str.split('-')]
                            self.str = ''
                            self.LCD.display(num1 - num2)
                        except ValueError:
                            self.LCD.display('Error')
                    elif self.str[0] == '-' and self.str.count('-') == 2:
                        try:
                            trash, num1, num2 = [x for x in self.str.split('-')]
                            num1, num2 = float(num1), float(num2)
                            num1 = num1 * (-1)
                            self.str = ''
                            self.LCD.display(num1 - num2)
                        except ValueError:
                            self.LCD.display('Error')
                    elif self.str[0] != '-' and self.str.count('-') == 2:
                        try:
                            num1, num2 = [x for x in self.str.split('-(-')]
                            num1 = float(num1)
                            num2 = float(num2[:len(num2) - 1])
                            self.str = ''
                            self.LCD.display(num1 + num2)
                        except ValueError:
                            self.LCD.display('Error')
                    elif self.str[0] == '-' and self.str.count('-') == 3:
                        try:
                            num1, num2 = [x for x in self.str.split('-(-')]
                            num1 = float(num1)
                            num2 = float(num2[:len(num2) - 1])
                            self.str = ''
                            self.LCD.display(num1 + num2)
                        except ValueError:
                            self.LCD.display('Error')
                    else:
                        self.LCD.display('Error')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
