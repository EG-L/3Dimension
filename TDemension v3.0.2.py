import sys
import os
from multiprocessing import Queue,freeze_support,Process,Manager
from PySide2.QtWidgets import QMainWindow, QApplication,QMessageBox,QDialog,QComboBox,QPushButton,QFileDialog
from PySide2.QtCore import *
from PySide2.QtGui import *
from datetime import datetime
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
import time
import pyqtgraph as pg
from TOMO_COSTAL_KW_v1 import Ui_MainWindow
import numpy as np
from time import ctime
from haversine import haversine
import matplotlib.pyplot as plt
import mplleaflet
import matplotlib
from PySide2.QtWebEngineWidgets import QWebEngineView
import pandas as pd
import re

def Multi_Calc(LOC,read_que,send_que,set_location,location,DSPEN,TRXPSEN,TRXCSEN,MNTIN,DC12VMNT,BOARD_TEMP,RTS_TEMP,RTS_DEPTH,DSP_TEMP):
    while True:
        if read_que.empty() != True:
            Dat = read_que.get()
            try:
                Data = list(map(float,Dat.decode().split(',')))
                set_location.value = int(Data.pop(0))-1
                location.value = int(Data.pop(0))-1

                if location.value+1 in LOC:
                    DSPEN[location.value] = Data.pop(0)
                    TRXPSEN[location.value] = Data.pop(0)
                    TRXCSEN[location.value] = Data.pop(0)
                    DC12VMNT[location.value] = Data.pop(0)
                    MNTIN[location.value] = Data.pop(0)
                    BOARD_TEMP[location.value] = Data.pop(0)
                    RTS_TEMP.value = Data.pop(0)
                    RTS_DEPTH.value = Data.pop(0)
                    Data.pop(0) #FPGA_Working
                    DSP_TEMP[location.value] = Data.pop(0)

                    send_que.put('RECV_RTS_DATA')
                    time.sleep(0.1)
                    send_que.put('RECV_ETC')
                    time.sleep(0.1)
                    send_que.put(list(map(int,Data)))
                else:
                    send_que.put('Error_RECV')
            except:
                send_que.put('Error_RECV')
        time.sleep(0.1)

def Multi_GPS(send_que,GPS_DATA): # GPS UPDATE
    broker = "test.mosquitto.org"
    topic = "Core/test12343Demension/version"
    while True:
        try:
            m = subscribe.simple(topic,hostname=broker,keepalive=20)
            dat = list(map(float,m.payload.decode().split(',')))
            GPS_DATA[int(dat[0])-1] = dat[1:]
            if dat[1] == 0 and dat[2] == 0:
                send_que.put('STATION %s GPS_ERROR'%int(dat[0]))
            else: 
                send_que.put('RECV_GPS')
            time.sleep(0.1)
        except Exception as e:
            print(e)
            print("1")
            continue

class QDialog_Setting(QDialog): ## SETTING
    def __init__(self):
        from Setting_KW import Ui_Dialog

        super().__init__()

        self.w =  Ui_Dialog()

        self.w.setupUi(self)

        self.w.pushButton.clicked.connect(self.openWindowClass)

    def openWindowClass(self):
        if self.w.lineEdit.text().upper() == 'KW' and self.w.lineEdit_2.text() == '1234': 
            mainwindow.show()
            global Order,Setting
            Order.put(int(self.w.comboBox.currentText()))
            Setting.close()
        else:
            messagebox = QMessageBox()
            messagebox.setText('아이디 또는 비밀번호를 잘못 입력하셨습니다.')
            messagebox.setWindowTitle('Alert')
            messagebox.setStyleSheet("background-color: rgba(16,30,41,240);color: rgb(255, 255, 255)")
            messagebox.exec_()

class VERSION_UPDATE(QThread):
    VERSION_DAT = Signal(str)
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

    def run(self):
        global VERSION_Que,GPS
        if VERSION_Que.empty() != True:
            Dat = VERSION_Que.get()
            if Dat == 'RECV_GPS':
                for i in range(len(self.parent.w.GPS_LABEL)):
                    self.parent.w.GPS_LABEL[i].setText('[%.2f,%.2f]'%(GPS[i][0],GPS[i][1]))
            elif Dat == 'RECV_ETC':
                for i in range(len(self.parent.w.ALL_RECV_DATA_LABEL)):
                    for j in range(len(self.parent.w.ALL_RECV_DATA_LABEL[i])):
                        self.parent.w.ALL_RECV_DATA_LABEL[i][j].setText(str(self.parent.w.ALL_RECV_DATA[i][j]))

class QDialog_Version_Check(QDialog): ## VERSION INFO
    def __init__(self):
        from version_check_KW import Ui_Dialog

        super().__init__()

        self.w = Ui_Dialog()

        self.w.setupUi(self)

        global DSPEN,TRXPSEN,TRXCSEN,MNTIN,DC12VMNT,BOARD_TEMP,GPS,DSP_TEMP

        self.DSPEN_LABEL = [self.w.label_6,self.w.label_26,self.w.label_27,self.w.label_28,self.w.label_29]
        self.TRXPSEN_LABEL = [self.w.label_8,self.w.label_30,self.w.label_31,self.w.label_32,self.w.label_33]
        self.TRXCSEN_LABEL = [self.w.label_10,self.w.label_34,self.w.label_35,self.w.label_36,self.w.label_37]
        self.MNTIN_LABEL = [self.w.label_21,self.w.label_22,self.w.label_23,self.w.label_24,self.w.label_25]
        self.DC12VMNT_LABEL = [self.w.label_38,self.w.label_39,self.w.label_40,self.w.label_41,self.w.label_42]
        self.BOARD_TEMP_LABEL = [self.w.label_45,self.w.label_44,self.w.label_48,self.w.label_47,self.w.label_46]
        self.GPS_LABEL = [self.w.label_52,self.w.label_51,self.w.label_53,self.w.label_50,self.w.label_54]
        self.DSP_TEMP_LABEL = [self.w.label_2,self.w.label_11,self.w.label_12,self.w.label_13,self.w.label_14]

        self.ALL_RECV_DATA_LABEL = [self.DSPEN_LABEL,self.TRXPSEN_LABEL,self.TRXCSEN_LABEL,self.MNTIN_LABEL,self.DC12VMNT_LABEL,self.BOARD_TEMP_LABEL,self.DSP_TEMP_LABEL]
        self.ALL_RECV_DATA = [DSPEN,TRXPSEN,TRXCSEN,MNTIN,DC12VMNT,BOARD_TEMP,DSP_TEMP]

        for i in range(len(self.ALL_RECV_DATA_LABEL)):
            for j in range(len(self.ALL_RECV_DATA_LABEL[i])):
                self.ALL_RECV_DATA_LABEL[i][j].setText(self.ALL_RECV_DATA[i][j])

    def closeEvent(self, event):
        self.close()

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

class Q_TimeSet(QThread):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.topic = "Core/test12343Demension/data"
    
    def run(self):
        global ProcessingQue,Axis_data,Thread_Working,Interval,Index_Number,select_hour,select_min,LOCATION,broker,DATA_DEPTH,DATA_TEMP,DATA_TIME,ORDER_STRING,OrderNumber

        if self.parent.start_time[2] != list(filter(None,ctime().split(' ')))[2]:

            with open('./KW_CSV_Data/%s/%s/%s/%s_DATA_LOG.txt'%(self.start_time[-1],self.start_time[1],self.start_time[2],re.sub(" |:","_",ctime())),'w') as file:
                file.write(self.textBrowser.toPlainText())

            DATA_TEMP = [[0],[0],[0],[0],[0]]
            DATA_DEPTH = [[0],[0],[0],[0],[0]]
            DATA_TIME = [[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()]]
            
            self.parent.start_time = list(filter(None,ctime().split(' ')))

            ProcessingQue.put('CLEAR_TEXT')

            if not os.path.exists('./KW_CSV_Data'):
                os.makedirs('./KW_CSV_Data')

            if not os.path.exists('./KW_CSV_Data/%s'%self.parent.start_time[-1]):
                os.makedirs('./KW_CSV_Data/%s'%self.parent.start_time[-1])

            if not os.path.exists('./KW_CSV_Data/%s/%s'%(self.parent.start_time[-1],self.parent.start_time[1])):
                os.makedirs('./KW_CSV_Data/%s/%s'%(self.parent.start_time[-1],self.parent.start_time[1]))
            
            if not os.path.exists('./KW_CSV_Data/%s/%s/%s'%(self.parent.start_time[-1],self.parent.start_time[1],self.parent.start_time[2])):
                os.makedirs('./KW_CSV_Data/%s/%s/%s'%(self.parent.start_time[-1],self.parent.start_time[1],self.parent.start_time[2]))

        if select_min <= datetime.now().minute: # 선택 분이 더 작거나 같으면
            if select_hour == datetime.now().hour: # 선택 시간이랑 현재 시간이랑 동일할 때
                if datetime.now().minute+1 >=60: # 현재 시각이 59분일 때
                    select_hour = (select_hour+1)%24 # 시간을 1시간 더해준다.
                select_min = (datetime.now().minute+1)%60 # 분을 1분 더해준다.

        Dat = bytes(str(select_hour)+","+str(select_min)+","+str(Interval)+","+str(LOCATION[Index_Number]),'utf-8')
        
        publish.single(self.topic,b'STOP,'+Dat+b',START',hostname=broker,keepalive=0)

        while True:
            if datetime.now().minute == select_min and datetime.now().hour == select_hour:
                break
            time.sleep(0.1)

        ProcessingQue.put('DATA_READ')

        select_hour = (select_hour+(select_min+Interval)//60)%24
        select_min = (select_min+Interval)%60
        
        # time.sleep(0.1)

        if Index_Number == len(Axis_data)-1:
            Index_Number = -1
        Index_Number+=1

        self.parent.textBrowser.append('\n%s : %s WAIT STATION %s\n'%(ctime(),ORDER_STRING[OrderNumber],LOCATION[Index_Number]))
        ProcessingQue.put('TimeSet')

class Q_DATAREAD(QThread): # SUBSCRIBE DATA READ
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.topic = "Core/sendTestData1234/data"

    def run(self):
        global Axis_data,ProcessingQue,Index_Number,LOCATION,broker
        Compare_Data = LOCATION[Index_Number-1]
        while True:
            m = subscribe.simple(self.topic,hostname=broker,keepalive=20)
            # if int(Dt.decode()[0]) == Compare_Data:
            MultiProc_Que.put(m.payload)

class Process_Function(QThread): ## MAIN QUEUE BUFFER
    DT_SEND = Signal(str)
    CL_TEXT = Signal(str)
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

    def run(self):
        global ProcessingQue,Thread_Working,MultiProc_Que,VERSION_Que,RT_data,RECV_INDEX,RTS_DEPTH,RTS_TEMP,DATA_TEMP,DATA_DEPTH,DATA_TIME,RTS_READ_Que,DISTANCE,GPS,LOCATION,recv_Map_Que,RT_INDEX,SET_INDEX,ORDER_STRING,OrderNumber
        while True:
            if ProcessingQue.empty() != True :
                Data = ProcessingQue.get()
                if Data == 'TimeSet': 
                    Thread_Working = True
                    self.parent._QTimeSet.start()
                elif Data == 'Stop':
                    Thread_Working = False
                    self.parent._QTimeSet.terminate()
                    self.parent._QDTREAD.terminate()
                    if ProcessingQue.empty() != True:
                        while True:
                            ProcessingQue.get()
                            if ProcessingQue.empty() == True:
                                break
                    if MultiProc_Que.empty() != True:
                        while True:
                            MultiProc_Que.get()
                            if MultiProc_Que.empty() == True:
                                break
                elif Data == 'DATA_READ':
                    self.parent._QDTREAD.terminate()
                    self.parent._QDTREAD.start()
                elif Data == 'RECV_GPS': # READ_GPS
                    VERSION_Que.put(Data)
                    self.parent.VERSION_UPDATE.start()
                elif Data == 'RECV_RTS_DATA': # TEMP , DEPTH
                    if DATA_TEMP[RECV_INDEX.value][-1] == 0 and DATA_DEPTH[RECV_INDEX.value][-1] == 0:
                        DATA_TIME[RECV_INDEX.value][-1] = datetime.now()
                        DATA_TEMP[RECV_INDEX.value][-1] = RTS_TEMP.value
                        DATA_DEPTH[RECV_INDEX.value][-1] = RTS_DEPTH.value
                    else:
                        DATA_TIME[RECV_INDEX.value].append(datetime.now())
                        DATA_TEMP[RECV_INDEX.value].append(RTS_TEMP.value)
                        DATA_DEPTH[RECV_INDEX.value].append(RTS_DEPTH.value)
                    
                    if DATA_TEMP[RECV_INDEX.value][-1]>=60:
                        self.parent.textBrowser.append('%s : STATION %s - %s ℃ DATA_TEMP ERROR'%(ctime(),RECV_INDEX.value+1,str(DATA_TEMP[RECV_INDEX.value][-1])))
                    if BOARD_TEMP[RECV_INDEX.value]>=60:
                        self.parent.textBrowser.append('%s : STATION %s - %s ℃ BOARD_TEMP ERROR'%(ctime(),RECV_INDEX.value+1,str(BOARD_TEMP[RECV_INDEX.value])))
                    if DSP_TEMP[RECV_INDEX.value]>=60:
                        self.parent.textBrowser.append('%s : STATION %s - %s ℃ DSP_TEMP ERROR'%(ctime(),RECV_INDEX.value+1,str(DSP_TEMP[RECV_INDEX.value])))

                    RTS_READ_Que.put('DATA_READ')
                elif Data == 'RECV_ETC': # ETC DATA
                    VERSION_Que.put(Data)
                    self.parent.VERSION_UPDATE.start()
                elif type(Data) == list: # READ_DATA
                    try:
                        pd.DataFrame(Data).to_csv('./KW_CSV_Data/%s/%s/%s/%s_Station_%s_Station_%s.csv'%(self.parent.start_time[-1],self.parent.start_time[1],self.parent.start_time[2],re.sub(" |:","_",ctime()),SET_INDEX.value+1,RECV_INDEX.value+1),header=False,index=False)
                    except:
                        print("Not DATA SAVE")
                        pass
                    START_INDEX = Data.pop(0)
                    RT_INDEX[RECV_INDEX.value] = [START_INDEX]
                    DEFAULT_LENGTH = np.array([0]*280000)
                    DEFAULT_LENGTH[START_INDEX:START_INDEX+len(Data)] = np.array(Data)
                    RT_data[RECV_INDEX.value] = list(DEFAULT_LENGTH)
                    self.DT_SEND.emit('DATA_RECV')
                    self.parent.textBrowser.append('%s : %s DATA_RECV_STATION %s'%(ctime(),ORDER_STRING[OrderNumber],str(RECV_INDEX.value+1)))
                
                elif Data == 'Error_RECV':
                    self.parent.textBrowser.append('%s : Error RECV'%ctime())
                
                elif Data == 'DISTANCE':
                    for i in range(len(LOCATION)-1):
                        for j in range(i+1,len(LOCATION)):
                            DISTANCE[LOCATION[i]-1][LOCATION[j]-1],DISTANCE[LOCATION[j]-1][LOCATION[i]-1] = haversine(GPS[LOCATION[i]-1][::-1],GPS[LOCATION[j]-1][::-1],unit='m'),haversine(GPS[LOCATION[i]-1][::-1],GPS[LOCATION[j]-1][::-1],unit='m')
                            self.parent.textBrowser.append('%s - %s : %s m SET'%(LOCATION[i],LOCATION[j],DISTANCE[LOCATION[i]-1][LOCATION[j]-1]))
                            break
                    
                    DISTANCE[LOCATION[-1]-1][LOCATION[0]-1],DISTANCE[LOCATION[0]-1][LOCATION[-1]-1] = haversine(GPS[LOCATION[-1]-1][::-1],GPS[LOCATION[0]-1][::-1],unit='m'),haversine(GPS[LOCATION[-1]-1][::-1],GPS[LOCATION[0]-1][::-1],unit='m')
                    self.parent.textBrowser.append('%s - %s : %s m SET\n'%(LOCATION[-1],LOCATION[0],DISTANCE[LOCATION[-1]-1][LOCATION[0]-1]))
                
                elif Data == 'RECV_MAP':
                    recv_Map_Que.put('UPDATE_MAP')

                elif Data == 'SENSOR_ON':
                    VERSION_Que.put('SENSOR_ON')

                elif Data == 'CLEAR_TEXT':
                    self.CL_TEXT.emit('CLEAR')
                elif 'GPS_ERROR' in Data:
                    self.parent.textBrowser.append(Data)

class TEDE_UPDATE(QThread):
    Update_SEND = Signal(str)
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
    
    def run(self):
        global RTS_READ_Que
        while True:
            if RTS_READ_Que.empty() != True:
                RTS_READ_Que.get()
                self.Update_SEND.emit('U')
            time.sleep(1)

class QDialog_TEMP_DEPTH(QDialog):
    def __init__(self):
        from TOMO_COSTAL_TEMP_KW import Ui_Dialog
        super().__init__()

        self.TEDE = Ui_Dialog()
        self.TEDE.setupUi(self)

        self.TEDE_p1 = self.TEDE.widget.plotItem

        self.TEDE_p2 = pg.ViewBox()
        self.TEDE_p1.showAxis('right')
        self.TEDE_p1.scene().addItem(self.TEDE_p2)
        self.TEDE_p1.getAxis('right').linkToView(self.TEDE_p2)
        self.TEDE_p2.setXLink(self.TEDE_p1)
        self.TEDE_p1.getAxis('right').setPen(pg.mkPen(color=(0,255,0),width=1))

        self.TEDE_p1.setLabel('right', 'Depth', units='m', **{'color': 'rgb(0, 255, 0)', 'font-size': '10pt',
                                'font-family' : 'D2Coding'})
        self.TEDE_p1.setLabel('left','Temperature',units='℃')

        self.READ_DT = TEDE_UPDATE(self)
        self.READ_DT.start()
        self.READ_DT.Update_SEND.connect(self.update_Data)

        self.TEDE.pushButton.clicked.connect(self.Choice_Sensor)

    def Choice_Sensor(self):
        global TEDE_INDEX
        TEDE_INDEX = int(self.TEDE.comboBox.currentText()[-1])-1
        self.update_Data(self)

    @Slot(str)
    def update_Data(self,temp):
        global DATA_DEPTH,DATA_TEMP,TEDE_INDEX
        self.TEDE.label.setText('%s℃'%str(DATA_TEMP[TEDE_INDEX][-1]))
        self.TEDE.label_2.setText('%sm'%str(DATA_DEPTH[TEDE_INDEX][-1]))

        self.TEDE_p1.clear()
        self.TEDE_p2.clear()

        Temperature = self.TEDE_p1.plot(pen=pg.mkPen(color=(255, 255, 255)),name='Temperature')
        Depth = self.TEDE_p1.plot(pen=pg.mkPen(color=(0, 255, 0)),name='Depth')
        curv2 = pg.PlotCurveItem(pen=pg.mkPen(color=(0, 255, 0)),name='Depth')

        self.TEDE_p2.addItem(curv2)

        Temperature.setData(x=[x.timestamp() for x in DATA_TIME[TEDE_INDEX]],y=DATA_TEMP[TEDE_INDEX])
        curv2.setData(x=[x.timestamp() for x in DATA_TIME[TEDE_INDEX]],y=DATA_DEPTH[TEDE_INDEX])

        if len(DATA_TIME[TEDE_INDEX])>=15:
            self.TEDE_p1.setXRange(DATA_TIME[TEDE_INDEX][-15].timestamp(),DATA_TIME[TEDE_INDEX][-1].timestamp(),padding=0)

        self.TEDE_p1.addLegend()

        self.updateViews()
        self.TEDE.widget.plotItem.vb.sigResized.connect(self.updateViews)

    def updateViews(self):
        self.TEDE_p2.setGeometry(self.TEDE_p1.getViewBox().sceneBoundingRect())

        self.TEDE_p2.linkedViewChanged(self.TEDE_p1.getViewBox(), self.TEDE_p2.XAxis)

    def closeEvent(self, event):
        self.close()

class Setting_Location(QDialog):
    def __init__(self):
        from Setting_LOCATION import Ui_Dialog

        super().__init__()

        self.ST = Ui_Dialog()
        self.ST.setupUi(self)


class Map_READ(QDialog): # 지도 업데이트
    def __init__(self):
        from MAP_KW import Ui_Dialog

        super().__init__()

        self.ST = Ui_Dialog()
        self.ST.setupUi(self)

        self.plt = plt

        self.fig = self.plt.figure()

        self.view = QWebEngineView()

        self.ST.horizontalLayout.addWidget(self.view)

        self.view.setHtml(mplleaflet.fig_to_html())

        self.Map_Update = MAP_VIEW(self)
        self.Map_Update.start()
        self.Map_Update.GPS_UPDATE.connect(self.RECV_UPDATE)

    @Slot(str)
    def RECV_UPDATE(self,loc):
        global GPS,LOCATION,SET_INDEX,RECV_INDEX,FLOW_DATA,GPS

        Xe = 0
        Yn = 0
        
        try:
            if len(LOCATION) >=3:
                try:
                    if FLOW_DATA[SET_INDEX.value][RECV_INDEX.value] != None and FLOW_DATA[LOCATION[LOCATION.index(SET_INDEX.value+1)-1]-1][LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1] != None:

                        VEC_1 = np.rad2deg(np.arctan2(GPS[SET_INDEX.value][1]-GPS[RECV_INDEX.value][1],GPS[SET_INDEX.value][0]-GPS[RECV_INDEX.value][0]))
                        VEC_2 = np.rad2deg(np.arctan2(GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][1]-GPS[RECV_INDEX.value][1],GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][0]-GPS[RECV_INDEX.value][0]))

                        V = list(map(float,np.dot(np.linalg.inv(np.array([[np.cos(VEC_1),np.sin(VEC_1)],[np.cos(VEC_2),np.sin(VEC_2)]])),np.array([FLOW_DATA[SET_INDEX.value][RECV_INDEX.value],FLOW_DATA[LOCATION[LOCATION.index(SET_INDEX.value+1)-1]-1][LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1]]))))

                        Ve,Vn = V[0],V[1]

                        Xe = (GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][0]+GPS[SET_INDEX.value][0]+GPS[RECV_INDEX.value][0])/3
                        Yn = (GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][1]+GPS[SET_INDEX.value][1]+GPS[RECV_INDEX.value][1])/3

                        # self.plt.quiver(Xe,Yn,Ve,Vn,scale=1,scale_units='xy')
                        self.plt.quiver(Xe,Yn,Ve,Vn)
                except:
                    Xe = (GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][0]+GPS[SET_INDEX.value][0]+GPS[RECV_INDEX.value][0])/3
                    Yn = (GPS[LOCATION[LOCATION.index(RECV_INDEX.value+1)-1]-1][1]+GPS[SET_INDEX.value][1]+GPS[RECV_INDEX.value][1])/3

                    self.plt.plot(Xe,Yn,'ko')

            self.plt.plot([GPS[LOCATION[i]-1][0] for i in range(len(LOCATION))],[GPS[LOCATION[i]-1][1] for i in range(len(LOCATION))],'rs',markersize=10)
            self.view.setHtml(mplleaflet.fig_to_html())

        except Exception as e:
            print(e)
            print("2")
            self.plt.plot([0 for i in range(len(LOCATION))],[0 for i in range(len(LOCATION))],'bs',markersize=10)
            self.view.setHtml(mplleaflet.fig_to_html())

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
                self.GPS_UPDATE.emit('RECV_MAP')

class WindowClass(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''DEFAULT SETTING'''
        global C_ORDER

        self.start_time = list(filter(None,ctime().split(' ')))

        if not os.path.exists('./KW_CSV_Data'):
            os.makedirs('./KW_CSV_Data')

        if not os.path.exists('./KW_CSV_Data/%s'%self.start_time[-1]):
            os.makedirs('./KW_CSV_Data/%s'%self.start_time[-1])

        if not os.path.exists('./KW_CSV_Data/%s/%s'%(self.start_time[-1],self.start_time[1])):
            os.makedirs('./KW_CSV_Data/%s/%s'%(self.start_time[-1],self.start_time[1]))
        
        if not os.path.exists('./KW_CSV_Data/%s/%s/%s'%(self.start_time[-1],self.start_time[1],self.start_time[2])):
            os.makedirs('./KW_CSV_Data/%s/%s/%s'%(self.start_time[-1],self.start_time[1],self.start_time[2]))

        C_ORDER = self.comboBox_5.currentIndex()
        self.tp = QDialog_TEMP_DEPTH()
        self.w = QDialog_Version_Check()
        self.L = Setting_Location()
        self.Map_ = Map_READ()


        ''' Thread Setting'''
        self._Worker = Worker(self)
        self._ProcessFunc = Process_Function(self)
        self.VERSION_UPDATE = VERSION_UPDATE(self)
        self._TEDE_UPDATE = TEDE_UPDATE(self)
        self._QTimeSet = Q_TimeSet(self)
        self._QDTREAD = Q_DATAREAD(self)
        self._Worker.SendData.connect(self.Setting_Axis)
        self._ProcessFunc.DT_SEND.connect(self.DATA_UPDATE)
        self._ProcessFunc.CL_TEXT.connect(self.CLEAR_TEXT)
        self._Worker.start()
        self._ProcessFunc.start()
        ''''''

        ''' Button Connection '''
        self.pushButton.clicked.connect(self.Version_stack)
        self.pushButton_5.clicked.connect(self.TimeSet)
        self.pushButton_2.clicked.connect(self.Stop_Setting)
        self.pushButton_4.clicked.connect(self.Setting_Start_STATION)
        self.pushButton_3.clicked.connect(self.LOLA_READ)
        self.pushButton_6.clicked.connect(self._TEDE_OPEN)
        self.pushButton_7.clicked.connect(self.DISTANCE_CHECK)
        self.pushButton_9.clicked.connect(self.READ_Map)
    
    @Slot(int)
    def Setting_Axis(self,Length):
        self._Worker.terminate()
        global Axis_data,LOCATION
        Axis_data = [0 for i in range(Length)]
        self.COMBO_ = [0 for i in range(Length)]
        self.btn = QPushButton(self)
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
"}")
        self.btn.setText(QCoreApplication.translate("Dialog", u"SET", None))

        for i in range(Length):
            self.COMBO_[i] = QComboBox(self)
            self.COMBO_[i].setStyleSheet(u"background-color:rgb(255,255,255);")
            self.L.ST.horizontalLayout.addWidget(self.COMBO_[i])
        self.L.ST.horizontalLayout.addWidget(self.btn)

        self.btn.clicked.connect(self.Setting_L)

        for i in range(Length):
            Axis_data[i] = pg.PlotWidget(title="STATION %s"%str(i+1))
            Axis_data[i].showGrid(x=True,y=True)
            self.comboBox_2.addItem("STATION %s"%str(i+1))
            self.tp.TEDE.comboBox.addItem('STATION %s'%str(i+1))
            self.verticalLayout_13.addWidget(Axis_data[i])
            self.w.GPS_LABEL[i].setText(str(GPS[i]))
            LOCATION.append(i+1)
            for j in range(5):
                self.COMBO_[i].addItem('STATION %s'%str(j+1))

    def Version_stack(self):
        global ProcessingQue
        self.w.show()

    def TimeSet(self):
        global ProcessingQue,Interval,select_hour,select_min,Index_Number,OrderNumber,LOCATION,DISTANCE,RT_data,RT_INDEX,FLOW_DATA,DATA_DEPTH,DATA_TEMP,DATA_TIME,ORDER_STRING,Axis_data
        try:
            self.textBrowser.clear()
            '''초기 데이터 세팅'''
            DISTANCE = [[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)]]
            RT_data = [[],[],[],[],[]]
            RT_INDEX = [[],[],[],[],[]]
            FLOW_DATA =[[None for i in range(5)],[None for i in range(5)],[None for i in range(5)],[None for i in range(5)],[None for i in range(5)]]
            DATA_TEMP = [[0],[0],[0],[0],[0]]
            DATA_DEPTH = [[0],[0],[0],[0],[0]]
            DATA_TIME = [[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()]]

            Index_Number = 0
            select_hour = int(self.lineEdit.text())%24
            select_min = int(self.lineEdit_2.text())%60
            Interval = int(self.lineEdit_3.text())
            self.pushButton_5.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            
            for i in range(len(Axis_data)):
                Axis_data[i].clear()
            ''''''

            '''Order Number 지정''' #12오더 고정
            OrderNumber = 65520
            ''''''

            self.textBrowser.append('%s : %s WAIT STATION %s'%(ctime(),ORDER_STRING[OrderNumber],LOCATION[0]))
            ProcessingQue.put('TimeSet')

        except:
            self.MessageBox.setText('숫자를 잘못 입력하셨습니다.')
            self.MessageBox.setWindowTitle('Alert')
            self.MessageBox.setStyleSheet("background-color: rgba(16,30,41,240);color: rgb(255, 255, 255)")
            self.MessageBox.exec_()
    
    def Stop_Setting(self):

        global ProcessingQue,Thread_Working,broker,GPS

        topic = "Core/test12343Demension/data"

        self.pushButton_5.setDisabled(False)
        self.pushButton_4.setDisabled(False)

        publish.single(topic,b'STOP',hostname=broker)

        ProcessingQue.put('Stop')

        self.textBrowser.append('%s : STOP'%ctime())

        for i in range(len(self.w.GPS_LABEL)):
            GPS[i] = [0,0]
            self.w.GPS_LABEL[i].setText(str(GPS[i]))

        with open('./KW_CSV_Data/%s/%s/%s/%s_DATA_LOG.txt'%(self.start_time[-1],self.start_time[1],self.start_time[2],re.sub(" |:","_",ctime())),'w') as file:
            file.write(self.textBrowser.toPlainText())

    def Setting_Start_STATION(self):
        self.L.show()
    
    @Slot(str)
    def DATA_UPDATE(self,DATA_RECV): # DRAW DATE PLOT
        #RECV_INDEX = STATION NUMBER, GPS=[[],[],[],[],[]]
        global Axis_data,RT_data,RECV_INDEX,LOCATION,DISTANCE,GPS,SET_INDEX,OrderNumber,RT_INDEX,FLOW_DATA,ProcessingQue,COLOR_SET

        self.textBrowser.append('STATION %s INDEX : %s'%(RECV_INDEX.value+1,RT_INDEX[RECV_INDEX.value][-1]+2000))

        Dis_Dat = 0 # 거리 데이터
        Flow_DT = 0 # 속도 데이터

        if GPS[RECV_INDEX.value] != [0,0] and GPS[SET_INDEX.value] != [0,0] and len(RT_data[SET_INDEX.value])!=0 and len(RT_data[RECV_INDEX.value])!=0:
            if LOCATION[LOCATION.index(RECV_INDEX.value+1)] == LOCATION[LOCATION.index(SET_INDEX.value+1)-1]: #gps의 값이 0,0이 아니면
                Dis_Dat = int(haversine(GPS[RECV_INDEX.value][::-1],GPS[SET_INDEX.value][::-1],unit='m'))
                DISTANCE[RECV_INDEX.value][SET_INDEX.value],DISTANCE[SET_INDEX.value][RECV_INDEX.value] = Dis_Dat,Dis_Dat
                self.textBrowser.append('STATION %s - STATION %s : %s m '%(SET_INDEX.value+1,RECV_INDEX.value+1,Dis_Dat))
                t1 = (RT_INDEX[SET_INDEX.value][-1]+2000-OrderNumber)/22000
                t2 = (RT_INDEX[RECV_INDEX.value][-1]+2000-OrderNumber)/22000
                Flow_DT = (Dis_Dat/2)*((1/t1)-(1/t2))
                FLOW_DATA[SET_INDEX.value][RECV_INDEX.value],FLOW_DATA[RECV_INDEX.value][SET_INDEX.value] = Flow_DT,Flow_DT
                self.textBrowser.append('Flow Velocity : %s m/s'%Flow_DT)

                if len(LOCATION) >= 3:
                    if FLOW_DATA[LOCATION[LOCATION.index(RECV_INDEX.value+1)-2]][LOCATION[LOCATION.index(RECV_INDEX.value+1)-3]] != None and FLOW_DATA[LOCATION[LOCATION.index(RECV_INDEX.value+1)-3]][LOCATION[LOCATION.index(RECV_INDEX.value+1)-2]] != None:
                        FLOW_DATA[LOCATION[LOCATION.index(RECV_INDEX.value+1)-2]][LOCATION[LOCATION.index(RECV_INDEX.value+1)-3]],FLOW_DATA[LOCATION[LOCATION.index(RECV_INDEX.value+1)-3]][LOCATION[LOCATION.index(RECV_INDEX.value+1)-2]] = None,None
                
                ProcessingQue.put('RECV_MAP')

        SORTED_INDEX = sorted(LOCATION)
        Axis_data[SORTED_INDEX.index(RECV_INDEX.value+1)].plot(RT_data[RECV_INDEX.value],clear=True,pen=COLOR_SET[RECV_INDEX.value])
        Axis_data[SORTED_INDEX.index(RECV_INDEX.value+1)].setXRange(RT_INDEX[RECV_INDEX.value][-1],RT_INDEX[RECV_INDEX.value][-1]+4000)

    def LOLA_READ(self): #LONGITUDE LATITUDE SHOW LOG
        global GPS
        self.textBrowser.append('%s - %s'%(self.comboBox_2.currentText(),str(GPS[int(self.comboBox_2.currentText()[-1])-1])))

    def _TEDE_OPEN(self):
        global TEDE_INDEX
        TEDE_INDEX = int(self.tp.TEDE.comboBox.currentText()[-1])-1
        self.tp.show()

    def Setting_L(self):
        global LOCATION,Axis_data,broker
        topic = "Core/test12343Demension/data"
        TEMP = []
        for i in range(len(LOCATION)):
            TEMP.append(self.COMBO_[i].currentIndex()+1)
        if len(set(TEMP)) != len(LOCATION):
            self.MessageBox.setText('위치를 다르게 설정해주세요.')
            self.MessageBox.setWindowTitle('Alert')
            self.MessageBox.setStyleSheet("background-color: rgba(16,30,41,240);color: rgb(255, 255, 255)")
            self.MessageBox.exec_()
        else:
            for i in range(len(LOCATION)):
                LOCATION[i] = self.COMBO_[i].currentIndex()+1
            
            for i in range(len(LOCATION)):
                self.verticalLayout_13.removeWidget(Axis_data[i])
                self.tp.TEDE.comboBox.removeItem(0)
                self.comboBox_2.removeItem(0)
                Axis_data[i] = pg.PlotWidget(title="STATION %s"%str(sorted(LOCATION)[i]))
                Axis_data[i].showGrid(x=True,y=True)
                self.verticalLayout_13.addWidget(Axis_data[i])
                self.tp.TEDE.comboBox.addItem("STATION %s"%str(sorted(LOCATION)[i]))
                self.comboBox_2.addItem("STATION %s"%str(sorted(LOCATION)[i]))
            
            publish.single(topic,b'LOCATION,'+bytes(str(LOCATION)[1:-1],'utf-8'),hostname=broker)
            self.textBrowser.append('%s : LOCATION SETTING DONE %s'%(ctime(),str(LOCATION)))
            self.L.close()

    def DISTANCE_CHECK(self):
        global ProcessingQue
        ProcessingQue.put('DISTANCE')
    
    def READ_Map(self):
        global GPS,ProcessingQue

        self.Map_.show()

    @Slot(str)
    def CLEAR_TEXT(self,Dt):
        self.textBrowser.clear()

if __name__ == "__main__":

    freeze_support()

    broker = "test.mosquitto.org"
    
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
    RTS_TEMP = manager.Value('f',0.0)
    RTS_DEPTH = manager.Value('f',0.0)

    Axis_data = []
    ORDER_STRING = {4080 : '8 ORDER', 16368 : '10 ORDER', 65520 : '12 ORDER'}
    LOCATION = manager.list([]) #위치 설정
    DISTANCE = [[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)]]
    DSPEN = manager.list(['Wait' for i in range(5)])
    TRXPSEN = manager.list(['Wait' for i in range(5)])
    TRXCSEN = manager.list(['Wait' for i in range(5)])
    MNTIN = manager.list(['Wait' for i in range(5)])
    DC12VMNT = manager.list(['Wait' for i in range(5)])
    BOARD_TEMP = manager.list(['Wait' for i in range(5)])
    GPS = manager.list([[0,0] for i in range(5)])
    RT_data = [[],[],[],[],[]] #데이터
    DATA_TEMP = [[0],[0],[0],[0],[0]]
    DATA_DEPTH = [[0],[0],[0],[0],[0]]
    DATA_TIME = [[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()],[datetime.now()]]
    DSP_TEMP = manager.list(['Wait' for i in range(5)])
    RT_INDEX = [[],[],[],[],[]]
    FLOW_DATA =[[None for i in range(5)],[None for i in range(5)],[None for i in range(5)],[None for i in range(5)],[None for i in range(5)]]
    COLOR_SET = [pg.mkPen(color=(0,255,0),width=1),pg.mkPen(color=(255,0,0),width=1),pg.mkPen(color=(0,0,255),width=1),pg.mkPen(color=(255,255,0),width=1),pg.mkPen(color=(0,255,255),width=1)]

    try:
        p1 = Process(target=Multi_Calc,args=(LOCATION,MultiProc_Que,ProcessingQue,SET_INDEX,RECV_INDEX,DSPEN,TRXPSEN,TRXCSEN,MNTIN,DC12VMNT,BOARD_TEMP,RTS_TEMP,RTS_DEPTH,DSP_TEMP),daemon=True)
        p2 = Process(target=Multi_GPS,args=(ProcessingQue,GPS,),daemon=True)

        p1.start()
        p2.start()

        app = QApplication(sys.argv)

        mainwindow = WindowClass()
        Setting = QDialog_Setting()

        Setting.show()

        app_return = app.exec_()

        mainwindow._Worker.terminate()
        mainwindow._ProcessFunc.terminate()
        mainwindow.VERSION_UPDATE.terminate()
        mainwindow._TEDE_UPDATE.terminate()
        mainwindow._QTimeSet.terminate()
        mainwindow._QDTREAD.terminate()
        mainwindow.tp.READ_DT.terminate()
        mainwindow.Map_.Map_Update.terminate()
        p1.terminate()
        p2.terminate()
        sys.exit(app_return)
        
    except Exception as e:
        print(e)
        print("3")
