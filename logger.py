from datetime import datetime
from logging import handlers
import logging
import os



class customLogger:
    _instance = None
    def __init__(self):
        if not customLogger._instance:
            print('__init__ method called but nothing is created')
            self.setting()
        else:
            print('instance already created:', self.getInstance())
 
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = customLogger()
        return cls._instance

    def setting(self):
        self.myApp = None
        self.createFolder('./logs/')
        # looger 생성
        self.logger = logging.getLogger()
        #  로그 파일 날짜
        date = datetime.today().strftime("%Y%m%d")
        # 저장되는 파일 주기
        file_handler = handlers.TimedRotatingFileHandler(filename=f'./logs/{date}.log',  when='D',  encoding='utf-8'  )
        # 저장되는 파일 형식
        formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s') 
        # 파일 형식 설정
        file_handler.setFormatter(formatter)
        # logger와 연결 
        self.logger.addHandler(file_handler)
    
    def createFolder(self,directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)
            
    def showLog(self,message):
        self.logger.info(f'{message}')
        if self.myApp != None:
            self.myApp.customsignal.run(message)
        
    def setMyApp(self,myApp):
        self.myApp = myApp
        
