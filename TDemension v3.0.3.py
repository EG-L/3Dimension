import sys
import os
from multiprocessing import Queue,freeze_support,Process,Manager #MultiProcessing 설정
from PySide2.QtWidgets import QMainWindow, QApplication,QMessageBox,QDialog,QComboBox,QPushButton,QFileDialog #PySide2 ui 위젯 사용
from PySide2.QtCore import * #PySide2 ui 위젯 사용
from PySide2.QtGui import * #PySide2 ui 위젯 사용
from datetime import datetime #날짜 업데이트
import paho.mqtt.subscribe as subscribe #MQTT 통신
import paho.mqtt.publish as publish #MQTT 통신
import time #지연시간
import pyqtgraph as pg #그래프 표시
from TOMO_COSTAL_KW_v2 import Ui_MainWindow #메인 UI 표시
import numpy as np #그래프 업데이트 함수 처리
from time import ctime #데이터 저장 간 시간 업데이트
from haversine import haversine #두 GPS 거리 계산
import matplotlib.pyplot as plt #MQTT 통신 MAP 화면 표시
import mplleaflet #MQTT 통신 MAP 화면 표시
import matplotlib #MQTT 통신 MAP 화면 표시
from PySide2.QtWebEngineWidgets import QWebEngineView #MQTT 통신 MAP 화면 표시
import pandas as pd #데이터 저장
import re #데이터 저장 포맷 설정

def Multi_Calc(LOC,read_que,send_que,set_location,location,DSPEN,TRXPSEN,TRXCSEN,MNTIN,DC12VMNT,BOARD_TEMP,RTS_TEMP,RTS_DEPTH,DSP_TEMP):
    '''MultiProcesisng 처리부'''
    '''
    해당 동작의 경우 Queue 통해서 데이터가 삽입 됐을 시 동작을 진행하며,
    Error가 실행됐을 때 동작이 멈추는 것을 방지하기 위해 Try-Exception 함수로 예외 처리 진행
    '''
    while True:
        if read_que.empty() != True: #Queue 버퍼가 Null값이 아닐 때
            Dat = read_que.get() # Data를 읽어 온다.
            try:
                Data = list(map(float,Dat.decode().split(','))) # 데이터 형 변환
                set_location.value = int(Data.pop(0))-1 #송신 위치
                location.value = int(Data.pop(0))-1 #수신 위치

                if location.value+1 in LOC: #LOCATION 함수 내에 value 값이 존재하면
                    DSPEN[location.value] = Data.pop(0) #DSPEN 저장
                    TRXPSEN[location.value] = Data.pop(0) #TRXPSEN 저장
                    TRXCSEN[location.value] = Data.pop(0) #TRXCSEN 저장
                    DC12VMNT[location.value] = Data.pop(0) #DC12VMNT 저장
                    MNTIN[location.value] = Data.pop(0) #MNTIN 저장
                    BOARD_TEMP[location.value] = Data.pop(0) #BOARD_TEMP 저장
                    RTS_TEMP.value = Data.pop(0) #센서 온도 저장
                    RTS_DEPTH.value = Data.pop(0) #센서 깊이 저장
                    Data.pop(0) #FPGA 동작 상태 (사용 x)
                    DSP_TEMP[location.value] = Data.pop(0) # DSP_TEMP 저장

                    send_que.put('RECV_RTS_DATA')
                    time.sleep(0.1)
                    send_que.put('RECV_ETC')
                    time.sleep(0.1)
                    send_que.put(list(map(int,Data)))
                else:
                    send_que.put('Error_RECV')
            except Exception as e:
                print(e)
                send_que.put('Error_RECV')
        time.sleep(0.1)

def Multi_GPS(send_que,GPS_DATA): # GPS UPDATE
    '''
    데이터 프로토콜에 따른 Broker 및 Topic 설정
    '''
    broker = "test.mosquitto.org" #Broker 서버 설정
    topic = "Core/test12343Demension/version" #GPS 수신 토픽
    while True:
        try:
            m = subscribe.simple(topic,hostname=broker,keepalive=20) # GPS DATA 수신 대기
            dat = list(map(float,m.payload.decode().split(','))) # DATA LIST
            GPS_DATA[int(dat[0])-1] = dat[1:]
            if dat[1] == 0 and dat[2] == 0: # GPS DATA가 0 일 때 동작
                send_que.put('STATION %s GPS_ERROR'%int(dat[0])) #Error 수신 함수
            else:  # GPS DATA가 0이 아닐 때 동작
                send_que.put('RECV_GPS')
            time.sleep(0.1)
        except Exception as e:# 에러 표기 및 에러가 표시 됐을 때
            print(e)
            continue # Multiprocessing 동작 중 실행 중지가 안되게 동작 진행

class QDialog_Setting(QDialog): ## SETTING
    def __init__(self):
        from Setting_KW import Ui_Dialog

        super().__init__() # Super 함수를 사용하여 QDialog를 상속

        self.w =  Ui_Dialog() #Import한 Ui_Dialog를 선언

        self.w.setupUi(self)

        self.w.pushButton.clicked.connect(self.openWindowClass) # 버튼 연동

    def openWindowClass(self):
        if self.w.lineEdit.text().upper() == 'KW' and self.w.lineEdit_2.text() == '1234':  # 해당 아이디와 비밀번호가 맞을 시
            mainwindow.show() # 메인화면 이동
            global Order,Setting
            Order.put(int(self.w.comboBox.currentText())) # Station 개수 삽입
            Setting.close() # Setting 화면 끄기
        else: # 틀릴 시
            messagebox = QMessageBox() #경고문 표시
            messagebox.setText('아이디 또는 비밀번호를 잘못 입력하셨습니다.')# 경고문 내용 설정
            messagebox.setWindowTitle('Alert')# 경고문 타이틀 설정
            messagebox.setStyleSheet("background-color: rgba(16,30,41,240);color: rgb(255, 255, 255)") # 경고문 배경 화면 설정
            messagebox.exec_()# 경고문 종료

class VERSION_UPDATE(QThread):
    VERSION_DAT = Signal(str)
    def __init__(self,parent):
        super().__init__()
        self.parent = parent #부모함수에 업데이트 하기 위한 함수

    def run(self):
        global VERSION_Que,GPS
        if VERSION_Que.empty() != True: #Version_que가 Null값이 아니라면
            Dat = VERSION_Que.get()
            if Dat == 'RECV_GPS':
                for i in range(len(self.parent.w.GPS_LABEL)): #GPS 정보 업데이트
                    self.parent.w.GPS_LABEL[i].setText('[%.2f,%.2f]'%(GPS[i][0],GPS[i][1]))
            elif Dat == 'RECV_ETC': #이외의 데이터 업데이트
                for i in range(len(self.parent.w.ALL_RECV_DATA_LABEL)):
                    for j in range(len(self.parent.w.ALL_RECV_DATA_LABEL[i])):
                        self.parent.w.ALL_RECV_DATA_LABEL[i][j].setText(str(self.parent.w.ALL_RECV_DATA[i][j])) #Ui_Dialog 업데이트 진행

class QDialog_Version_Check(QDialog): ## VERSION INFO
    def __init__(self):
        from version_check_KW import Ui_Dialog

        super().__init__()

        self.w = Ui_Dialog()

        self.w.setupUi(self)

        global DSPEN,TRXPSEN,TRXCSEN,MNTIN,DC12VMNT,BOARD_TEMP,GPS,DSP_TEMP

        self.DSPEN_LABEL = [self.w.label_6,self.w.label_26,self.w.label_27,self.w.label_28,self.w.label_29] #INFO 내의 DSPEN 정보 업데이트
        self.TRXPSEN_LABEL = [self.w.label_8,self.w.label_30,self.w.label_31,self.w.label_32,self.w.label_33] #INFO 내의 TRXPSEN 정보 업데이트
        self.TRXCSEN_LABEL = [self.w.label_10,self.w.label_34,self.w.label_35,self.w.label_36,self.w.label_37] #INFO 내의 TRXCSEN 정보 업데이트
        self.MNTIN_LABEL = [self.w.label_21,self.w.label_22,self.w.label_23,self.w.label_24,self.w.label_25] #INFO 내의 MNTIN 정보 업데이트
        self.DC12VMNT_LABEL = [self.w.label_38,self.w.label_39,self.w.label_40,self.w.label_41,self.w.label_42] #INFO 내의 DC12VMNT 정보 업데이트
        self.BOARD_TEMP_LABEL = [self.w.label_45,self.w.label_44,self.w.label_48,self.w.label_47,self.w.label_46] #INFO 내의 BOARD_TEMP 정보 업데이트
        self.GPS_LABEL = [self.w.label_52,self.w.label_51,self.w.label_53,self.w.label_50,self.w.label_54] #INFO 내의 GPS 정보 업데이트
        self.DSP_TEMP_LABEL = [self.w.label_2,self.w.label_11,self.w.label_12,self.w.label_13,self.w.label_14] #INFO 내의 DSP_TEMP 정보 업데이트

        self.ALL_RECV_DATA_LABEL = [self.DSPEN_LABEL,self.TRXPSEN_LABEL,self.TRXCSEN_LABEL,self.MNTIN_LABEL,self.DC12VMNT_LABEL,self.BOARD_TEMP_LABEL,self.DSP_TEMP_LABEL] #INFO 내의 모든 정보 업데이트
        self.ALL_RECV_DATA = [DSPEN,TRXPSEN,TRXCSEN,MNTIN,DC12VMNT,BOARD_TEMP,DSP_TEMP] # 저장 데이터

        for i in range(len(self.ALL_RECV_DATA_LABEL)): # 모든 함수 초기 업데이트
            for j in range(len(self.ALL_RECV_DATA_LABEL[i])):
                self.ALL_RECV_DATA_LABEL[i][j].setText(self.ALL_RECV_DATA[i][j])

    def closeEvent(self, event):
        self.close() # 닫기 버튼 클릭 시 동작

class Worker(QThread): ## SETTING QUEUE BUFFER
    SendData = Signal(int)

    def __init__(self,parent):
        super().__init__()
        self.parent = parent

    def run(self):
        global Order
        while True:
            if Order.qsize !=0 :
                self.SendData.emit(Order.get())
                break

class DATA_LOG_AUTO_SAVE(QThread):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

    def run(self):

        global DATA_TEMP,DATA_DEPTH,DATA_TIME,ProcessingQue
        while True:
            time.sleep(60*60*3) # 특정시간 업데이트 대기(60초*60*3 = 3시간 대기)
            '''데이터 로그 저장'''

            try:
                with open('./KW_CSV_Data/%s/%s/%s/%s_DATA_LOG.txt'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1],list(filter(None,ctime().split(' ')))[2],re.sub(" |:","_",ctime())),'w') as file:
                    file.write(self.parent.textBrowser.toPlainText())#현재까지의 로그 파일을 저장
            except Exception as e:
                print(e)
                if not os.path.exists('./KW_CSV_Data'):# 파일이 없을 경우 파일 생성
                    os.makedirs('./KW_CSV_Data')

                if not os.path.exists('./KW_CSV_Data/%s'%list(filter(None,ctime().split(' ')))[-1]):
                    os.makedirs('./KW_CSV_Data/%s'%list(filter(None,ctime().split(' ')))[-1])

                if not os.path.exists('./KW_CSV_Data/%s/%s'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1])):
                    os.makedirs('./KW_CSV_Data/%s/%s'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1]))
                
                if not os.path.exists('./KW_CSV_Data/%s/%s/%s'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1],list(filter(None,ctime().split(' ')))[2])):
                    
                    os.makedirs('./KW_CSV_Data/%s/%s/%s'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1],list(filter(None,ctime().split(' ')))[2]))
                    
                    with open('./KW_CSV_Data/%s/%s/%s/%s_DATA_LOG.txt'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1],list(filter(None,ctime().split(' ')))[2],re.sub(" |:","_",ctime())),'w') as file:
                        file.write(self.parent.textBrowser.toPlainText())#현재까지 로그 파일을 저장
                pass
            
            time.sleep(0.1)
            
            ProcessingQue.put('CLEAR_TEXT') # 데이터 로그 창 초기화

            #AUTO SAVE DATA_LOG 창 표시 구현 예정
            time.sleep(0.1)

            ProcessingQue.put('DATA_AUTO_SAVE')

            '''파일 생성'''

class Q_TimeSet(QThread):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.topic = "Core/test12343Demension/data"
    
    def run(self):
        global ProcessingQue,Axis_data,Thread_Working,Interval,Index_Number,select_hour,select_min,LOCATION,broker,DATA_DEPTH,DATA_TEMP,DATA_TIME,ORDER_STRING,OrderNumber

        if select_min <= datetime.now().minute: # 선택 분이 더 작거나 같으면
            if select_hour == datetime.now().hour: # 선택 시간이랑 현재 시간이랑 동일할 때
                if datetime.now().minute+1 >=60: # 현재 시각이 59분일 때
                    select_hour = (select_hour+1)%24 # 시간을 1시간 더해준다.
                select_min = (datetime.now().minute+1)%60 # 분을 1분 더해준다.

        Dat = bytes(str(select_hour)+","+str(select_min)+","+str(Interval)+","+str(LOCATION[Index_Number]),'utf-8') # 송신 시간 DATA 설정
        
        publish.single(self.topic,b'STOP,'+Dat+b',START',hostname=broker,keepalive=0) # 데이터 송신


        while True: # 일정 시간을 대기 위한 함수
            if datetime.now().minute == select_min and datetime.now().hour == select_hour:
                break
            time.sleep(0.1)

        ProcessingQue.put('DATA_READ')

        select_hour = (select_hour+(select_min+Interval)//60)%24 # 해당 시가 24시를 넘지 않기 위해 나머지를 구해준다.
        select_min = (select_min+Interval)%60 # 해당 분이 60분을 넘지 않기 위해 나머지를 구해준다.
        
        if Index_Number == len(Axis_data)-1: # 순차적으로 인덱스를 동작하기 위한 함수
            Index_Number = -1
        Index_Number+=1


        ProcessingQue.put('TimeSet')

class Q_DATAREAD(QThread): # SUBSCRIBE DATA READ
    '''
    데이터 프로토콜에 따른 Broker 및 Topic 설정
    '''
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.topic = "Core/sendTestData1234/data"

    def run(self):
        global Axis_data,ProcessingQue,Index_Number,LOCATION,broker
        
        self.parent.textBrowser.append('\n%s : WORKING STATION %s\n'%(ctime(),LOCATION[Index_Number-1])) # SENSOR 동작 데이터 로그

        ProcessingQue.put('%s DATA_LED'%str(LOCATION[Index_Number-1]-1)) #SENSOR 동작 LED

        while True:
            m = subscribe.simple(self.topic,hostname=broker,keepalive=20) # 데이터 수신 대기

            MultiProc_Que.put(m.payload) # 데이터 수신 완료 시 데이터 Multiprocessing 함수로 보내 처리

class Process_Function(QThread): ## MAIN QUEUE BUFFER
    DT_SEND = Signal(str) #데이터 송신 관련 Signal/Slot 함수 처리
    CL_TEXT = Signal(str) #데이터 로그 초기화 Signal/Slot 함수 처리
    UPDATE_LED = Signal(str) # LED 관련 업데이트 Signal/Slot 함수 처리
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

    def run(self):
        #전역변수
        global ProcessingQue,Thread_Working,MultiProc_Que,VERSION_Que,RT_data,RECV_INDEX,RTS_DEPTH,RTS_TEMP,DATA_TEMP,DATA_DEPTH,DATA_TIME,RTS_READ_Que,DISTANCE,GPS,LOCATION,recv_Map_Que,RT_INDEX,SET_INDEX,ORDER_STRING,OrderNumber
        while True:
            if ProcessingQue.empty() != True :#ProcessingQue가 공백이 아니면
                Data = ProcessingQue.get()
                if Data == 'TimeSet':#동작 실행 명령어가 들어오면 동작
                    Thread_Working = True
                    self.parent._QTimeSet.terminate() # 동작 초기화
                    self.parent._QTimeSet.start() # 동작 실행
                elif Data == 'Stop':#동작 종료 명령어가 들어오면
                    Thread_Working = False
                    self.parent._QTimeSet.terminate() # 동작 초기화
                    self.parent._QDTREAD.terminate() # 동작 초기화
                    self.parent._AUTOSAVE.terminate() # 동작 초기화
                    if ProcessingQue.empty() != True:
                        while True: # Queue 경우 clear 함수가 없기 때문에 공간이 빌 때까지 비워주어 Queue에 아무것도 없게 만들어 Stop한다.
                            ProcessingQue.get()
                            if ProcessingQue.empty() == True:
                                break
                    if MultiProc_Que.empty() != True:
                        while True:
                            MultiProc_Que.get()
                            if MultiProc_Que.empty() == True:
                                break
                elif Data == 'DATA_READ':#데이터 송신 명령어를 읽었을 때
                    self.parent._QDTREAD.terminate() # 동작 초기화
                    self.parent._QDTREAD.start() # 동작 실행
                elif Data == 'RECV_GPS': # READ_GPS
                    VERSION_Que.put(Data)
                    self.parent.VERSION_UPDATE.start() #GPS 업데이트 함수 실행
                elif Data == 'RECV_RTS_DATA': # TEMP , DEPTH
                    if (int(self.parent.start_time[3].split(":")[0])+3)%24 == int(list(filter(None,ctime().split(' ')))[3].split(":")[0]): #현재 시간 +3 일 경우 동작 진행(ex: 3시간 후)
                        DATA_TEMP = [[0],[0],[0],[0],[0]]# 초기화
                        DATA_DEPTH = [[0],[0],[0],[0],[0]]# 초기화
                        DATA_TIME = [[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()]]# start_time 지정

                        self.parent.start_time = list(filter(None,ctime().split(' ')))

                    if DATA_TEMP[RECV_INDEX.value][-1] == 0 and DATA_DEPTH[RECV_INDEX.value][-1] == 0: # 깊이 및 온도 데이터가 초기값일 경우
                        DATA_TIME[RECV_INDEX.value][-1] = datetime.now() # 현재 시간
                        DATA_TEMP[RECV_INDEX.value][-1] = RTS_TEMP.value # 센서 온도
                        DATA_DEPTH[RECV_INDEX.value][-1] = RTS_DEPTH.value # 센서 깊이
                    else:# 초기값이 아닐 경우(처음을 제외한 경우 이 함수가 진행되게 된다.)
                        DATA_TIME[RECV_INDEX.value].append(datetime.now())
                        DATA_TEMP[RECV_INDEX.value].append(RTS_TEMP.value)
                        DATA_DEPTH[RECV_INDEX.value].append(RTS_DEPTH.value)

                    RTS_READ_Que.put('DATA_READ')
                    
                    if BOARD_TEMP[RECV_INDEX.value]>=60: # 60도 이상일 경우 이상 신호 발생 데이터 로그 및 LED 표기
                        self.parent.textBrowser.append('%s : STATION %s - %s ℃ BOARD_TEMP ERROR'%(ctime(),RECV_INDEX.value+1,str(BOARD_TEMP[RECV_INDEX.value])))
                        self.UPDATE_LED.emit('%s ERR_BOARD_TEMP'%RECV_INDEX.value)
                    else:
                        self.UPDATE_LED.emit('%s NOR_BOARD_TEMP'%RECV_INDEX.value)
                    if DSP_TEMP[RECV_INDEX.value]>=60: # 60도 이상일 경우 이상 신호 발생 데이터 로그 및 LED 표기
                        self.parent.textBrowser.append('%s : STATION %s - %s ℃ DSP_TEMP ERROR'%(ctime(),RECV_INDEX.value+1,str(DSP_TEMP[RECV_INDEX.value])))
                        self.UPDATE_LED.emit('%s ERR_DSP_TEMP'%RECV_INDEX.value)
                    else:
                        self.UPDATE_LED.emit('%s NOR_DSP_TEMP'%RECV_INDEX.value)

                elif Data == 'RECV_ETC': # ETC DATA
                    VERSION_Que.put(Data)
                    self.parent.VERSION_UPDATE.start()
                elif type(Data) == list: # READ_DATA
                    try:#데이터 저장 시 동작 진행
                        pd.DataFrame(Data).to_csv('./KW_CSV_Data/%s/%s/%s/%s_Station_%s_Station_%s.csv'%(ctime().split(' ')[-1],ctime().split(' ')[1],ctime().split(' ')[2],re.sub(" |:","_",ctime()),SET_INDEX.value+1,RECV_INDEX.value+1),header=False,index=False)
                    except:# 데이터 저장 중 경로가 없을 경우 예외 처리
                        print("Not DATA SAVE")

                        if not os.path.exists('./KW_CSV_Data'):# 파일이 없을 경우 파일 생성
                            os.makedirs('./KW_CSV_Data')

                        if not os.path.exists('./KW_CSV_Data/%s'%list(filter(None,ctime().split(' ')))[-1]):
                            os.makedirs('./KW_CSV_Data/%s'%list(filter(None,ctime().split(' ')))[-1])

                        if not os.path.exists('./KW_CSV_Data/%s/%s'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1])):
                            os.makedirs('./KW_CSV_Data/%s/%s'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1]))
                        
                        if not os.path.exists('./KW_CSV_Data/%s/%s/%s'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1],list(filter(None,ctime().split(' ')))[2])):
                            
                            os.makedirs('./KW_CSV_Data/%s/%s/%s'%(list(filter(None,ctime().split(' ')))[-1],list(filter(None,ctime().split(' ')))[1],list(filter(None,ctime().split(' ')))[2]))
                        pass
                    START_INDEX = Data.pop(0) # 데이터 인덱스 저장
                    RT_INDEX[RECV_INDEX.value] = [START_INDEX] # 시작 인덱스 위치
                    DEFAULT_LENGTH = np.array([0]*280000) # 28만개 데이터 설정
                    DEFAULT_LENGTH[START_INDEX:START_INDEX+len(Data)] = np.array(Data) # 중간 위치 데이터 삽입
                    RT_data[RECV_INDEX.value] = list(DEFAULT_LENGTH)
                    self.DT_SEND.emit('DATA_RECV') # 데이터 그리기
                    self.parent.textBrowser.append('%s : %s DATA_RECV_STATION %s'%(ctime(),ORDER_STRING[OrderNumber],str(RECV_INDEX.value+1))) # 데이터 로그 출력
                
                elif Data == 'Error_RECV': # 에러 데이터 수신 시
                    self.parent.textBrowser.append('%s : Error RECV'%ctime()) # 데이터 로그 에러 처리
                
                elif Data == 'DISTANCE': # 거리 데이터 수신 시
                    for i in range(len(LOCATION)-1):
                        for j in range(i+1,len(LOCATION)): # harversine 함수를 통한 GPS 간 거리 데이터 구하기
                            DISTANCE[LOCATION[i]-1][LOCATION[j]-1],DISTANCE[LOCATION[j]-1][LOCATION[i]-1] = haversine(GPS[LOCATION[i]-1][::-1],GPS[LOCATION[j]-1][::-1],unit='m'),haversine(GPS[LOCATION[i]-1][::-1],GPS[LOCATION[j]-1][::-1],unit='m')
                            self.parent.textBrowser.append('%s - %s : %s m SET'%(LOCATION[i],LOCATION[j],DISTANCE[LOCATION[i]-1][LOCATION[j]-1]))# 거리 데이터 로그 출력
                            break
                    
                    DISTANCE[LOCATION[-1]-1][LOCATION[0]-1],DISTANCE[LOCATION[0]-1][LOCATION[-1]-1] = haversine(GPS[LOCATION[-1]-1][::-1],GPS[LOCATION[0]-1][::-1],unit='m'),haversine(GPS[LOCATION[-1]-1][::-1],GPS[LOCATION[0]-1][::-1],unit='m')
                    self.parent.textBrowser.append('%s - %s : %s m SET\n'%(LOCATION[-1],LOCATION[0],DISTANCE[LOCATION[-1]-1][LOCATION[0]-1]))
                
                elif Data == 'RECV_MAP': # Map 관련 업데이트 함수
                    recv_Map_Que.put('UPDATE_MAP')

                elif Data == 'CLEAR_TEXT': # 데이터 로그 창 지우기
                    self.CL_TEXT.emit('CLEAR')

                elif 'GPS_ERROR' in Data: # GPS Error 데이터 로그 출력
                    self.parent.textBrowser.append(Data)
                    
                elif 'DATA_LED' in Data: # LED 관련 업데이트 함수
                    self.UPDATE_LED.emit(Data)

                elif 'DATA_AUTO_SAVE' in Data:
                    self.parent.textBrowser.append('DATA LOG AUTO SAVE\n%s'%os.getcwd()+'\KW_CSV_Data')

class TEDE_UPDATE(QThread):
    Update_SEND = Signal(str)# 온도 및 깊이 업데이트를 위한 Signal/Slot 함수
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
    
    def run(self):
        global RTS_READ_Que
        while True:
            if RTS_READ_Que.empty() != True: # RTS_READ_Que가 공백이 아니면
                RTS_READ_Que.get()
                self.Update_SEND.emit('U')#Signal/Slot 업데이트 함수
            time.sleep(0.1)

class QDialog_TEMP_DEPTH(QDialog):
    def __init__(self):
        from TOMO_COSTAL_TEMP_KW import Ui_Dialog #Ui_Dialog 화면 상속을 위한 함수
        super().__init__()#QDialog 상속

        self.TEDE = Ui_Dialog()
        self.TEDE.setupUi(self)

        self.TEDE_p1 = self.TEDE.widget.plotItem #Plot 위젯 설정

        self.TEDE_p2 = pg.ViewBox() #온도와 깊이를 동시에 표시하기 위한 viewbox 생성
        self.TEDE_p1.showAxis('right')
        self.TEDE_p1.scene().addItem(self.TEDE_p2) # Scene에 동시 표기
        self.TEDE_p1.getAxis('right').linkToView(self.TEDE_p2) #View 연동
        self.TEDE_p2.setXLink(self.TEDE_p1)
        self.TEDE_p1.getAxis('right').setPen(pg.mkPen(color=(0,255,0),width=1))

        self.TEDE_p1.setLabel('right', 'Depth', units='m', **{'color': 'rgb(0, 255, 0)', 'font-size': '10pt',
                                'font-family' : 'D2Coding'}) #깊이 Label 표기
        self.TEDE_p1.setLabel('left','Temperature',units='℃') #온도 Label 표기

        self.READ_DT = TEDE_UPDATE(self) # QThread 연동을 위한 함수
        self.READ_DT.start()#QThread 시작
        self.READ_DT.Update_SEND.connect(self.update_Data)

        self.TEDE.pushButton.clicked.connect(self.Choice_Sensor)#버튼 클릭시 이벤트 함수 동작

    def Choice_Sensor(self):#comboBox에 삽입된 데이터에 따른 
        global TEDE_INDEX
        TEDE_INDEX = int(self.TEDE.comboBox.currentText()[-1])-1
        self.update_Data(self)

    @Slot(str)
    def update_Data(self,temp):#데이터가 들어올 시 업데이트
        global DATA_DEPTH,DATA_TEMP,TEDE_INDEX
        
        self.TEDE.label.setText('%s℃'%str(DATA_TEMP[TEDE_INDEX][-1])) #온도 Label 업데이트
        self.TEDE.label_2.setText('%sm'%str(DATA_DEPTH[TEDE_INDEX][-1])) #깊이 Label 업데이트

        self.TEDE_p1.clear() #그래프를 그리기 전 초기화 함수
        self.TEDE_p2.clear() #그래프를 그리기 전 초기화 함수

        Temperature = self.TEDE_p1.plot(pen=pg.mkPen(color=(255, 255, 255)),name='Temperature') # 온도 데이터 그래프
        Depth = self.TEDE_p1.plot(pen=pg.mkPen(color=(0, 255, 0)),name='Depth') # 깊이 데이터 그래프
        curv2 = pg.PlotCurveItem(pen=pg.mkPen(color=(0, 255, 0)),name='Depth')

        self.TEDE_p2.addItem(curv2)

        Temperature.setData(x=[x.timestamp() for x in DATA_TIME[TEDE_INDEX]],y=DATA_TEMP[TEDE_INDEX]) #온도 시간에 따른 그래프 설정
        curv2.setData(x=[x.timestamp() for x in DATA_TIME[TEDE_INDEX]],y=DATA_DEPTH[TEDE_INDEX]) # 깊이 시간에 따른 그래프 설정

        if len(DATA_TIME[TEDE_INDEX])>=15:#데이터 시간의 인덱스 값이 15개가 넘어가면
            self.TEDE_p1.setXRange(DATA_TIME[TEDE_INDEX][-15].timestamp(),DATA_TIME[TEDE_INDEX][-1].timestamp(),padding=0) #뒤에서 15개만 화면상 표시

        self.TEDE_p1.addLegend()

        self.updateViews()
        self.TEDE.widget.plotItem.vb.sigResized.connect(self.updateViews) # 위젯 크기에 맞게 화면 조절

    def updateViews(self):
        self.TEDE_p2.setGeometry(self.TEDE_p1.getViewBox().sceneBoundingRect())

        self.TEDE_p2.linkedViewChanged(self.TEDE_p1.getViewBox(), self.TEDE_p2.XAxis)

    def closeEvent(self, event): # 위젯 종료 시 동작
        self.close()

class Setting_Location(QDialog): #LOCATION 화면 세팅 함수
    def __init__(self):
        from Setting_LOCATION import Ui_Dialog #Setting 화면 불러오기

        super().__init__() # 상속을 위한 함수

        self.ST = Ui_Dialog() #Ui_Dialog 선언
        self.ST.setupUi(self)


class Map_READ(QDialog): # 지도 업데이트
    def __init__(self):
        from MAP_KW import Ui_Dialog #MAP 화면 불러오기

        super().__init__() # 상속을 위한 함수

        self.ST = Ui_Dialog() # Ui_Dialog 선언
        self.ST.setupUi(self)

        self.plt = plt # Map화면 구성을 위한 plt

        self.view = QWebEngineView() # Map 화면 구성을 위한 WebEngine

        self.ST.horizontalLayout.addWidget(self.view) # 화면상에 위젯 추가

        self.view.setHtml(mplleaflet.fig_to_html()) # html로 화면 표시

        self.Map_Update = MAP_VIEW(self) # 실시간 업데이트를 위한 Thread
        self.Map_Update.start()
        self.Map_Update.GPS_UPDATE.connect(self.RECV_UPDATE) #GPS 데이터 수신 시 Event 함수

    @Slot(str)
    def RECV_UPDATE(self,loc):
        #RECV_INDEX,SET_INDEX = 현재 수신 위치,현재 송신 위치
        #LOCATION = ex) [3,2,4,1,5]
        global GPS,LOCATION,SET_INDEX,RECV_INDEX,FLOW_DATA,GPS

        Xe = 0 #X방향 3개의 GPS 중심 값 초기화 함수
        Yn = 0 #Y방향 3개의 GPS 중심 값 초기화 함수
        
        try:

            self.plt.xlim([-180,180])#메르카토르 도법 기준 -180~180
            self.plt.ylim([-90,90])#메르카토르 도법 기준 -90~90
            #해당 X,Y축의 한계를 지정해주지 않으면 화면 상의 크기가 계속 바뀌게 된다.

            if len(LOCATION) >=3: # 데이터가 3개 이상일 때
                try:
                    if FLOW_DATA[SET_INDEX.value][RECV_INDEX.value] != None and FLOW_DATA[LOCATION[LOCATION.index(SET_INDEX.value+1)-1]-1][LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1] != None:

                        VEC_1 = np.rad2deg(np.arctan2(GPS[SET_INDEX.value][1]-GPS[RECV_INDEX.value][1],GPS[SET_INDEX.value][0]-GPS[RECV_INDEX.value][0]))#두 위치 각도 계산
                        VEC_2 = np.rad2deg(np.arctan2(GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][1]-GPS[RECV_INDEX.value][1],GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][0]-GPS[RECV_INDEX.value][0])) #두 위치 각도 계산

                        V = list(map(float,np.dot(np.linalg.inv(np.array([[np.cos(VEC_1),np.sin(VEC_1)],[np.cos(VEC_2),np.sin(VEC_2)]])),np.array([FLOW_DATA[RECV_INDEX.value][SET_INDEX.value],FLOW_DATA[RECV_INDEX.value][LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1]]))))
                        #[[cos a,sin a],[cos b, sin b]]^-1*[[Vab],[Va'b']] = [Ve,Vn]

                        Ve,Vn = V[0],V[1] # 동쪽 속도, 북쪽 속도

                        # print(Ve,Vn)

                        Xe = (GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][0]+GPS[SET_INDEX.value][0]+GPS[RECV_INDEX.value][0])/3 #동쪽 방향 세 점의 중심
                        Yn = (GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][1]+GPS[SET_INDEX.value][1]+GPS[RECV_INDEX.value][1])/3 #북쪽 방향 세 점의 중심

                        self.plt.quiver(Xe,Yn,Ve,Vn,scale=1,scale_units='xy') # 벡터 표시

                except: #예외 처리 시
                    Xe = (GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][0]+GPS[SET_INDEX.value][0]+GPS[RECV_INDEX.value][0])/3
                    Yn = (GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][1]+GPS[SET_INDEX.value][1]+GPS[RECV_INDEX.value][1])/3

                    self.plt.plot(Xe,Yn,'ko',markersize=10)# 세점의 검은색 원 표시

            self.plt.plot([GPS[LOCATION[i]-1][0] for i in range(len(LOCATION))],[GPS[LOCATION[i]-1][1] for i in range(len(LOCATION))],'ro',markersize=10) # 세점의 붉은색 원 표시

            self.view.setHtml(mplleaflet.fig_to_html()) # 화면상 출력

        except Exception as e:
            print(e)#에러 발생 시
            self.plt.plot([0 for i in range(len(LOCATION))],[0 for i in range(len(LOCATION))],'bo',markersize=10)#세점의 파란색 원 표시 위도,경도 0,0
            self.view.setHtml(mplleaflet.fig_to_html())#화면상 출력

class MAP_VIEW(QThread):
    GPS_UPDATE = Signal(str)
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

    def run(self):
        global recv_Map_Que
        while True:
            if recv_Map_Que.empty() != True:
                recv_Map_Que.get()
                self.GPS_UPDATE.emit('RECV_MAP')#QThread를 통하여 맵 화면을 업데이트 하기위한 함수

class WindowClass(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()#QMainWindow 상속
        self.setupUi(self)

        '''DEFAULT SETTING'''
        global C_ORDER

        self.start_time = list(filter(None,ctime().split(' '))) #초기 데이터 저장용 시간 계산

        if not os.path.exists('./KW_CSV_Data'): #초기 데이터 저장용 폴더가 없을 경우 생성
            os.makedirs('./KW_CSV_Data')

        if not os.path.exists('./KW_CSV_Data/%s'%self.start_time[-1]): #초기 데이터 저장용 폴더가 없을 경우 생성
            os.makedirs('./KW_CSV_Data/%s'%self.start_time[-1])

        if not os.path.exists('./KW_CSV_Data/%s/%s'%(self.start_time[-1],self.start_time[1])): #초기 데이터 저장용 폴더가 없을 경우 생성
            os.makedirs('./KW_CSV_Data/%s/%s'%(self.start_time[-1],self.start_time[1]))
        
        if not os.path.exists('./KW_CSV_Data/%s/%s/%s'%(self.start_time[-1],self.start_time[1],self.start_time[2])): #초기 데이터 저장용 폴더가 없을 경우 생성
            os.makedirs('./KW_CSV_Data/%s/%s/%s'%(self.start_time[-1],self.start_time[1],self.start_time[2]))

        C_ORDER = self.comboBox_5.currentIndex()
        self.tp = QDialog_TEMP_DEPTH() # 센서 깊이 및 온도 Thread 
        self.w = QDialog_Version_Check() # Info Thread
        self.L = Setting_Location() # Location Thread
        self.Map_ = Map_READ() # Map Thread

        ''' Thread Setting'''
        self._Worker = Worker(self) # Worker Thread
        self._ProcessFunc = Process_Function(self) # 함수 Queue 세팅 Thread
        self.VERSION_UPDATE = VERSION_UPDATE(self) # INfo Update Thread
        self._TEDE_UPDATE = TEDE_UPDATE(self) # 센서 온도 및 깊이 Update Thread
        self._QTimeSet = Q_TimeSet(self) # 동작 관련 Thread
        self._QDTREAD = Q_DATAREAD(self) # 데이터 업데이트 관련 Thread
        self._AUTOSAVE = DATA_LOG_AUTO_SAVE(self) # 자동 저장 관련 Thread
        self._Worker.SendData.connect(self.Setting_Axis)#Signal/Slot 연동
        self._ProcessFunc.DT_SEND.connect(self.DATA_UPDATE)#Signal/Slot 연동
        self._ProcessFunc.CL_TEXT.connect(self.CLEAR_TEXT)#Signal/Slot 연동
        self._ProcessFunc.UPDATE_LED.connect(self.Update_LED)#Signal/Slot 연동
        self._Worker.start()#Thread 동작
        self._ProcessFunc.start()#Thread 동작
        ''''''

        ''' Button Connection '''
        self.pushButton.clicked.connect(self.Version_stack) #InFo 버튼연동
        self.pushButton_5.clicked.connect(self.TimeSet) #동작 관련 버튼연동
        self.pushButton_2.clicked.connect(self.Stop_Setting) #정지 관련 버튼연동
        self.pushButton_4.clicked.connect(self.Setting_Start_STATION) #버튼연동
        self.pushButton_3.clicked.connect(self.LOLA_READ) #위도 경도 보여주기 버튼연동
        self.pushButton_6.clicked.connect(self._TEDE_OPEN) #센서 온도 및 깊이 버튼연동
        self.pushButton_7.clicked.connect(self.DISTANCE_CHECK) #거리 계산 버튼연동
        self.pushButton_9.clicked.connect(self.READ_Map) #맵 관련 버튼연동

        '''ALERT_LED'''
        self.BOARD_ALERT_LED = [self.BOARD_LED_1,self.BOARD_LED_2,self.BOARD_LED_3,self.BOARD_LED_4,self.BOARD_LED_5]
        self.DSP_ALERT_LED = [self.DSP_LED_1,self.DSP_LED_2,self.DSP_LED_3,self.DSP_LED_4,self.DSP_LED_5]
        ''''''
    
    @Slot(int)
    def Setting_Axis(self,Length):
        self._Worker.terminate() # Station 개수 삽입 Thread 동작 종료
        global Axis_data,LOCATION
        '''
        동작 진입 시 해당 함수 동작
        화면 출력 전 초기화 진행
        '''
        Axis_data = [0 for i in range(Length)] # Station 개수 만큼 0데이터 생성
        self.COMBO_ = [0 for i in range(Length)]#Station 개수 만큼 0데이터 생성
        self.btn = QPushButton(self) # 버튼 생성
        self.btn.setObjectName(u"pushButton")
        self.btn.setStyleSheet(u"QPushButton{	\n"
"	background-color:rgb(255,255,255);\n"
"	color:rgb(0,0,0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgb(102, 102, 102);\n"
"	color:rgb(255,255,255);\n"
"}") # 버튼 백그라운드 설정
        self.btn.setText(QCoreApplication.translate("Dialog", u"SET", None)) # Location에 버튼 생성

        for i in range(Length):
            self.COMBO_[i] = QComboBox(self)
            self.COMBO_[i].setStyleSheet(u"background-color:rgb(255,255,255);")
            self.L.ST.horizontalLayout.addWidget(self.COMBO_[i]) # Station 개수만큼 LOCATION에 생성
        self.L.ST.horizontalLayout.addWidget(self.btn)# LOCATION 버튼 추가

        self.btn.clicked.connect(self.Setting_L) # 버튼 연동

        for i in range(Length):
            Axis_data[i] = pg.PlotWidget(title="STATION %s"%str(i+1)) # 그래프 초기 생성
            Axis_data[i].showGrid(x=True,y=True) #그래프 Grid 세팅
            self.comboBox_2.addItem("STATION %s"%str(i+1))#메인화면 내 위도 경도 관련 콤보박스 생성
            self.tp.TEDE.comboBox.addItem('STATION %s'%str(i+1))#온도 콤보박스 생성
            self.verticalLayout_13.addWidget(Axis_data[i])# 그래프 삽입
            self.w.GPS_LABEL[i].setText(str(GPS[i]))#GPS 초기 라벨 생성
            LOCATION.append(i+1)
            for j in range(5):
                self.COMBO_[i].addItem('STATION %s'%str(j+1))

    def Version_stack(self):
        global ProcessingQue
        self.w.show()#Info 정보 보여주기

    def TimeSet(self):
        global ProcessingQue,Interval,select_hour,select_min,Index_Number,OrderNumber,LOCATION,DISTANCE,RT_data,RT_INDEX,FLOW_DATA,DATA_DEPTH,DATA_TEMP,DATA_TIME,ORDER_STRING,Axis_data
        try:
            self.textBrowser.clear() # 동작 진행 시 데이터 로그 지우기
            '''초기 데이터 세팅'''
            DISTANCE = [[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)]]
            RT_data = [[],[],[],[],[]]
            RT_INDEX = [[],[],[],[],[]]
            FLOW_DATA =[[None for i in range(5)],[None for i in range(5)],[None for i in range(5)],[None for i in range(5)],[None for i in range(5)]]
            DATA_TEMP = [[0],[0],[0],[0],[0]]
            DATA_DEPTH = [[0],[0],[0],[0],[0]]
            DATA_TIME = [[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()]]

            self.start_time = list(filter(None,ctime().split(' '))) # 동작 시작 시 시간 계산

            Index_Number = 0
            select_hour = int(self.lineEdit.text())%24
            select_min = int(self.lineEdit_2.text())%60
            Interval = int(self.lineEdit_3.text())
            self.pushButton_5.setDisabled(True) #TimeSet 버튼 동작 시 LOCATION SET Disable
            self.pushButton_4.setDisabled(True) #TimeSet 버튼 동작 시 Time Set Disable
            
            for i in range(len(Axis_data)):
                Axis_data[i].clear()
            ''''''

            '''Order Number 지정''' #12오더 고정
            OrderNumber = 65520
            ''''''

            self.textBrowser.append('%s : WAIT STATION %s'%(ctime(),LOCATION[Index_Number]))
            ProcessingQue.put('TimeSet')
            self._AUTOSAVE.start()#자동 저장 실행 3시간 기준

        except:
            self.MessageBox.setText('숫자를 잘못 입력하셨습니다.')
            self.MessageBox.setWindowTitle('Alert')
            self.MessageBox.setStyleSheet("background-color: rgba(16,30,41,240);color: rgb(255, 255, 255)")
            self.MessageBox.exec_()
    
    def Stop_Setting(self):
        '''
        데이터 프로토콜에 따른 Broker 및 Topic 설정
        '''

        global ProcessingQue,Thread_Working,broker,GPS

        topic = "Core/test12343Demension/data" # 데이터 송신 관련 TOPIC

        self.pushButton_5.setDisabled(False) # Stop 버튼 동작 시 LOCATION SET Enable
        self.pushButton_4.setDisabled(False) # STop 버튼 동작 시 Time Set Enable

        publish.single(topic,b'STOP',hostname=broker) # Mqtt 데이터 송신

        ProcessingQue.put('Stop') # Queue 데이터 송신

        self.textBrowser.append('%s : STOP'%ctime()) #데이터로그 출력

        self.Update_LED('STOP_LED') # LED 초기화

        for i in range(len(self.w.GPS_LABEL)): # GPS 초기화
            GPS[i] = [0,0]
            self.w.GPS_LABEL[i].setText(str(GPS[i]))

        try:
            with open('./KW_CSV_Data/%s/%s/%s/%s_DATA_LOG.txt'%(self.start_time[-1],self.start_time[1],self.start_time[2],re.sub(" |:","_",ctime())),'w') as file:
                file.write(self.textBrowser.toPlainText()) #데이터 로그 저장
        except:
            pass

    def Setting_Start_STATION(self):
        self.L.show()
    
    @Slot(str)
    def DATA_UPDATE(self,DATA_RECV): # DRAW DATE PLOT
        #RECV_INDEX,SET_INDEX = 현재 수신 위치-1 (0번->1번),현재 송신 위치-1 (0번->1번)
        global Axis_data,RT_data,RECV_INDEX,LOCATION,DISTANCE,GPS,SET_INDEX,OrderNumber,RT_INDEX,FLOW_DATA,ProcessingQue,COLOR_SET

        self.textBrowser.append('STATION %s INDEX : %s'%(RECV_INDEX.value+1,RT_INDEX[RECV_INDEX.value][-1]+2000)) # 데이터 로그 인덱스 번호 출력

        Dis_Dat = 0 # 거리 데이터
        Flow_DT = 0 # 유속 초기값

        try:
            if GPS[RECV_INDEX.value] != [0,0] and GPS[SET_INDEX.value] != [0,0] and len(RT_data[SET_INDEX.value])!=0 and len(RT_data[RECV_INDEX.value])!=0:
                if LOCATION[LOCATION.index(RECV_INDEX.value+1)] == LOCATION[LOCATION.index(SET_INDEX.value+1)-1]: #현재 위치와 이전 위치가 맞다면 ex) [2,3,1] SET_INDEX가 1일 때, 3이 맞다면
                    Dis_Dat = int(haversine(GPS[RECV_INDEX.value][::-1],GPS[SET_INDEX.value][::-1],unit='m')) # 데이터 거리
                    DISTANCE[RECV_INDEX.value][SET_INDEX.value],DISTANCE[SET_INDEX.value][RECV_INDEX.value] = Dis_Dat,Dis_Dat
                    self.textBrowser.append('STATION %s - STATION %s : %s m '%(SET_INDEX.value+1,RECV_INDEX.value+1,Dis_Dat))
                    t1 = (RT_INDEX[SET_INDEX.value][-1]+2000-OrderNumber)/22000 #t1의 시간
                    t2 = (RT_INDEX[RECV_INDEX.value][-1]+2000-OrderNumber)/22000 #t2의 시간
                    Flow_DT = (Dis_Dat/2)*((1/t1)-(1/t2)) # 유속 송신위치 - 수신위치
                    FLOW_DATA[SET_INDEX.value][RECV_INDEX.value],FLOW_DATA[RECV_INDEX.value][SET_INDEX.value] = Flow_DT,-Flow_DT #송신위치-수신위치,수신위치-송신위치
                    self.textBrowser.append('Flow Velocity : %.2f m/s'%Flow_DT)#유속 데이터 로그 표시

                    if len(LOCATION) >= 3:
                        if FLOW_DATA[LOCATION[LOCATION.index(RECV_INDEX.value+1)-2]][LOCATION[LOCATION.index(RECV_INDEX.value+1)-3]] != None and FLOW_DATA[LOCATION[LOCATION.index(RECV_INDEX.value+1)-3]][LOCATION[LOCATION.index(RECV_INDEX.value+1)-2]] != None:
                            FLOW_DATA[LOCATION[LOCATION.index(RECV_INDEX.value+1)-2]][LOCATION[LOCATION.index(RECV_INDEX.value+1)-3]],FLOW_DATA[LOCATION[LOCATION.index(RECV_INDEX.value+1)-3]][LOCATION[LOCATION.index(RECV_INDEX.value+1)-2]] = None,None
                    
                    ProcessingQue.put('RECV_MAP') # 맵 화면 업데이트를 위해 Queue 삽입

            SORTED_INDEX = sorted(LOCATION) #순서대로 LOCATION 변경
            Axis_data[SORTED_INDEX.index(RECV_INDEX.value+1)].plot(RT_data[RECV_INDEX.value],clear=True,pen=COLOR_SET[RECV_INDEX.value]) #메인화면상 그래프 표시
            Axis_data[SORTED_INDEX.index(RECV_INDEX.value+1)].setXRange(RT_INDEX[RECV_INDEX.value][-1],RT_INDEX[RECV_INDEX.value][-1]+4000) #메인화면 그래프 내 x범위 설정
        except:
            pass

    def LOLA_READ(self): #LONGITUDE LATITUDE SHOW LOG
        global GPS
        self.textBrowser.append('%s - %s'%(self.comboBox_2.currentText(),str(GPS[int(self.comboBox_2.currentText()[-1])-1])))#두 위치의 거리 데이터 로그 표시

    def _TEDE_OPEN(self):
        global TEDE_INDEX
        TEDE_INDEX = int(self.tp.TEDE.comboBox.currentText()[-1])-1 # 온도와 깊이 인덱스 설정(콤보박스 이용 시 필요)
        self.tp.show()#온도와 깊이 화면 보여주기

    def Setting_L(self):#LOCATION 위치 변경 시 함수 동작
        '''
        데이터 프로토콜에 따른 Broker 및 Topic 설정
        '''
        global LOCATION,Axis_data,broker
        topic = "Core/test12343Demension/data" # MQTT 통신 시 데이터 송신 토픽
        TEMP = []
        for i in range(len(LOCATION)):
            TEMP.append(self.COMBO_[i].currentIndex()+1) # 임시 리스트에 함수 담아 두기
        if len(set(TEMP)) != len(LOCATION):#현재 위치의 개수와 TEMP의 개수가 다를 시(SET함수를 적어 중복이 없게 동작)
            self.MessageBox.setText('위치를 다르게 설정해주세요.')
            self.MessageBox.setWindowTitle('Alert')
            self.MessageBox.setStyleSheet("background-color: rgba(16,30,41,240);color: rgb(255, 255, 255)")
            self.MessageBox.exec_()
        else:
            for i in range(len(LOCATION)):# 같을 시 LOCATION 설정
                LOCATION[i] = self.COMBO_[i].currentIndex()+1
            
            for i in range(len(LOCATION)):#위의 로케이션 설정이 완료되면 해당 위치대로 재배치
                self.verticalLayout_13.removeWidget(Axis_data[i])# 축 데이터 삭제
                self.tp.TEDE.comboBox.removeItem(0)# 센서 온도 및 깊이 화면 내 콤보박스 삭제
                self.comboBox_2.removeItem(0)#메인화면 내 콤보 박스 삭제
                Axis_data[i] = pg.PlotWidget(title="STATION %s"%str(sorted(LOCATION)[i]))#메인화면 내 그래프 설정
                Axis_data[i].showGrid(x=True,y=True)# 메인화면 내 그래프 그리드 표시
                self.verticalLayout_13.addWidget(Axis_data[i]) # 메인화면 내 그래프 삽입
                self.tp.TEDE.comboBox.addItem("STATION %s"%str(sorted(LOCATION)[i]))# 센서 온도 및 깊이 화면 내 콤보박스 재설정
                self.comboBox_2.addItem("STATION %s"%str(sorted(LOCATION)[i]))#메인화면 내 콤보 박스 재설정
            
            publish.single(topic,b'LOCATION,'+bytes(str(LOCATION)[1:-1],'utf-8'),hostname=broker)#MQTT 데이터 송신
            self.textBrowser.append('%s : LOCATION SETTING DONE %s'%(ctime(),str(LOCATION)))#데이터 로그 화면 출력
            self.L.close()#자동 닫기

    def DISTANCE_CHECK(self):#거리 체크 버튼 동작시 이벤트 발생
        global ProcessingQue
        ProcessingQue.put('DISTANCE')#거리 체크
    
    def READ_Map(self):#맵 버튼 동작시 이벤트 발생
        self.Map_.show()# 맵 화면 보여주기

    @Slot(str)
    def CLEAR_TEXT(self,Dt):#데이터 로그 삭제
        self.textBrowser.clear()# 데이터 로그 삭제 동작

    @Slot(str)
    def Update_LED(self,dt):#LED 업데이트 동작
        WORKING_LED = [self.label_7,self.label_9,self.label_10,self.label_11,self.label_12] # LED 라벨
        if 'ERR_BOARD_TEMP' in dt:# 보드 온도 에러 동작 시
            self.BOARD_ALERT_LED[int(dt.split()[0])].setStyleSheet("background-color:Red") # LED 붉은 색상 변경
        elif 'NOR_BOARD_TEMP' in dt:# 보드 온도 노말 동작 시
            self.BOARD_ALERT_LED[int(dt.split()[0])].setStyleSheet("background-color:Lime") # LED 초록 색상 변경
        elif 'ERR_DSP_TEMP' in dt:# DSP 온도 에러 동작 시 
            self.DSP_ALERT_LED[int(dt.split()[0])].setStyleSheet("background-color:Red") # LED 붉은 색상 변경
        elif 'NOR_DSP_TEMP' in dt:# DSP 온도 노말 동작 시
            self.DSP_ALERT_LED[int(dt.split()[0])].setStyleSheet("background-color:Lime") # LED 초록 색상 변경
        elif 'STOP_LED' in dt:# STOP 버튼 클릭 시 동작
            for i in range(len(WORKING_LED)):#동작 LED 붉은 색상으로 모두 변경
                WORKING_LED[i].setStyleSheet("background-color:Red")
        elif 'DATA_LED' in dt:# 동작 LED 동작 시
            DATA_NUMBER = int(dt.split()[0])#LOCATION 위치
            for i in range(len(WORKING_LED)):
                if DATA_NUMBER == i:#현재 로케이션 위치랑 동일하면
                    WORKING_LED[i].setStyleSheet("background-color:Lime")# LED 초록 색상 변경
                else:#다를 시
                    WORKING_LED[i].setStyleSheet("background-color:Red")# LED 붉은 색상 변경

if __name__ == "__main__":

    freeze_support()#EXE 파일 생성 시 Multiprocessing이 무한히 동작치 않게끔 하기 위해 적용

    broker = "test.mosquitto.org" # MQTT 통신 시 브로커 설정
    
    manager = Manager() # list 함수를 전역변수로 사용

    Order = Queue()
    ProcessingQue = Queue()
    MultiProc_Que = Queue()
    VERSION_Que = Queue()
    RTS_READ_Que = Queue()
    recv_Map_Que= Queue()
    Thread_Working = False
    select_hour = 0
    select_min = 0
    Interval = 0
    Index_Number = 1
    C_ORDER = 0
    OrderNumber = 0
    TEDE_INDEX = 0
    SET_INDEX = manager.Value('i',0)
    RECV_INDEX = manager.Value('i',0) # 센서 순서
    RTS_TEMP = manager.Value('f',0.0) # 실시간 센서 온도
    RTS_DEPTH = manager.Value('f',0.0) # 실시간 센서 깊이

    Axis_data = []
    ORDER_STRING = {4080 : '8 ORDER', 16368 : '10 ORDER', 65520 : '12 ORDER'} # ORDER 넘버에 따른 가중치
    LOCATION = manager.list([]) #위치 순서 설정 ex) [4,5,2,3,1]
    DISTANCE = [[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)]] # 거리
    DSPEN = manager.list(['Wait' for i in range(5)]) # DSPEN 초기 설정
    TRXPSEN = manager.list(['Wait' for i in range(5)]) # TRXPSEN 초기 설정
    TRXCSEN = manager.list(['Wait' for i in range(5)]) # TRXCSEN 초기 설정
    MNTIN = manager.list(['Wait' for i in range(5)]) # MNTIN 초기 설정
    DC12VMNT = manager.list(['Wait' for i in range(5)]) # DC12VMNT 초기 설정
    BOARD_TEMP = manager.list(['Wait' for i in range(5)]) # BOARD 온도 초기 설정
    GPS = manager.list([[0,0] for i in range(5)]) # GPS 초기 설정
    RT_data = [[],[],[],[],[]] #데이터
    DATA_TEMP = [[0],[0],[0],[0],[0]] #센서 온도
    DATA_DEPTH = [[0],[0],[0],[0],[0]] # 센서 깊이
    DATA_TIME = [[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()]] # 시간 별 센서 온도
    DSP_TEMP = manager.list(['Wait' for i in range(5)]) # DSP 온도 초기 설정
    RT_INDEX = [[],[],[],[],[]] # 데이터 인덱스 번호
    FLOW_DATA =[[None for i in range(5)],[None for i in range(5)],[None for i in range(5)],[None for i in range(5)],[None for i in range(5)]] # 유속
    COLOR_SET = [pg.mkPen(color=(0,255,0),width=1),pg.mkPen(color=(255,0,0),width=1),pg.mkPen(color=(255,0,255),width=1),pg.mkPen(color=(255,255,0),width=1),pg.mkPen(color=(0,255,255),width=1)] # 그래프 색상
    BOARD_LED = [0 for i in range(5)]# BOARD LED 초기 설정
    DSP_LED = [0 for i in range(5)]# DSP LED 초기 설정

    try:
        p1 = Process(target=Multi_Calc,args=(LOCATION,MultiProc_Que,ProcessingQue,SET_INDEX,RECV_INDEX,DSPEN,TRXPSEN,TRXCSEN,MNTIN,DC12VMNT,BOARD_TEMP,RTS_TEMP,RTS_DEPTH,DSP_TEMP),daemon=True) # MultiProcessing 동작
        p2 = Process(target=Multi_GPS,args=(ProcessingQue,GPS,),daemon=True) # MultiProcessing 동작

        p1.start() #MultiProcessing 동작 시작
        p2.start() #MultiProcessing 동작 시작

        app = QApplication(sys.argv)

        mainwindow = WindowClass()
        Setting = QDialog_Setting()

        Setting.show() # 세팅 화면 보여주기

        '''
        동작 종료 시 발생 함수
        '''
        app_return = app.exec_() # 동작 종료

        mainwindow._Worker.terminate()#Worker Thread 종료
        mainwindow._ProcessFunc.terminate()#ProcessFunc Thread 종료
        mainwindow.VERSION_UPDATE.terminate()#VERSION_UPDATE Thread 종료
        mainwindow._TEDE_UPDATE.terminate()#온도 및 깊이 Thread 종료
        mainwindow._QTimeSet.terminate()#TimeSet Thread 종료
        mainwindow._QDTREAD.terminate()#데이터 읽기 종료
        mainwindow.tp.READ_DT.terminate()#
        mainwindow.Map_.Map_Update.terminate()#
        mainwindow._AUTOSAVE.terminate()
        p1.terminate()#MultiProcessing 종료
        p2.terminate()#MultiProcessing 종료
        sys.exit(app_return)#동작 종료
        
    except Exception as e:
        print(e)
