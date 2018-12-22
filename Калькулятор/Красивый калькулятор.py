import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import math


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Kalkulator.ui', self)
        self.setWindowTitle('Калькулятор')
        self.LCD.setDigitCount(18)
        self.checkalt = False
        self.tenss.setEnabled(False)

        self.str, self.znak, self.strall, self.numbers, self.sys = '', [], '', [], 10

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
        self.tenss.clicked.connect(self.tensf)
        self.twoss.clicked.connect(self.twosf)
        self.eightss.clicked.connect(self.eightsf)
        self.sixteenss.clicked.connect(self.sixteensf)
        self.alt.clicked.connect(self.altf)

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
        self.tenss.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.eightss.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.sixteenss.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.twoss.setStyleSheet("QPushButton {color: #FF55FF;}")
        self.drob.setStyleSheet("QPushButton {color: #00AA00;}")
        self.sqr.setStyleSheet("QPushButton {color: #00AA00;}")
        self.sqrt.setStyleSheet("QPushButton {color: #00AA00;}")
        self.fact.setStyleSheet("QPushButton {color: #00AA00;}")

    def df(self):
        try:
            if self.strall and self.strall != '-':
                if self.str:
                    self.numbers.append(float(self.str))
                    self.str = ''
                if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*']:
                    self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['/'])
                    del self.znak[len(self.znak) - 1]
                else:
                    self.strall += '/'
                self.znak.append('/')
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
                if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*']:
                    self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['-'])
                    del self.znak[len(self.znak) - 1]
                else:
                    self.strall += '-'
                self.znak.append('-')
                self.primer.setText(self.strall)
            else:
                self.znak.append('-')
                self.strall += '-'
                self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def sf(self):
        try:
            if self.strall and self.strall != '-':
                if self.str:
                    self.numbers.append(float(self.str))
                    self.str = ''
                if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*']:
                    self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['+'])
                    del self.znak[len(self.znak) - 1]
                else:
                    self.strall += '+'
                self.znak.append('+')
                self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def pf(self):
        try:
            if self.strall and self.strall != '-':
                if self.str:
                    self.numbers.append(float(self.str))
                    self.str = ''
                if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*']:
                    self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['*'])
                    del self.znak[len(self.znak) - 1]
                else:
                    self.strall += '*'
                self.znak.append('*')
                self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def procentf(self):
        try:
            if self.strall and self.strall != '-':
                if self.str:
                    self.numbers.append(float(self.str))
                    self.str = ''
                if self.strall[len(self.strall) - 1] in ['/', '-', '+', '*', '%']:
                    self.strall = ''.join(list(self.strall)[:len(self.strall) - 1] + ['%'])
                    del self.znak[len(self.znak) - 1]
                else:
                    self.strall += '%'
                self.znak.append('%')
                self.primer.setText(self.strall)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def altf(self):
        if self.sys == 16:
            if self.checkalt:
                self.checkalt = False
                self.alt.setStyleSheet("QPushButton {color: #000000;}")
                self.one.setText('1')
                self.two.setText('2')
                self.three.setText('3')
                self.four.setText('4')
                self.five.setText('5')
                self.six.setText('6')
            else:
                self.checkalt = True
                self.alt.setStyleSheet("QPushButton {color: #FF0000;}")
                self.one.setText('A')
                self.two.setText('B')
                self.three.setText('C')
                self.four.setText('D')
                self.five.setText('E')
                self.six.setText('F')

    def ninef(self):
        self.str += '9'
        self.strall += '9'
        self.fornumbers()

    def eightf(self):
        self.str += '8'
        self.strall += '8'
        self.fornumbers()

    def sevenf(self):
        self.str += '7'
        self.strall += '7'
        self.fornumbers()

    def sixf(self):
        self.str += 'F' if self.checkalt else '6'
        self.strall += 'F' if self.checkalt else '6'
        self.fornumbers()

    def fivef(self):
        self.str += 'E' if self.checkalt else '5'
        self.strall += 'E' if self.checkalt else '5'
        self.fornumbers()

    def fourf(self):
        self.str += 'D' if self.checkalt else '4'
        self.strall += 'D' if self.checkalt else '4'
        self.fornumbers()

    def threef(self):
        self.str += 'C' if self.checkalt else '3'
        self.strall += 'C' if self.checkalt else '3'
        self.fornumbers()

    def twof(self):
        self.str += 'B' if self.checkalt else '2'
        self.strall += 'B' if self.checkalt else '2'
        self.fornumbers()

    def onef(self):
        self.str += 'A' if self.checkalt else '1'
        self.strall += 'A' if self.checkalt else '1'
        self.fornumbers()

    def zerof(self):
        self.str += '0'
        self.strall += '0'
        self.fornumbers()

    def Cf(self):
        self.str, self.znak, self.strall, self.numbers = '', [], '', []
        self.LCD.display(0)
        self.primer.setText('')

    def zapf(self):
        self.str += '.' if self.strall else '0.'
        self.strall += '.' if self.strall else '0.'
        self.fornumbers()

    def fornumbers(self):
        self.LCD.display(self.str)
        self.primer.setText(self.strall)

    def deletef(self):
        try:
            if self.strall == '-':
                self.strall, self.znak = '', []
                self.primer.setText(self.strall)
            elif self.str:
                self.str = self.str[:len(self.str) - 1]
                self.LCD.display(self.str)
                self.strall = self.strall[:len(self.strall) - 1]
                self.primer.setText(self.strall)
            elif self.numbers:
                self.strall = self.strall[:len(self.strall) - 1] \
                    if self.strall[:len(self.strall) - 1] != '.' \
                    else self.strall[:len(self.strall) - 2]
                self.numbers[0] = int(self.strall) \
                    if self.strall.count('.') == 0 \
                    else float(self.strall)
                self.str = str(self.numbers[0])
                self.primer.setText(self.strall)
                self.LCD.display(self.str)
                if self.strall == str(self.numbers[0]):
                    del self.numbers[0]
            else:
                self.LCD.display(0)
                self.primer.setText('')
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def drobf(self):
        try:
            self.trans()
            k = int(1 / float(self.numbers[0])) \
                if str(1 / float(self.numbers[0]))[-1:-3:-1] == '0.' \
                else 1 / float(self.numbers[0])
            self.disp(k)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def factf(self):
        try:
            self.trans()
            k = int(self.numbers[0])
            k = math.factorial(k)
            self.disp(k)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def sqrtf(self):
        try:
            self.trans()
            k = int(float(self.numbers[0]) ** 0.5) \
                if str(float(self.numbers[0]) ** 0.5)[-1:-3:-1] == '0.' \
                else float(self.numbers[0]) ** 0.5
            self.disp(k)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def sqrf(self):
        try:
            self.trans()
            k = int(float(self.numbers[0]) ** 2) \
                if str(float(self.numbers[0]) ** 2)[-1:-3:-1] == '0.' \
                else float(self.numbers[0]) ** 2
            self.disp(k)
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def disp(self, k):
        self.LCD.display(k)
        self.strall = str(k)[:len(str(k)) - 2] if str(k)[-1:-3:-1] == '0.' else str(k)
        self.primer.setText(self.strall)
        self.str = ''
        self.numbers[0] = k

    def trans(self):
        if self.strall and not self.numbers:
            if self.sys != 16:
                self.numbers.append(float(self.strall))
            else:
                self.numbers.append(self.strall)

    def countf(self):
        if self.strall:
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
            self.numbers[0] = int(self.numbers[0]) \
                if str(self.numbers[0])[-1:-3:-1] == '0.' \
                else float(self.numbers[0])
            self.str, self.znak, self.strall = '', [], str(self.numbers[0])
            self.primer.setText(self.strall)
            self.LCD.display(self.numbers[0])

    def rf(self):
        try:
            if self.sys == 10:
                self.countf()
            else:
                if self.sys == 2:
                    self.numbers.append(int(self.str))
                    for i in range(len(self.numbers)):
                        self.numbers[i] = int(str(int(self.numbers[i])), base=2)
                    if len(self.znak) == len(self.numbers):
                        del self.znak[0]
                        self.numbers[0] *= -1
                    self.sys = 10
                    self.countf()
                    self.sys = 2
                    self.numbers[0] = self.transtwo(self.numbers[0])
                    self.primer.setText(self.strall)
                    self.numbers = [self.numbers[0]]
                elif self.sys == 8:
                    self.numbers.append(int(self.str))
                    for i in range(len(self.numbers)):
                        self.numbers[i] = int(str(int(self.numbers[i])), base=8)
                    if len(self.znak) == len(self.numbers):
                        del self.znak[0]
                        self.numbers[0] *= -1
                    self.sys = 10
                    self.countf()
                    self.sys = 8
                    num = int(self.numbers[0])
                    n = ''
                    while num > 0:
                        y = str(num % 8)
                        n = y + n
                        num = int(num / 8)
                    k = -1 * int(n) if n and self.znak else int(n)
                    self.numbers[0] = k
                    self.LCD.display(k)
                    self.strall = str(k)
                    self.primer.setText(self.strall)
                    self.numbers = [self.numbers[0]]
                elif self.sys == 16:
                    self.numbers.append(self.str)
                    for i in range(len(self.numbers)):
                        self.numbers[i] = int(str(self.numbers[i]), base=16)
                    if len(self.znak) == len(self.numbers):
                        self.numbers[0] *= -1
                    self.sys = 10
                    self.countf()
                    self.sys = 16
                    self.numbers[0] = self.transsixteen(self.numbers[0])
                    self.primer.setText(self.strall)
                    self.numbers = [self.numbers[0]]
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def able(self, b):
        self.sqrt.setEnabled(b)
        self.sqr.setEnabled(b)
        self.fact.setEnabled(b)
        self.drob.setEnabled(b)
        self.procent.setEnabled(b)

    def alltrue(self):
        self.two.setEnabled(True)
        self.three.setEnabled(True)
        self.four.setEnabled(True)
        self.five.setEnabled(True)
        self.six.setEnabled(True)
        self.seven.setEnabled(True)
        self.eight.setEnabled(True)
        self.nine.setEnabled(True)

    def transtwo(self, num):
        n = ''
        while num > 0:
            y = str(num % 2)
            n = y + n
            num = int(num / 2)
        k = -1 * int(n) if n and self.znak else int(n)
        self.LCD.display(k)
        self.strall = str(k)
        return k

    def transeight(self, num):
        n = ''
        while num > 0:
            y = str(num % 8)
            n = y + n
            num = int(num / 8)
        k = -1 * int(n) if n and self.znak else int(n)
        self.LCD.display(k)
        self.strall = str(k)
        return k

    def transsixteen(self, num):
        n = ''
        l = ['A', 'B', 'C', 'D', 'E', 'F']
        while num > 0:
            y = int(num % 16)
            if y < 10:
                n = str(y) + n
            else:
                n = l[y - 10] + n
            num = int(num / 16)
        k = '-' + n if n and self.znak else n
        return k

    def twosf(self):
        try:
            self.trans()
            self.pastsys = self.sys
            self.sys = 2
            self.default()
            self.alltrue()
            self.able(False)
            self.twoss.setEnabled(False)
            self.tenss.setEnabled(True)
            self.eightss.setEnabled(True)
            self.sixteenss.setEnabled(True)
            self.two.setEnabled(False)
            self.three.setEnabled(False)
            self.four.setEnabled(False)
            self.five.setEnabled(False)
            self.six.setEnabled(False)
            self.seven.setEnabled(False)
            self.eight.setEnabled(False)
            self.nine.setEnabled(False)
            if self.numbers:
                if self.pastsys == 16:
                    self.numbers[0] = self.transtwo(int(self.numbers[0], base=self.pastsys))
                else:
                    self.numbers[0] = self.transtwo(int(str(int(self.numbers[0])), base=self.pastsys))
                self.LCD.display(self.numbers[0])
                self.strall = str(self.numbers[0])
            else:
                self.LCD.display(0)
            self.str = ''
        except Exception:
            self.LCD.display('Error')
            self.primer.setText('')

    def eightsf(self):
        try:
            self.trans()
            self.pastsys = self.sys
            self.sys = 8
            self.default()
            self.alltrue()
            self.able(False)
            self.eightss.setEnabled(False)
            self.tenss.setEnabled(True)
            self.twoss.setEnabled(True)
            self.sixteenss.setEnabled(True)
            self.eight.setEnabled(False)
            self.nine.setEnabled(False)
            if self.numbers:
                if self.pastsys == 16:
                    self.numbers[0] = self.transeight(int(self.numbers[0], base=self.pastsys))
                else:
                    self.numbers[0] = self.transeight(int(str(int(self.numbers[0])), base=self.pastsys))
                self.LCD.display(self.numbers[0])
                self.strall = str(self.numbers[0])
            else:
                self.LCD.display(0)
            self.str = ''
        except Exception as e:
            print(e)
            self.LCD.display('Error')
            self.primer.setText('')

    def tensf(self):
        try:
            self.trans()
            self.pastsys = self.sys
            self.sys = 10
            self.default()
            self.alltrue()
            self.able(True)
            self.eightss.setEnabled(True)
            self.tenss.setEnabled(False)
            self.twoss.setEnabled(True)
            self.sixteenss.setEnabled(True)
            if self.numbers:
                if self.pastsys == 16:
                    self.numbers[0] = int(self.numbers[0], base=self.pastsys)
                else:
                    self.numbers[0] = int(str(int(self.numbers[0])), base=self.pastsys)
                self.LCD.display(self.numbers[0])
                self.strall = str(self.numbers[0])
            else:
                self.LCD.display(0)
            self.str = ''
        except Exception as e:
            print(e)
            self.LCD.display('Error')
            self.primer.setText('')

    def sixteensf(self):
        try:
            self.trans()
            self.pastsys = self.sys
            self.sys = 16
            self.alltrue()
            self.able(False)
            self.eightss.setEnabled(True)
            self.tenss.setEnabled(True)
            self.twoss.setEnabled(True)
            self.sixteenss.setEnabled(False)
            if self.numbers:
                self.numbers[0] = self.transsixteen(int(str(int(self.numbers[0])), base=self.pastsys))
                self.LCD.display(self.numbers[0])
                self.strall = str(self.numbers[0])
            else:
                self.LCD.display(0)
            if self.numbers:
                self.str, self.strall = str(self.numbers[0]), str(self.numbers[0])
                del self.numbers[0]
        except Exception as e:
            print(e)
            self.LCD.display('Error')
            self.primer.setText('')

    def default(self):
        if self.checkalt and self.sys != 16:
            self.checkalt = False
            self.alt.setStyleSheet("QPushButton {color: #000000;}")
            self.one.setText('1')
            self.two.setText('2')
            self.three.setText('3')
            self.four.setText('4')
            self.five.setText('5')
            self.six.setText('6')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
