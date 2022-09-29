import traceback
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton, QVBoxLayout  , QTextEdit 
from PyQt5.QtCore import *
import sys
from webServer import  app 
from logger import customLogger
import uvicorn


class newFastAPI(QThread):
    def run(self):
        uvicorn.run(app,host='localhost',port=8080)
        

class CustomSignal(QObject):
    signal = pyqtSignal(str) #반드시 클래스 변수로 선언할 것

    def run(self,text):
        # text = "emit으로 전달"
        self.signal.emit(text) #customFunc 메서드 실행시 signal의 emit 메서드사용

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(' pyQt5 & fastAPI log Test')
        self.move(300, 300)
        self.resize(400, 200)
        # self.setWindowFlags(Qt.CoverWindow)
        
        self.tb = QTextEdit()
        self.tb.setReadOnly(True)
        self.tb.append('시작')
        
        self.customsignal = CustomSignal() #Mysignal 클래스의 객체 선언
        self.customsignal.signal.connect(self.append_text) #객체에 대한시그널 및 슬롯 설정


        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.tb, 0)
        vbox.addWidget(self.clear_btn, 1)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 1000, 300)
        
    @pyqtSlot(str)    
    def append_text(self,text):
        self.tb.append(text)

    def clear_text(self):
        self.tb.clear()
    


if __name__ == '__main__':
    try:
        Q = QApplication(sys.argv)
        brower = MyApp()
        brower.show()
        log = customLogger.getInstance()
        log.setMyApp(brower)

        api = newFastAPI()
        api.start()
        sys.exit(Q.exec_())

    except:
        log.showLog('=============================  에러 발생','error')
        log.showLog(traceback.format_exc(),'error')
 
