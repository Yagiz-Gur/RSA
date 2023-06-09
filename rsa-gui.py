from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt.setGeometry(QtCore.QRect(60, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.encrypt.setFont(font)
        self.encrypt.setObjectName("encrypt")
        self.encrypt.clicked.connect(self.enc)

        self.input = QtWidgets.QTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(280, 40, 501, 191))
        self.input.setObjectName("input")

        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(280, 280, 501, 261))
        self.output.setObjectName("output")

        self.decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt.setGeometry(QtCore.QRect(60, 390, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decrypt.setFont(font)
        self.decrypt.setObjectName("decrypt")
        self.decrypt.clicked.connect(self.dec)

        self.public_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.public_2.setGeometry(QtCore.QRect(110, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.public_2.setFont(font)
        self.public_2.setObjectName("public_2")

        self.private_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.private_2.setGeometry(QtCore.QRect(110, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.private_2.setFont(font)
        self.private_2.setObjectName("private_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 76, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(280, 250, 501, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(280, 10, 501, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 280, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(190, 40, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuRSA = QtWidgets.QMenu(self.menubar)
        self.menuRSA.setObjectName("menuRSA")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuRSA.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Rsa", "Rsa"))
        self.encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.decrypt.setText(_translate("MainWindow", "Decrypt"))
        # self.public_2.setText(_translate("MainWindow", "key"))
        # self.private_2.setText(_translate("MainWindow", "key"))
        self.label.setText(_translate("MainWindow", "Public Key:"))
        self.label_2.setText(_translate("MainWindow", "Private Key:"))
        self.label_3.setText(_translate("MainWindow", "Output:"))
        self.label_1.setText(_translate("MainWindow", "Input:"))
        self.menuRSA.setTitle(_translate("MainWindow", "RSA"))
    
    
    def enc(self): #encrpyt the text and print to output section
        key=self.public_2.text()
        liste = key.split(",")
        e=int(liste[0])
        n=int(liste[1])
    
        output=[]
        text1=self.to_ascii()
        for i in text1:
            i=int(i)
            output.append((i**e)%n)
        output ="+".join([str(item) for item in output])
        self.output.setText(output) 

    def to_ascii(self):   #convert strings to ascii code
        ascii_values = []
        for i in self.input.toPlainText():
            ascii_values.append(ord(i))

        return ascii_values

    def from_ascii(self,text):# convert ascii code to string
        text_values = []
        for i in text():
            text_values.append(chr(i))
        return text_values

    def dec(self): #encrpyt the text and print to output section
        key=self.private_2.text()
        liste = key.split(",")
        d=int(liste[0])
        n=int(liste[1])

        output=[]
        a=self.input.toPlainText()
        li=list(a.split("+"))
        for i in li:
           i=int(i)
           output.append((i**d)%n)
        
        decrypted = []
        for i in output:
            decrypted.append(chr(i))
        
        output ="".join([str(item) for item in decrypted])
        self.output.setPlainText(output) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
