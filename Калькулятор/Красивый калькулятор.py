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
        self.ans.clicked.connect(self.ansf)

        self.zap.setStyleSheet("QPushButton {color: #0000FF;}")
        self.zero.setStyleSheet("QPushButton {color: #0000FF;}")
        self.one.setStyleSheet("QPushButton {color: #0000FF;}")
        self.two.setStyleSheet("QPushButton {color: #0000FF;}")
        self.three.setStyleSheet("QPushButton {color: #0000FF;}")
        self.four.setStyleSheet("QPushButton {color: #0000FF;}")
        self.five.setStyleSheet("QPushButton {color: #0000FF;}")
        self.six.setStyleSheet("QPushButton {color: #0000FF;}")
        self.seven.setStyleSheet("QPushButton {color: #0000FF;}")
        self.eight.setStyleSheet("QPushButton {color: #0000FF;}")
        self.nine.setStyleSheet("QPushButton {color: #0000FF;}")
        self.d.setStyleSheet("QPushButton {color: #FFA500;}")
        self.s.setStyleSheet("QPushButton {color: #FFA500;}")
        self.p.setStyleSheet("QPushButton {color: #FFA500;}")
        self.ra.setStyleSheet("QPushButton {color: #FFA500;}")
        self.r.setStyleSheet("QPushButton {color: #FF0000;}")
        self.procent.setStyleSheet("QPushButton {color: #FFA500;}")
        self.tentotwo.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.tentoeight.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.tentosixteen.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.sixteentoten.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.eighttoten.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.twototen.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.drob.setStyleSheet("QPushButton {color: #00AA00;}")
        self.sqr.setStyleSheet("QPushButton {color: #00AA00;}")
        self.sqrt.setStyleSheet("QPushButton {color: #00AA00;}")
        self.fact.setStyleSheet("QPushButton {color: #00AA00;}")

    def df(self):
        try:
            if self.str:
                self.numbers.append(float(self.str))
                self.str = ''
            if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['/'])
                del self.znak[len(self.znak) - 1]
                self.znak.append('/')
            else:
                self.znak.append('/')
                self.strall += '/'
            self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def raf(self):
        try:
            if self.str or self.strall:
                if self.str:
                    self.numbers.append(float(self.str))
                    self.str = ''
                if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                    self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['-'])
                    del self.znak[len(self.znak) - 1]
                    self.znak.append('-')
                else:
                    self.znak.append('-')
                    self.strall += '-'
                self.primer.setText(self.strall)
            else:
                self.znak.append('-')
                self.strall += '-'
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def sf(self):
        try:
            if self.str:
                self.numbers.append(float(self.str))
                self.str = ''
            if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['+'])
                del self.znak[len(self.znak) - 1]
                self.znak.append('+')
            else:
                self.znak.append('+')
                self.strall += '+'
            self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def pf(self):
        try:
            if self.str:
                self.numbers.append(float(self.str))
                self.str = ''
            if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['*'])
                del self.znak[len(self.znak) - 1]
                self.znak.append('*')
            else:
                self.znak.append('*')
                self.strall += '*'
            self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def procentf(self):
        try:
            if self.str:
                self.numbers.append(float(self.str))
                self.str = ''
            if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['%'])
                del self.znak[len(self.znak) - 1]
                self.znak.append('%')
            else:
                self.znak.append('%')
                self.strall += '%'
            self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def altf(self):
        if self.checkalt:
            self.checkalt = False
            self.alt.setStyleSheet("QPushButton {color: #000000;}")
        else:
            self.checkalt = True
            self.alt.setStyleSheet("QPushButton {color: #FF0000;}")

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

    def deletef(self):
        try:
            self.str = self.str[:len(self.str) - 1]
            if len(self.numbers) == len(self.znak):
                self.strall = self.strall[:len(self.strall) - 1]
            if self.str:
                self.LCD.display(self.str)
                self.primer.setText(self.strall)
            else:
                self.LCD.display(0)
                self.primer.setText('')
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def factf(self):
        try:
            num1 = int(self.strall)
            self.str = ''
            if num1 < 1 or num1 > 12:
                raise Exception
            else:
                factorial = 1
                for i in range(2, num1 + 1):
                    factorial *= i
                self.LCD.display(factorial)
                self.primer.setText(self.strall + '!')
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def drobf(self):
        try:
            self.LCD.display(1 / float(self.strall))
            self.primer.setText('1/' + self.strall)
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def sqrtf(self):
        try:
            if float(self.strall) < 0:
                raise Exception
            self.LCD.display(float(self.str) ** 0.5)
            self.primer.setText('√' + self.str)
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def sqrf(self):
        try:
            self.LCD.display(float(self.strall) ** 2)
            self.primer.setText(self.strall + '²')
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def rf(self):
        try:
            if self.str:
                self.numbers.append(float(self.str))
                self.str = ''
            if self.strall[0] == '-':
                del self.znak[0]
                self.numbers[0] = -1 * self.numbers[0]
            while self.znak:
                if '%' in self.znak:
                    for i in range(len(self.znak)):
                        if self.znak[i] == '%':
                            self.numbers[i] = self.numbers[i] / 100
                            del self.znak[i]
                            break
                elif '*' in self.znak or '/' in self.znak:
                    for i in range(len(self.znak)):
                        if self.znak[i] == '*':
                            self.numbers[i] = self.numbers[i] * self.numbers[i + 1]
                            del self.znak[i]
                            del self.numbers[i + 1]
                            break
                        elif self.znak[i] == '/':
                            self.numbers[i] = self.numbers[i] / self.numbers[i + 1]
                            del self.znak[i]
                            del self.numbers[i + 1]
                            break
                elif '+' in self.znak or '-' in self.znak:
                    for i in range(len(self.znak)):
                        if self.znak[i] == '-':
                            self.numbers[i] = self.numbers[i] - self.numbers[i + 1]
                            del self.znak[i]
                            del self.numbers[i + 1]
                            break
                        elif self.znak[i] == '+':
                            self.numbers[i] = self.numbers[i] + self.numbers[i + 1]
                            del self.znak[i]
                            del self.numbers[i + 1]
                            break
            self.primer.setText(self.strall)
            self.LCD.display(self.numbers[0])
            self.maybenum = self.numbers[0]
            self.str, self.znak, self.strall, self.numbers = '', [], '', []
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def ansf(self):
        try:
            self.numbers.append(self.maybenum)

            self.strall += str(self.maybenum)
            self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def tentotwof(self):
        try:
            num = int(self.str)
            n = ''
            while num > 0:
                y = str(num % 2)
                n = y + n
                num = int(num / 2)
            if n:
                if self.znak:
                    k = -1 * int(n)
                else:
                    k = int(n)
                self.LCD.display(k)
                self.maybenum = k
            else:
                self.LCD.display(0)
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def tentoeightf(self):
        try:
            num = int(self.str)
            n = ''
            while num > 0:
                y = str(num % 8)
                n = y + n
                num = int(num / 8)
            if n:
                if self.znak:
                    k = -1 * int(n)
                else:
                    k = int(n)
                self.LCD.display(k)
                self.maybenum = k
            else:
                self.LCD.display(0)
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def tentosixteenf(self):
        try:
            num = int(self.str)
            n = ''
            l = ['A', 'B', 'C', 'D', 'E', 'F']
            while num > 0:
                y = int(num % 16)
                if y < 10:
                    n = str(y) + n
                else:
                    n = l[y - 10] + n
                num = int(num / 16)
            if n:
                if self.znak:
                    k = -1 * int(n)
                else:
                    k = int(n)
                self.LCD.display(k)
                self.maybenum = k
            else:
                self.LCD.display(0)
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def twototenf(self):
        try:
            if self.znak:
                k = -1 * int(self.str, base=2)
            else:
                k = int(self.str, base=2)
            self.LCD.display(k)
            self.maybenum = k
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def eighttotenf(self):
        try:
            if self.znak:
                k = -1 * int(self.str, base=8)
            else:
                k = int(self.str, base=8)
            self.LCD.display(k)
            self.maybenum = k
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def sixteentotenf(self):
        try:
            if self.znak:
                k = -1 * int(self.str, base=16)
            else:
                k = int(self.str, base=16)
            self.LCD.display(k)
            self.maybenum = k
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
