from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from numpy import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pandas as pd
from plotnine import ggplot, geom_point, aes, geom_line, theme, xlab, ylab

class Ui_MainWindow(object):
        
    def canvas_plot(self):
        dpi = 30
        size_inches = (11, 8)                                       
        size_px = int(size_inches[0]*dpi), int(size_inches[1]*dpi)  
        self.figure.clear()
        n = 10
        x = np.linspace(0, 2 * np.pi, n)
        df = pd.DataFrame({
            'x': x,
            'y1': np.random.rand(n),
            'y2': np.sin(x),
            'y3': np.cos(x) * np.sin(x)
        })
        y = 'y1'

        # specify the plot and get the figure object
        ff = (ggplot(df, aes('x', y))
              + geom_line()
              + theme(figure_size=size_inches,dpi=dpi)
              + xlab('time(s)')
              + ylab('altitude(m)')
             )
        
        fig = ff.draw()

        # update to the new figure
        self.canvas.figure = fig

        # close the figure so that we don't create too many figure instances
        plt.close(fig)
        self.canvas.draw()
        
        
        
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 480)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CENTRAL_WIDGET = QtWidgets.QWidget(MainWindow)
        self.CENTRAL_WIDGET.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CENTRAL_WIDGET.setObjectName("CENTRAL_WIDGET")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CENTRAL_WIDGET)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FRAME_1 = QtWidgets.QFrame(self.CENTRAL_WIDGET)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FRAME_1.sizePolicy().hasHeightForWidth())
        self.FRAME_1.setSizePolicy(sizePolicy)
        self.FRAME_1.setMinimumSize(QtCore.QSize(0, 0))
        self.FRAME_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FRAME_1.setSizeIncrement(QtCore.QSize(0, 0))
        self.FRAME_1.setStyleSheet("background-color: rgb(255 , 255, 255);")
        self.FRAME_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRAME_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_1.setObjectName("FRAME_1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.FRAME_1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.FRAME_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(150, 60))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("kc-logo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.FRAME_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("cansat.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.FRAME_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(150, 60))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("team_logo.jpeg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_10 = QtWidgets.QLabel(self.FRAME_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(111)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("font: 18pt \"Bahnschrift SemiLight SemiConde\";\n"
"font: 57 16pt \"Yu Gothic Medium\";\n"
"")
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_30 = QtWidgets.QLabel(self.FRAME_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMaximumSize(QtCore.QSize(50, 40))
        self.label_30.setSizeIncrement(QtCore.QSize(500, 500))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("../../Downloads/WhatsApp Image 2022-09-14 at 6.34.16 PM.jpeg"))
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setWordWrap(True)
        self.label_30.setOpenExternalLinks(True)
        self.label_30.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_4.addWidget(self.label_30)
        self.label_12 = QtWidgets.QLabel(self.FRAME_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(100, 40))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("college.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(self.FRAME_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(90, 60))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("indian_flag.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.verticalLayout.addWidget(self.FRAME_1)
        self.FRAME_2 = QtWidgets.QFrame(self.CENTRAL_WIDGET)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FRAME_2.sizePolicy().hasHeightForWidth())
        self.FRAME_2.setSizePolicy(sizePolicy)
        self.FRAME_2.setMinimumSize(QtCore.QSize(0, 0))
        self.FRAME_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FRAME_2.setBaseSize(QtCore.QSize(0, 200))
        self.FRAME_2.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border:none")
        self.FRAME_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FRAME_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FRAME_2.setObjectName("FRAME_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.FRAME_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.FRAME_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("border: None;\n"
"border-style: outset;\n"
"background-color: rgb(220, 220, 220);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setStyleSheet("border:none")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 5px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setStyleSheet("border:none")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    font: 6pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(10, 10, 10);\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    border-radius: 1px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 2px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_18.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    font: 6pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(10, 10, 10);\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    border-radius: 1px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 2px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_18.addWidget(self.pushButton_7)
        self.horizontalLayout_2.addWidget(self.frame_9)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setStyleSheet("border:none")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 5px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setStyleSheet("border:none")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    font: 6pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(10, 10, 10);\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    border-radius: 1px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 2px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_19.addWidget(self.pushButton_8)
        self.horizontalLayout_2.addWidget(self.frame_12)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.FRAME_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QtCore.QSize(12333333, 16777215))
        self.frame_6.setStyleSheet("border: None;\n"
"border-style: outset;\n"
"background-color: rgb(220, 220, 220);\n"
"padding:0")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_51 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("font: 8pt \"Arial\";\n"
"border:None")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_6.addWidget(self.label_51)
        self.frame_20 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setStyleSheet("background-color: None;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_31 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 0, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 0, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 0, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 5px;")
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 1, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 5px;")
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 1, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 5px;")
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 1, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_20)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.FRAME_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("border: None;\n"
"border-style: outset;\n"
"background-color: rgb(220, 220, 220);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font: 8pt \"Arial\";\n"
"border:None")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.widget_6 = QtWidgets.QWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.SOFTWARE_STATE_A_TEXT = QtWidgets.QLabel(self.widget_6)
        self.SOFTWARE_STATE_A_TEXT.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.SOFTWARE_STATE_A_TEXT.setObjectName("SOFTWARE_STATE_A_TEXT")
        self.gridLayout_5.addWidget(self.SOFTWARE_STATE_A_TEXT, 0, 0, 1, 1)
        self.SOFTWARE_STATE_A_TEXT_7 = QtWidgets.QLabel(self.widget_6)
        self.SOFTWARE_STATE_A_TEXT_7.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.SOFTWARE_STATE_A_TEXT_7.setObjectName("SOFTWARE_STATE_A_TEXT_7")
        self.gridLayout_5.addWidget(self.SOFTWARE_STATE_A_TEXT_7, 2, 0, 1, 1)
        self.SOFTWARE_STATE_A_TEXT_4 = QtWidgets.QLabel(self.widget_6)
        self.SOFTWARE_STATE_A_TEXT_4.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.SOFTWARE_STATE_A_TEXT_4.setObjectName("SOFTWARE_STATE_A_TEXT_4")
        self.gridLayout_5.addWidget(self.SOFTWARE_STATE_A_TEXT_4, 0, 1, 1, 1)
        self.SOFTWARE_STATE_A_TEXT_6 = QtWidgets.QLabel(self.widget_6)
        self.SOFTWARE_STATE_A_TEXT_6.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.SOFTWARE_STATE_A_TEXT_6.setObjectName("SOFTWARE_STATE_A_TEXT_6")
        self.gridLayout_5.addWidget(self.SOFTWARE_STATE_A_TEXT_6, 2, 1, 1, 1)
        self.SOFTWARE_STATE_A_TEXT_2 = QtWidgets.QLabel(self.widget_6)
        self.SOFTWARE_STATE_A_TEXT_2.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.SOFTWARE_STATE_A_TEXT_2.setObjectName("SOFTWARE_STATE_A_TEXT_2")
        self.gridLayout_5.addWidget(self.SOFTWARE_STATE_A_TEXT_2, 0, 2, 1, 1)
        self.SOFTWARE_STATE_A_TEXT_3 = QtWidgets.QLabel(self.widget_6)
        self.SOFTWARE_STATE_A_TEXT_3.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.SOFTWARE_STATE_A_TEXT_3.setObjectName("SOFTWARE_STATE_A_TEXT_3")
        self.gridLayout_5.addWidget(self.SOFTWARE_STATE_A_TEXT_3, 2, 2, 1, 1)
        self.SOFTWARE_STATE_A_TEXT_5 = QtWidgets.QLabel(self.widget_6)
        self.SOFTWARE_STATE_A_TEXT_5.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(0,0,);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.SOFTWARE_STATE_A_TEXT_5.setObjectName("SOFTWARE_STATE_A_TEXT_5")
        self.gridLayout_5.addWidget(self.SOFTWARE_STATE_A_TEXT_5, 0, 3, 1, 1)
        self.verticalLayout_7.addWidget(self.widget_6)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.FRAME_2)
        self.frame_2 = QtWidgets.QFrame(self.CENTRAL_WIDGET)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FRAME_3 = QtWidgets.QTabWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.FRAME_3.sizePolicy().hasHeightForWidth())
        self.FRAME_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.FRAME_3.setFont(font)
        self.FRAME_3.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.FRAME_3.setObjectName("FRAME_3")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_13 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet("font: 6pt \"Arial Rounded MT Bold\";\n"
"background-color: rgb(220, 220, 220);\n"
"border:None")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_72 = QtWidgets.QLabel(self.frame_13)
        self.label_72.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_72.setObjectName("label_72")
        self.gridLayout_4.addWidget(self.label_72, 0, 11, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.frame_13)
        self.label_73.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_73.setObjectName("label_73")
        self.gridLayout_4.addWidget(self.label_73, 0, 6, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.frame_13)
        self.label_74.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setObjectName("label_74")
        self.gridLayout_4.addWidget(self.label_74, 2, 6, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.frame_13)
        self.label_75.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_75.setObjectName("label_75")
        self.gridLayout_4.addWidget(self.label_75, 0, 7, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.frame_13)
        self.label_76.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_76.setObjectName("label_76")
        self.gridLayout_4.addWidget(self.label_76, 0, 10, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.frame_13)
        self.label_77.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setObjectName("label_77")
        self.gridLayout_4.addWidget(self.label_77, 2, 10, 1, 1)
        self.label_84 = QtWidgets.QLabel(self.frame_13)
        self.label_84.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_84.setAlignment(QtCore.Qt.AlignCenter)
        self.label_84.setObjectName("label_84")
        self.gridLayout_4.addWidget(self.label_84, 2, 9, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.frame_13)
        self.label_85.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_85.setAlignment(QtCore.Qt.AlignCenter)
        self.label_85.setObjectName("label_85")
        self.gridLayout_4.addWidget(self.label_85, 2, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.frame_13)
        self.label_42.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_4.addWidget(self.label_42, 0, 3, 1, 1)
        self.label_86 = QtWidgets.QLabel(self.frame_13)
        self.label_86.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_86.setObjectName("label_86")
        self.gridLayout_4.addWidget(self.label_86, 0, 0, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.frame_13)
        self.label_43.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_4.addWidget(self.label_43, 0, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.frame_13)
        self.label_44.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_4.addWidget(self.label_44, 0, 4, 1, 1)
        self.label_87 = QtWidgets.QLabel(self.frame_13)
        self.label_87.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_87.setObjectName("label_87")
        self.gridLayout_4.addWidget(self.label_87, 0, 2, 1, 1)
        self.label_88 = QtWidgets.QLabel(self.frame_13)
        self.label_88.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_88.setObjectName("label_88")
        self.gridLayout_4.addWidget(self.label_88, 0, 5, 1, 1)
        self.label_89 = QtWidgets.QLabel(self.frame_13)
        self.label_89.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_89.setAlignment(QtCore.Qt.AlignCenter)
        self.label_89.setObjectName("label_89")
        self.gridLayout_4.addWidget(self.label_89, 2, 11, 1, 1)
        self.label_90 = QtWidgets.QLabel(self.frame_13)
        self.label_90.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_90.setObjectName("label_90")
        self.gridLayout_4.addWidget(self.label_90, 0, 8, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.frame_13)
        self.label_91.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_91.setAlignment(QtCore.Qt.AlignCenter)
        self.label_91.setObjectName("label_91")
        self.gridLayout_4.addWidget(self.label_91, 2, 4, 1, 1)
        self.label_92 = QtWidgets.QLabel(self.frame_13)
        self.label_92.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_92.setAlignment(QtCore.Qt.AlignCenter)
        self.label_92.setObjectName("label_92")
        self.gridLayout_4.addWidget(self.label_92, 2, 8, 1, 1)
        self.label_93 = QtWidgets.QLabel(self.frame_13)
        self.label_93.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_93.setAlignment(QtCore.Qt.AlignCenter)
        self.label_93.setObjectName("label_93")
        self.gridLayout_4.addWidget(self.label_93, 2, 7, 1, 1)
        self.label_94 = QtWidgets.QLabel(self.frame_13)
        self.label_94.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_94.setAlignment(QtCore.Qt.AlignCenter)
        self.label_94.setObjectName("label_94")
        self.gridLayout_4.addWidget(self.label_94, 2, 5, 1, 1)
        self.label_95 = QtWidgets.QLabel(self.frame_13)
        self.label_95.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_95.setAlignment(QtCore.Qt.AlignCenter)
        self.label_95.setObjectName("label_95")
        self.gridLayout_4.addWidget(self.label_95, 2, 3, 1, 1)
        self.label_96 = QtWidgets.QLabel(self.frame_13)
        self.label_96.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_96.setObjectName("label_96")
        self.gridLayout_4.addWidget(self.label_96, 0, 9, 1, 1)
        self.label_97 = QtWidgets.QLabel(self.frame_13)
        self.label_97.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_97.setAlignment(QtCore.Qt.AlignCenter)
        self.label_97.setObjectName("label_97")
        self.gridLayout_4.addWidget(self.label_97, 2, 2, 1, 1)
        self.label_98 = QtWidgets.QLabel(self.frame_13)
        self.label_98.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_98.setAlignment(QtCore.Qt.AlignCenter)
        self.label_98.setObjectName("label_98")
        self.gridLayout_4.addWidget(self.label_98, 2, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    font: 6pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(10, 10, 10);\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    border-radius: 2px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 2px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_4.addWidget(self.pushButton_11, 0, 12, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    font: 6pt \"Arial Rounded MT Bold\";\n"
"    color: rgb(10, 10, 10);\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    border-radius: 2px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 2px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_4.addWidget(self.pushButton_12, 2, 12, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet("border:None;\n"
"background-color: rgb(220, 220, 220);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setStyleSheet("border:None;\n"
"font: 6pt \"Arial Rounded MT Bold\";")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_99 = QtWidgets.QLabel(self.frame_15)
        self.label_99.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_99.setAlignment(QtCore.Qt.AlignCenter)
        self.label_99.setObjectName("label_99")
        self.gridLayout_7.addWidget(self.label_99, 1, 1, 1, 1)
        self.label_100 = QtWidgets.QLabel(self.frame_15)
        self.label_100.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100.setObjectName("label_100")
        self.gridLayout_7.addWidget(self.label_100, 0, 3, 1, 1)
        self.label_101 = QtWidgets.QLabel(self.frame_15)
        self.label_101.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_101.setAlignment(QtCore.Qt.AlignCenter)
        self.label_101.setObjectName("label_101")
        self.gridLayout_7.addWidget(self.label_101, 1, 3, 1, 1)
        self.label_102 = QtWidgets.QLabel(self.frame_15)
        self.label_102.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_102.setAlignment(QtCore.Qt.AlignCenter)
        self.label_102.setObjectName("label_102")
        self.gridLayout_7.addWidget(self.label_102, 3, 1, 1, 1)
        self.label_103 = QtWidgets.QLabel(self.frame_15)
        self.label_103.setAlignment(QtCore.Qt.AlignCenter)
        self.label_103.setObjectName("label_103")
        self.gridLayout_7.addWidget(self.label_103, 0, 2, 1, 1)
        self.label_104 = QtWidgets.QLabel(self.frame_15)
        self.label_104.setAlignment(QtCore.Qt.AlignCenter)
        self.label_104.setObjectName("label_104")
        self.gridLayout_7.addWidget(self.label_104, 0, 1, 1, 1)
        self.label_105 = QtWidgets.QLabel(self.frame_15)
        self.label_105.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_105.setAlignment(QtCore.Qt.AlignCenter)
        self.label_105.setObjectName("label_105")
        self.gridLayout_7.addWidget(self.label_105, 1, 2, 1, 1)
        self.label_106 = QtWidgets.QLabel(self.frame_15)
        self.label_106.setAlignment(QtCore.Qt.AlignCenter)
        self.label_106.setObjectName("label_106")
        self.gridLayout_7.addWidget(self.label_106, 2, 0, 1, 1)
        self.label_107 = QtWidgets.QLabel(self.frame_15)
        self.label_107.setAlignment(QtCore.Qt.AlignCenter)
        self.label_107.setObjectName("label_107")
        self.gridLayout_7.addWidget(self.label_107, 1, 0, 1, 1)
        self.label_108 = QtWidgets.QLabel(self.frame_15)
        self.label_108.setAlignment(QtCore.Qt.AlignCenter)
        self.label_108.setObjectName("label_108")
        self.gridLayout_7.addWidget(self.label_108, 3, 0, 1, 1)
        self.label_109 = QtWidgets.QLabel(self.frame_15)
        self.label_109.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_109.setAlignment(QtCore.Qt.AlignCenter)
        self.label_109.setObjectName("label_109")
        self.gridLayout_7.addWidget(self.label_109, 3, 2, 1, 1)
        self.label_110 = QtWidgets.QLabel(self.frame_15)
        self.label_110.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_110.setAlignment(QtCore.Qt.AlignCenter)
        self.label_110.setObjectName("label_110")
        self.gridLayout_7.addWidget(self.label_110, 3, 3, 1, 1)
        self.label_111 = QtWidgets.QLabel(self.frame_15)
        self.label_111.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_111.setAlignment(QtCore.Qt.AlignCenter)
        self.label_111.setObjectName("label_111")
        self.gridLayout_7.addWidget(self.label_111, 2, 2, 1, 1)
        self.label_112 = QtWidgets.QLabel(self.frame_15)
        self.label_112.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_112.setAlignment(QtCore.Qt.AlignCenter)
        self.label_112.setObjectName("label_112")
        self.gridLayout_7.addWidget(self.label_112, 2, 1, 1, 1)
        self.label_113 = QtWidgets.QLabel(self.frame_15)
        self.label_113.setStyleSheet("background-color: rgb(50,50,50);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 130, 80);\n"
"border-style: outset;\n"
"border-radius: 2px;")
        self.label_113.setAlignment(QtCore.Qt.AlignCenter)
        self.label_113.setObjectName("label_113")
        self.gridLayout_7.addWidget(self.label_113, 2, 3, 1, 1)
        self.horizontalLayout_9.addWidget(self.frame_15)
        self.widget_4 = QtWidgets.QWidget(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet("border:None")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_114 = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy)
        self.label_114.setStyleSheet("font: 6pt \"Arial Rounded MT Bold\";\n"
"border:None")
        self.label_114.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_114.setObjectName("label_114")
        self.verticalLayout_15.addWidget(self.label_114)
        self.progressBar_2 = QtWidgets.QProgressBar(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_2.setStyleSheet("border: 0.5px solid rgb(0,0,0);")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_15.addWidget(self.progressBar_2)
        self.horizontalLayout_9.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.TEMP_GRAPH = QtWidgets.QFrame(self.widget_5)
        self.TEMP_GRAPH.setStyleSheet("border:None")
        self.TEMP_GRAPH.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TEMP_GRAPH.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TEMP_GRAPH.setObjectName("TEMP_GRAPH")
        
        #Create a horizontal layout
        #HL for horizontal layout
        self.HL_TG = QtWidgets.QHBoxLayout(self.TEMP_GRAPH)
        self.HL_TG.setObjectName("HL_TG")
        #Canvas here
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        #end of canvas
        #Add canvas
        self.HL_TG.addWidget(self.canvas)
        #End of horizontal layout
        #Plotting the container telementry temperature graph
        self.canvas_plot()  
        
        self.horizontalLayout_7.addWidget(self.TEMP_GRAPH)
        self.ALTI_GRAPH = QtWidgets.QFrame(self.widget_5)
        self.ALTI_GRAPH.setStyleSheet("border:None")
        self.ALTI_GRAPH.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ALTI_GRAPH.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ALTI_GRAPH.setObjectName("ALTI_GRAPH")
        
        #Create a horizontal layout
        #HL for horizontal layout
        self.HL_AG = QtWidgets.QHBoxLayout(self.ALTI_GRAPH)
        self.HL_AG.setObjectName("HL_AG")
        #Canvas here
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        #end of canvas
        #Add canvas
        self.HL_AG.addWidget(self.canvas)
        #End of horizontal layout
        #Plotting the container telementry temperature graph
        self.canvas_plot()  
        
        
        self.horizontalLayout_7.addWidget(self.ALTI_GRAPH)
        self.horizontalLayout_9.addWidget(self.widget_5)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.FRAME_3.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.FRAME_3.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.conteiner_telementry_2 = QtWidgets.QGroupBox(self.tab_3)
        self.conteiner_telementry_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.conteiner_telementry_2.setFont(font)
        self.conteiner_telementry_2.setStyleSheet("font: 63 6pt \"Yu Gothic UI Semibold\";\n"
"font: 6pt \"Segoe UI Variable Text Semibold\";\n"
"background-color: rgb(200, 200, 200);\n"
"border-style: outset;\n"
"border: 0.5px solid rgb(24, 24, 24);\n"
"color: rgb(0,0,0)")
        self.conteiner_telementry_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.conteiner_telementry_2.setObjectName("conteiner_telementry_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.conteiner_telementry_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.CTC_TABLE = QtWidgets.QTableWidget(self.conteiner_telementry_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.CTC_TABLE.sizePolicy().hasHeightForWidth())
        self.CTC_TABLE.setSizePolicy(sizePolicy)
        self.CTC_TABLE.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"border:None;\n"
"background-color: rgb(190, 190, 190);\n"
"alternate-background-color: rgb(164,164, 164);")
        self.CTC_TABLE.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.CTC_TABLE.setAlternatingRowColors(True)
        self.CTC_TABLE.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.CTC_TABLE.setShowGrid(False)
        self.CTC_TABLE.setGridStyle(QtCore.Qt.NoPen)
        self.CTC_TABLE.setWordWrap(False)
        self.CTC_TABLE.setRowCount(5)
        self.CTC_TABLE.setObjectName("CTC_TABLE")
        self.CTC_TABLE.setColumnCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CTC_TABLE.setItem(1, 0, item)
        self.CTC_TABLE.horizontalHeader().setDefaultSectionSize(56)
        self.CTC_TABLE.horizontalHeader().setHighlightSections(True)
        self.CTC_TABLE.horizontalHeader().setMinimumSectionSize(16)
        self.CTC_TABLE.verticalHeader().setVisible(False)
        self.CTC_TABLE.verticalHeader().setDefaultSectionSize(10)
        self.verticalLayout_9.addWidget(self.CTC_TABLE)
        self.CTC_SAVECSV_BUTTON = QtWidgets.QPushButton(self.conteiner_telementry_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CTC_SAVECSV_BUTTON.sizePolicy().hasHeightForWidth())
        self.CTC_SAVECSV_BUTTON.setSizePolicy(sizePolicy)
        self.CTC_SAVECSV_BUTTON.setStyleSheet("QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    border-radius:5px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #000000, stop: 1 #008000\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    color:rgb(0,0,0);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    color:\n"
"    }")
        self.CTC_SAVECSV_BUTTON.setObjectName("CTC_SAVECSV_BUTTON")
        self.verticalLayout_9.addWidget(self.CTC_SAVECSV_BUTTON)
        self.verticalLayout_8.addWidget(self.conteiner_telementry_2)
        self.conteiner_telementry_3 = QtWidgets.QGroupBox(self.tab_3)
        self.conteiner_telementry_3.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.conteiner_telementry_3.setFont(font)
        self.conteiner_telementry_3.setStyleSheet("font: 63 6pt \"Yu Gothic UI Semibold\";\n"
"font: 6pt \"Segoe UI Variable Text Semibold\";\n"
"background-color: rgb(200, 200, 200);\n"
"border-style: outset;\n"
"border: 0.5px solid rgb(24, 24, 24);\n"
"color: rgb(0,0,0)")
        self.conteiner_telementry_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.conteiner_telementry_3.setObjectName("conteiner_telementry_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.conteiner_telementry_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.PTC_TABLE = QtWidgets.QTableWidget(self.conteiner_telementry_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.PTC_TABLE.sizePolicy().hasHeightForWidth())
        self.PTC_TABLE.setSizePolicy(sizePolicy)
        self.PTC_TABLE.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 6pt \"Arial Rounded MT Bold\";\n"
"border:None;\n"
"background-color: rgb(190, 190, 190);\n"
"alternate-background-color: rgb(164,164, 164);")
        self.PTC_TABLE.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PTC_TABLE.setLineWidth(1)
        self.PTC_TABLE.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.PTC_TABLE.setAlternatingRowColors(True)
        self.PTC_TABLE.setTextElideMode(QtCore.Qt.ElideNone)
        self.PTC_TABLE.setShowGrid(False)
        self.PTC_TABLE.setGridStyle(QtCore.Qt.NoPen)
        self.PTC_TABLE.setWordWrap(False)
        self.PTC_TABLE.setRowCount(5)
        self.PTC_TABLE.setObjectName("PTC_TABLE")
        self.PTC_TABLE.setColumnCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PTC_TABLE.setItem(1, 0, item)
        self.PTC_TABLE.horizontalHeader().setDefaultSectionSize(56)
        self.PTC_TABLE.horizontalHeader().setHighlightSections(True)
        self.PTC_TABLE.horizontalHeader().setMinimumSectionSize(16)
        self.PTC_TABLE.horizontalHeader().setStretchLastSection(False)
        self.PTC_TABLE.verticalHeader().setVisible(False)
        self.PTC_TABLE.verticalHeader().setDefaultSectionSize(10)
        self.PTC_TABLE.verticalHeader().setHighlightSections(False)
        self.verticalLayout_10.addWidget(self.PTC_TABLE)
        self.PTC_SAVECSV_BUTTON = QtWidgets.QPushButton(self.conteiner_telementry_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PTC_SAVECSV_BUTTON.sizePolicy().hasHeightForWidth())
        self.PTC_SAVECSV_BUTTON.setSizePolicy(sizePolicy)
        self.PTC_SAVECSV_BUTTON.setStyleSheet("QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    border-radius:5px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #000000, stop: 1 #008000\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    color:rgb(0,0,0);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    color:\n"
"    }")
        self.PTC_SAVECSV_BUTTON.setObjectName("PTC_SAVECSV_BUTTON")
        self.verticalLayout_10.addWidget(self.PTC_SAVECSV_BUTTON)
        self.verticalLayout_8.addWidget(self.conteiner_telementry_3)
        self.FRAME_3.addTab(self.tab_3, "")
        self.horizontalLayout_3.addWidget(self.FRAME_3)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.CENTRAL_WIDGET)

        self.retranslateUi(MainWindow)
        self.FRAME_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>GROUND CONTROL <span style=\" color:#ff0000;\">INTERFACE</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "PORT"))
        self.label_4.setText(_translate("MainWindow", "COM4"))
        self.pushButton_6.setText(_translate("MainWindow", "SCAN"))
        self.pushButton_7.setText(_translate("MainWindow", "STOP"))
        self.label_2.setText(_translate("MainWindow", "BAUDRATE"))
        self.label_3.setText(_translate("MainWindow", "9600"))
        self.pushButton_8.setText(_translate("MainWindow", "RUN"))
        self.label_51.setText(_translate("MainWindow", "GROUND STATION DETAILS"))
        self.label_31.setText(_translate("MainWindow", "LONGITUDE"))
        self.label_33.setText(_translate("MainWindow", "LATTITUDE"))
        self.label_35.setText(_translate("MainWindow", "MISSION TIME"))
        self.label_32.setText(_translate("MainWindow", "24.0469N"))
        self.label_36.setText(_translate("MainWindow", "16:23:23"))
        self.label_34.setText(_translate("MainWindow", "24.0469E"))
        self.label_5.setText(_translate("MainWindow", "SOFTWARE STATE"))
        self.SOFTWARE_STATE_A_TEXT.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#00ff00;\">●</span> A - BOOT</p></body></html>"))
        self.SOFTWARE_STATE_A_TEXT_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#00ff00;\">●</span> B - IDLE</p></body></html>"))
        self.SOFTWARE_STATE_A_TEXT_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#00ff00;\">●</span> C - LAUNCHED</p></body></html>"))
        self.SOFTWARE_STATE_A_TEXT_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ff0000;\">●</span> D - DESCENDING</p></body></html>"))
        self.SOFTWARE_STATE_A_TEXT_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ff0000;\">●</span> E - PARACHUTE DEPLOYED</p></body></html>"))
        self.SOFTWARE_STATE_A_TEXT_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ff0000;\">●</span> F - RELEASING PAYLOAD</p></body></html>"))
        self.SOFTWARE_STATE_A_TEXT_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ff0000;\">●</span> G - LANDED</p></body></html>"))
        self.label_72.setText(_translate("MainWindow", "CMD ECHO"))
        self.label_73.setText(_translate("MainWindow", "TP RELEASE"))
        self.label_74.setText(_translate("MainWindow", "N"))
        self.label_75.setText(_translate("MainWindow", "TEMP"))
        self.label_76.setText(_translate("MainWindow", "GPS STATS"))
        self.label_77.setText(_translate("MainWindow", "9.7"))
        self.label_84.setText(_translate("MainWindow", "77.4977"))
        self.label_85.setText(_translate("MainWindow", "F"))
        self.label_42.setText(_translate("MainWindow", "GPS LATT"))
        self.label_86.setText(_translate("MainWindow", "MODE"))
        self.label_43.setText(_translate("MainWindow", "ALTITUDE"))
        self.label_44.setText(_translate("MainWindow", "GPS ALTI"))
        self.label_87.setText(_translate("MainWindow", "VOLTAGE"))
        self.label_88.setText(_translate("MainWindow", "SOFT STATE"))
        self.label_89.setText(_translate("MainWindow", "CXON"))
        self.label_90.setText(_translate("MainWindow", "GPS TIME"))
        self.label_91.setText(_translate("MainWindow", "120.15"))
        self.label_92.setText(_translate("MainWindow", "16:05:23"))
        self.label_93.setText(_translate("MainWindow", "34.7"))
        self.label_94.setText(_translate("MainWindow", "LAUNCHED"))
        self.label_95.setText(_translate("MainWindow", "27.2046"))
        self.label_96.setText(_translate("MainWindow", "GPS LONG"))
        self.label_97.setText(_translate("MainWindow", "7.38"))
        self.label_98.setText(_translate("MainWindow", "120.3"))
        self.pushButton_11.setText(_translate("MainWindow", "START TELEMETRY"))
        self.pushButton_12.setText(_translate("MainWindow", "STOP TELEMETRY"))
        self.label_99.setText(_translate("MainWindow", "0"))
        self.label_100.setText(_translate("MainWindow", "YOW"))
        self.label_101.setText(_translate("MainWindow", "0"))
        self.label_102.setText(_translate("MainWindow", "0"))
        self.label_103.setText(_translate("MainWindow", "PITCH"))
        self.label_104.setText(_translate("MainWindow", "ROLL"))
        self.label_105.setText(_translate("MainWindow", "0"))
        self.label_106.setText(_translate("MainWindow", "ACC"))
        self.label_107.setText(_translate("MainWindow", "GYR"))
        self.label_108.setText(_translate("MainWindow", "MOG"))
        self.label_109.setText(_translate("MainWindow", "0"))
        self.label_110.setText(_translate("MainWindow", "0"))
        self.label_111.setText(_translate("MainWindow", "0"))
        self.label_112.setText(_translate("MainWindow", "0"))
        self.label_113.setText(_translate("MainWindow", "0"))
        self.label_114.setText(_translate("MainWindow", "BATTERY"))
        self.FRAME_3.setTabText(self.FRAME_3.indexOf(self.tab), _translate("MainWindow", "CANSAT TELEMETRY"))
        self.FRAME_3.setTabText(self.FRAME_3.indexOf(self.tab_2), _translate("MainWindow", "COMMAND"))
        self.conteiner_telementry_2.setTitle(_translate("MainWindow", "CONTAINER TELEMENTRY CHART"))
        self.CTC_TABLE.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.CTC_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TEAM ID"))
        item = self.CTC_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MISSION TIME"))
        item = self.CTC_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PACKET COUNT"))
        item = self.CTC_TABLE.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PACKET TYPE"))
        item = self.CTC_TABLE.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "MODE"))
        item = self.CTC_TABLE.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "TP RELEASE"))
        item = self.CTC_TABLE.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ALTITIUDE "))
        item = self.CTC_TABLE.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "TEMP"))
        item = self.CTC_TABLE.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "VOLTAGE"))
        item = self.CTC_TABLE.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "GPS TIME"))
        item = self.CTC_TABLE.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "GPS LATT"))
        item = self.CTC_TABLE.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "GPS LONG "))
        item = self.CTC_TABLE.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "GPS ALTI"))
        item = self.CTC_TABLE.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "GPS SA??"))
        item = self.CTC_TABLE.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "SOFT STATE"))
        item = self.CTC_TABLE.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "CMD ECHO"))
        __sortingEnabled = self.CTC_TABLE.isSortingEnabled()
        self.CTC_TABLE.setSortingEnabled(False)
        item = self.CTC_TABLE.item(0, 0)
        item.setText(_translate("MainWindow", "1070"))
        item = self.CTC_TABLE.item(1, 0)
        item.setText(_translate("MainWindow", "1070"))
        self.CTC_TABLE.setSortingEnabled(__sortingEnabled)
        self.CTC_SAVECSV_BUTTON.setText(_translate("MainWindow", "SAVE AS CSV"))
        self.conteiner_telementry_3.setTitle(_translate("MainWindow", "PAYLOAD TELEMENTRY CHART"))
        self.PTC_TABLE.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.PTC_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TEAM ID"))
        item = self.PTC_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MISSION TIME"))
        item = self.PTC_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PACKET COUNT"))
        item = self.PTC_TABLE.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PACKET TYPE"))
        item = self.PTC_TABLE.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "TP ALTITUDE"))
        item = self.PTC_TABLE.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "TP RELEASE"))
        item = self.PTC_TABLE.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TP TEMP"))
        item = self.PTC_TABLE.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "TP VOLT"))
        item = self.PTC_TABLE.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "GYRO P"))
        item = self.PTC_TABLE.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "GYRO Y"))
        item = self.PTC_TABLE.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "ACCEL R"))
        item = self.PTC_TABLE.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "ACCEL P"))
        item = self.PTC_TABLE.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "ACCEL Y"))
        item = self.PTC_TABLE.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "MAG R"))
        item = self.PTC_TABLE.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "MAG P"))
        item = self.PTC_TABLE.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "MAG Y"))
        __sortingEnabled = self.PTC_TABLE.isSortingEnabled()
        self.PTC_TABLE.setSortingEnabled(False)
        item = self.PTC_TABLE.item(0, 0)
        item.setText(_translate("MainWindow", "1070"))
        item = self.PTC_TABLE.item(1, 0)
        item.setText(_translate("MainWindow", "1070"))
        self.PTC_TABLE.setSortingEnabled(__sortingEnabled)
        self.PTC_SAVECSV_BUTTON.setText(_translate("MainWindow", "SAVE AS CSV"))
        self.FRAME_3.setTabText(self.FRAME_3.indexOf(self.tab_3), _translate("MainWindow", "CHART"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())