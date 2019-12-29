import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl, QThread
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
from lib.YouViewerLayout import Ui_MainWindow
import re
import datetime
import pytube
from PyQt5.QtMultimedia import QSound
from lib.AuthDialog import AuthDialog

#form_class = uic.loadUiType("/Users/dkkim/Documents/section6/ui/you_viewer_v1.0.ui")[0]

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAuthLock()
        self.initSignal()

        self.user_id = 'test'
        self.user_pw = None

        self.is_play = False

        self.youtb = None
        self.youtb_fsize = 0



    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')



    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

    #기본 UI 활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증 완료')

    def showStatusMsg(self,msg) :
        self.statusbar.showMessage(msg)

    #시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
        self.previewButton.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.webView.loadProgress.connect(self.showProgressBrowserLoading)
        self.fileNavButton.clicked.connect(self.selectDownPath)
        self.calendarWidget.clicked.connect(self.append_date)
        self.startButton.clicked.connect(self.downloadYoutb)

    @pyqtSlot()
    def authCheck(self):
    #    dlg = AuthDialog()
    #    dlg.exec_()
    #    self.user_id = dlg.user_id
    #    self.user_pw = dlg.user_pw

        #print("id: %s password: %s" %(self.user_id,self.user_pw))

         # 이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        # 유저 정보 및 사용 유효기간을 체크하는 코드를 넣어주세요.
        # code
        # code
        #print("id: %s password: %s" %(self.user_id,self.user_pw))

        if True:
            self.initAuthActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
            self.append_log_msg("login Success")

        else:
            QMessageBox.about(self, "인증오류", "아이디 또는 비밀번호 인증 오류")

    def load_url(self):
        url = self.urlTextEdit.text().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webView.load(QUrl('about:blank'))
            self.previewButton.setText("재생")
            self.is_play = False
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus(True)
            self.startButton.setEnabled(True)
            self.streamCombobox.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg("인증완료")


        else:
            if v.match(url) is not None:
                self.append_log_msg('Play CLick')
                self.webView.load(QUrl(url))
                self.showStatusMsg(url + "재생중")
                self.previewButton.setText("중지")
                self.is_play = True
                self.startButton.setEnabled(True)
                self.initalYouWork(url)

            else:
                QMessageBox.about(self,"URL형식오류","Youtube 주소 형식이 아님")
                self.urlTextEdit.clear()
                self.urlTextEdit.setFocus(True)

    def initalYouWork(self,url):
        video_list = pytube.YouTube(url)

        self.youtb = video_list.streams.all()
        self.streamCombobox.clear()
        for q in self.youtb:
            #print(q.itag,q.mime_type,q.abr)
            tmp_list, str_list= [], []
            tmp_list.append(str(q.mime_type or ''))
            tmp_list.append(str(q.res or ''))
            tmp_list.append(str(q.fps or ''))
            tmp_list.append(str(q.abr or ''))

            #print(tmp_list)
            str_list = [x for x in tmp_list if x!= '']
            print('step3',str_list)

            self.streamCombobox.addItem(','.join(str_list))

    def append_log_msg(self,act) :
        now  = datetime.datetime.now()
        nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
        app_msg = self.user_id + " : " + act + '- (' + nowDatetime + ')'
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg)

        #활동로그 저장
        with open('/Users/dkkim/Documents/section6/log/log.txt','a') as f:
            f.write(app_msg+'\n')

    @pyqtSlot(int)
    def showProgressBrowserLoading(self, v):
        self.progressBar.setValue(v)

    @pyqtSlot()
    def selectDownPath(self):
        #파일선택
        #fname = QFileDialog.getOpenFileName(self)
        #self.pathTextEdit.setText(fname[0])


        #경로선택
        fPath = QFileDialog.getExistingDirectory(self,'Select Directory')
        self.pathTextEdit.setText(fPath)

    @pyqtSlot()
    def append_date(self) :
        cur_date = self.calendarWidget.selectedDate()
        #print('Click Date',self.calendarWidget.selectedDate().toString())
        print(str(cur_date.year())+"-"+str(cur_date.month())+'-'+str(cur_date.day()))
        self.append_log_msg('Calendar Click')

    @pyqtSlot()
    def downloadYoutb(self):
        down_dir = self.pathTextEdit.text().strip()
        if down_dir is None or down_dir == ''or not down_dir:
            QMessageBox.about(self,'경로선택','다운로드 받을 경로를 선택하세요')
            self.pathTextEdit.setFocus(True)
            return None

            self.youtb_fsize = self.youtb[self.streamCombobox.currentIndex()].filesize
            print('fsize',self.youtb_fsize)
            self.youtb[self.streamCombobox.currentIndex()].download(down_dir)
            self.append_log_msg('Download Click')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
