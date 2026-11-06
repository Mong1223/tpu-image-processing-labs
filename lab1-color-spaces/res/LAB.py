import PyQt5.QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
import cv2
import yuv_lib as yuv
import hsl_lib as hsl



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 882)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLoadImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadImage.setGeometry(QtCore.QRect(60, 30, 111, 31))
        self.btnLoadImage.setObjectName("btnLoadImage")
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(190, 30, 161, 20))
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton1.setChecked(True)
        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(QtCore.QRect(190, 50, 161, 20))
        self.radioButton2.setObjectName("radioButton2")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(350, 30, 111, 31))
        self.btnStart.setObjectName("btnStart")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(60, 120, 821, 711))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 709))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(540, 20, 160, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.labelhor = QtWidgets.QLabel(self.centralwidget)
        self.labelhor.setGeometry(QtCore.QRect(1000, 20, 55, 16))
        self.labelhor.setObjectName("labelhor")


        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(540, 40, 160, 16))
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")

        self.labelhor2 = QtWidgets.QLabel(self.centralwidget)
        self.labelhor2.setGeometry(QtCore.QRect(1000, 40, 55, 16))
        self.labelhor2.setObjectName("labelhor")
        self.horizontalScrollBar_3 = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar_3.setGeometry(QtCore.QRect(540, 60, 160, 16))
        self.horizontalScrollBar_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_3.setObjectName("horizontalScrollBar_3")
        self.labelhor3 = QtWidgets.QLabel(self.centralwidget)
        self.labelhor3.setGeometry(QtCore.QRect(1000, 60, 55, 16))
        self.labelhor3.setObjectName("labelhor")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 20, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 40, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 60, 55, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLoadImage.setText(_translate("MainWindow", "Load image"))
        self.btnLoadImage.clicked.connect(self.on_load)
        self.radioButton1.setText(_translate("MainWindow", "RGB --> HSL --> RGB"))
        self.radioButton2.setText(_translate("MainWindow", "RGB --> YUV --> RGB"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnStart.clicked.connect(self.start_click)
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.labelhor.setText(_translate("MainWindow", "TextLabel"))
        self.labelhor2.setText(_translate("MainWindow", "TextLabel"))
        self.labelhor3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "DO"))
        self.pushButton.clicked.connect(self.mydef)

    def mydef(self):
        # print(self.horizontalScrollBar.value())
        self.labelhor.setText(str(self.horizontalScrollBar.value()))
        self.labelhor2.setText(str(self.horizontalScrollBar_2.value()))
        self.labelhor3.setText(str(self.horizontalScrollBar_3.value()))

        val1 = self.horizontalScrollBar.value()
        val2 = self.horizontalScrollBar_2.value()
        val3 = self.horizontalScrollBar_3.value()
        if self.radioButton2.isChecked():
            self.Y_new = yuv.YUV_sumq(self.Y, val1)
            self.U_new = yuv.YUV_sumq(self.U, val2)
            self.V_new = yuv.YUV_sumq(self.V, val3)

            Y_image, U_image, V_image = yuv.getYUVsep(self.Y_new, self.U_new, self.V_new)

            yuv_to_rgb_image = yuv.YUV2RGB(self.Y_new, self.U_new, self.V_new)

            pix_Y = self.cv2pixmap(Y_image)
            pix_U = self.cv2pixmap(U_image)
            pix_V = self.cv2pixmap(V_image)
            pix_yuv2rgb = self.cv2pixmap(yuv_to_rgb_image)
            pic = [pix_Y, pix_U, pix_V, pix_yuv2rgb]
            names = ['Y_new', 'U_new', 'V_new', 'YUV to RGB new']
            self.pix_label_list = []
            self.pix_label_names = []

            for i in range(len(pic)):
                label_pic = QtWidgets.QLabel()
                label_pic.setPixmap(pic[i])
                self.pix_label_list.append(label_pic)
                label_name = QtWidgets.QLabel()
                label_name.setText(names[i])
                self.pix_label_names.append(label_name)
                self.formLayout.addRow(self.pix_label_list[i], self.pix_label_names[i])
        if self.radioButton1.isChecked():
            self.H_new = hsl.HSL_sumH(self.h, val1)
            self.S_new = hsl.HSL_sumq(self.s, val3/100)
            self.L_new = hsl.HSL_sumq(self.l, val2/100)
            H_image, L_image, S_image = hsl.getHSLpic(self.H_new,  self.L_new, self.S_new)
            hsl_to_rgb_image = cv2.merge([self.H_new,self.L_new, self.S_new])
            hsl_to_rgb_image = hsl.hsl_rgb(hsl_to_rgb_image)
            hsl_to_rgb_image = np.array(hsl_to_rgb_image).astype(np.uint8)
            pix_H = self.cv2pixmap(H_image)
            pix_S = self.cv2pixmap(S_image)
            pix_L = self.cv2pixmap(L_image)
            pix_hsl2rgb = self.cv2pixmap(hsl_to_rgb_image)
            pic = [pix_H, pix_S, pix_L, pix_hsl2rgb]
            names = ['H_new', 'S_new', 'L_new', 'HSL to RGB new']
            self.pix_label_list = []
            self.pix_label_names = []

            for i in range(len(pic)):
                label_pic = QtWidgets.QLabel()
                label_pic.setPixmap(pic[i])
                self.pix_label_list.append(label_pic)
                label_name = QtWidgets.QLabel()
                label_name.setText(names[i])
                self.pix_label_names.append(label_name)
                self.formLayout.addRow(self.pix_label_list[i], self.pix_label_names[i])
    def on_load(self):
        image = QFileDialog.getOpenFileName(None, 'OpenFile', 'C:\\data\\images', "All (*.*);;Image(*.jpg);;png(*.png)")
        imagePath = image[0]
        self.image_name = imagePath.replace('/', '\\')
        pixmap = QPixmap(imagePath)
        img_name = QtWidgets.QLabel()
        img_name.setText('Original Image')
        self.imgLabel = QtWidgets.QLabel()
        self.imgLabel.setPixmap(pixmap)
        self.formLayout = PyQt5.QtWidgets.QFormLayout()
        self.groupBox = PyQt5.QtWidgets.QGroupBox()
        self.formLayout.addRow(self.imgLabel, img_name)
        self.groupBox.setLayout(self.formLayout)
        self.scrollArea.setWidget(self.groupBox)
        self.scrollArea.setWidgetResizable(True)

    def cv2pixmap(self, image):
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(qImg)
        return pixmap

    def start_click(self):

        orgnl_image = cv2.imread(self.image_name)
        orgnl_image = cv2.cvtColor(orgnl_image, cv2.COLOR_BGR2RGB)
        while self.formLayout.rowCount() != 1:
            self.formLayout.removeRow(1)
        # rgb2yuv
        if self.radioButton2.isChecked():
            self.label.setText('Y')
            self.horizontalScrollBar.setMaximum(255)
            self.horizontalScrollBar.setMinimum(-255)
            self.horizontalScrollBar.setValue(0)
            self.label_2.setText('U')
            self.horizontalScrollBar_2.setMaximum(255)
            self.horizontalScrollBar_2.setMinimum(-255)
            self.horizontalScrollBar_2.setValue(0)
            self.label_3.setText('V')
            self.horizontalScrollBar_3.setMaximum(255)
            self.horizontalScrollBar_3.setMinimum(-255)
            self.horizontalScrollBar_3.setValue(0)


            # print(self.horizontalScrollBar.value())


            self.formLayout.update()
            self.Y, self.U, self.V = yuv.RGB2YUV(orgnl_image)
            # print('max', np.max(self.U))
            Y_image, U_image, V_image = yuv.getYUVsep(self.Y,self.U,self.V)

            yuv_to_rgb_image = yuv.YUV2RGB(self.Y,self.U,self.V)


            pix_Y = self.cv2pixmap(Y_image)
            pix_U = self.cv2pixmap(U_image)
            pix_V = self.cv2pixmap(V_image)
            pix_yuv2rgb = self.cv2pixmap(yuv_to_rgb_image)
            pic = [pix_Y, pix_U, pix_V, pix_yuv2rgb]
            names = ['Y', 'U', 'V', 'YUV to RGB']
            self.pix_label_list = []
            self.pix_label_names = []

            for i in range(len(pic)):

                label_pic = QtWidgets.QLabel()
                label_pic.setPixmap(pic[i])
                self.pix_label_list.append(label_pic)
                label_name = QtWidgets.QLabel()
                label_name.setText(names[i])
                self.pix_label_names.append(label_name)
                self.formLayout.addRow(self.pix_label_list[i], self.pix_label_names[i])

        if self.radioButton1.isChecked():

            self.label.setText('H')
            self.horizontalScrollBar.setMaximum(360)
            self.horizontalScrollBar.setMinimum(-360)
            self.horizontalScrollBar.setValue(0)
            self.label_2.setText('L')
            self.horizontalScrollBar_2.setMaximum(100)
            self.horizontalScrollBar_2.setMinimum(-100)
            self.horizontalScrollBar_2.setValue(0)
            self.label_3.setText('S')
            self.horizontalScrollBar_3.setMaximum(100)
            self.horizontalScrollBar_3.setMinimum(-100)
            self.horizontalScrollBar_3.setValue(0)


            self.formLayout.update()
            image_hsl = np.array(hsl.rgb_hsl(orgnl_image))
            self.h2, self.l, self.s, self.h = cv2.split(image_hsl)
            h_pic, l_pic, s_pic = hsl.getHSLpic(self.h, self.l, self.s)

            image_to_rgb = cv2.merge([self.h, self.l, self.s])
            image_hsl_rgb = np.array(hsl.hsl_rgb(image_to_rgb)).astype(np.uint8)
            pix_h = self.cv2pixmap(h_pic)
            pix_s = self.cv2pixmap(s_pic)
            pix_l = self.cv2pixmap(l_pic)

            pix_yuv2rgb = self.cv2pixmap(image_hsl_rgb)

            pic = [pix_h, pix_s, pix_l, pix_yuv2rgb]
            names = ['h', 's', 'l', 'HSL to RGB']
            self.pix_label_list = []
            self.pix_label_names = []

            for i in range(len(pic)):
                label_pic = QtWidgets.QLabel()
                label_pic.setPixmap(pic[i])
                self.pix_label_list.append(label_pic)
                label_name = QtWidgets.QLabel()
                label_name.setText(names[i])
                self.pix_label_names.append(label_name)
                self.formLayout.addRow(self.pix_label_list[i], self.pix_label_names[i])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
