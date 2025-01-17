# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 659)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 10))
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"QPushButton{\n"
"	border: 2px solid gray\n"
"	border-radius: 50px\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.window_layout = QVBoxLayout()
        self.window_layout.setSpacing(0)
        self.window_layout.setObjectName(u"window_layout")
        self.header_container = QFrame(self.centralwidget)
        self.header_container.setObjectName(u"header_container")
        self.header_container.setMinimumSize(QSize(0, 32))
        self.header_container.setMaximumSize(QSize(16777215, 24))
        self.header_container.setFrameShape(QFrame.NoFrame)
        self.header_container.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.header_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header_container)
        self.header_left.setObjectName(u"header_left")
        self.header_left.setMinimumSize(QSize(10, 10))
        self.header_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.header_left.setFrameShape(QFrame.NoFrame)
        self.header_left.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_4.addWidget(self.header_left)

        self.header_center = QFrame(self.header_container)
        self.header_center.setObjectName(u"header_center")
        self.header_center.setMinimumSize(QSize(160, 0))
        self.header_center.setFrameShape(QFrame.NoFrame)
        self.header_center.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.header_center)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.header_center)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))
        self.label_3.setStyleSheet(u"font: 90 16pt \"Times New Roman\";")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.header_center)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(24, 24))
        self.label_4.setMaximumSize(QSize(24, 24))
        self.label_4.setPixmap(QPixmap(u":/logo/logo/logo small v2.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_4, 0, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addWidget(self.header_center)

        self.header_right = QFrame(self.header_container)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setFrameShape(QFrame.NoFrame)
        self.header_right.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.header_right)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_right)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_5.addWidget(self.frame)

        self.button_minimize = QPushButton(self.header_right)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon)
        self.button_minimize.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_minimize)

        self.button_maximize = QPushButton(self.header_right)
        self.button_maximize.setObjectName(u"button_maximize")
        self.button_maximize.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/expand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_maximize.setIcon(icon1)
        self.button_maximize.setCheckable(True)
        self.button_maximize.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_maximize)

        self.button_exit = QPushButton(self.header_right)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_exit.setIcon(icon2)
        self.button_exit.setFlat(True)

        self.horizontalLayout_5.addWidget(self.button_exit)


        self.horizontalLayout_4.addWidget(self.header_right)


        self.window_layout.addWidget(self.header_container)

        self.body_container = QFrame(self.centralwidget)
        self.body_container.setObjectName(u"body_container")
        self.body_container.setFrameShape(QFrame.NoFrame)
        self.body_container.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.body_container)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_container = QFrame(self.body_container)
        self.sidebar_container.setObjectName(u"sidebar_container")
        self.sidebar_container.setMinimumSize(QSize(56, 0))
        self.sidebar_container.setMaximumSize(QSize(56, 16777215))
        self.sidebar_container.setFrameShape(QFrame.NoFrame)
        self.sidebar_container.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.sidebar_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebaar_button_container = QFrame(self.sidebar_container)
        self.sidebaar_button_container.setObjectName(u"sidebaar_button_container")
        self.sidebaar_button_container.setFrameShape(QFrame.NoFrame)
        self.sidebaar_button_container.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.sidebaar_button_container)
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 48, 0, 0)
        self.button_go_to_home = QPushButton(self.sidebaar_button_container)
        self.button_go_to_home.setObjectName(u"button_go_to_home")
        self.button_go_to_home.setMinimumSize(QSize(0, 56))
        self.button_go_to_home.setStyleSheet(u"border-radius : 50")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/homeX64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_home.setIcon(icon3)
        self.button_go_to_home.setIconSize(QSize(24, 24))
        self.button_go_to_home.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_home)

        self.button_go_to_analytics = QPushButton(self.sidebaar_button_container)
        self.button_go_to_analytics.setObjectName(u"button_go_to_analytics")
        self.button_go_to_analytics.setMinimumSize(QSize(0, 56))
        self.button_go_to_analytics.setStyleSheet(u"border-radius : 50")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/chart-histogram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_analytics.setIcon(icon4)
        self.button_go_to_analytics.setIconSize(QSize(24, 24))
        self.button_go_to_analytics.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_analytics)

        self.button_go_to_settings = QPushButton(self.sidebaar_button_container)
        self.button_go_to_settings.setObjectName(u"button_go_to_settings")
        self.button_go_to_settings.setMinimumSize(QSize(0, 56))
        self.button_go_to_settings.setStyleSheet(u"border-radius : 50")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_go_to_settings.setIcon(icon5)
        self.button_go_to_settings.setIconSize(QSize(24, 24))
        self.button_go_to_settings.setAutoDefault(False)
        self.button_go_to_settings.setFlat(True)

        self.verticalLayout_2.addWidget(self.button_go_to_settings)

        self.frame_2 = QFrame(self.sidebaar_button_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.sidebaar_button_container)

        self.sidebar_footer = QFrame(self.sidebar_container)
        self.sidebar_footer.setObjectName(u"sidebar_footer")
        self.sidebar_footer.setFrameShape(QFrame.NoFrame)
        self.sidebar_footer.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.sidebar_footer)


        self.horizontalLayout_2.addWidget(self.sidebar_container)

        self.body_container_2 = QFrame(self.body_container)
        self.body_container_2.setObjectName(u"body_container_2")
        self.body_container_2.setFrameShape(QFrame.NoFrame)
        self.body_container_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.body_container_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.body_container_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_3 = QVBoxLayout(self.page_home)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.page_home_header = QFrame(self.page_home)
        self.page_home_header.setObjectName(u"page_home_header")
        self.page_home_header.setMaximumSize(QSize(16777215, 125))
        self.page_home_header.setFrameShape(QFrame.NoFrame)
        self.page_home_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.page_home_header)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.page_home_header_left = QFrame(self.page_home_header)
        self.page_home_header_left.setObjectName(u"page_home_header_left")
        self.page_home_header_left.setFrameShape(QFrame.NoFrame)
        self.page_home_header_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.page_home_header_left)

        self.page_home_header_center = QFrame(self.page_home_header)
        self.page_home_header_center.setObjectName(u"page_home_header_center")
        self.page_home_header_center.setMinimumSize(QSize(0, 100))
        self.page_home_header_center.setFrameShape(QFrame.NoFrame)
        self.page_home_header_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.page_home_header_center)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.page_home_header_center)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Lucida Calligraphy"])
        font.setPointSize(28)
        self.label_5.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.page_home_header_center)

        self.page_home_header_right = QFrame(self.page_home_header)
        self.page_home_header_right.setObjectName(u"page_home_header_right")
        self.page_home_header_right.setFrameShape(QFrame.NoFrame)
        self.page_home_header_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.page_home_header_right)


        self.verticalLayout_3.addWidget(self.page_home_header)

        self.page_home_body = QFrame(self.page_home)
        self.page_home_body.setObjectName(u"page_home_body")
        self.page_home_body.setMinimumSize(QSize(0, 300))
        self.page_home_body.setFrameShape(QFrame.NoFrame)
        self.page_home_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.page_home_body)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.page_home_body_left = QFrame(self.page_home_body)
        self.page_home_body_left.setObjectName(u"page_home_body_left")
        self.page_home_body_left.setFrameShape(QFrame.NoFrame)
        self.page_home_body_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.page_home_body_left)

        self.page_home_body_center = QFrame(self.page_home_body)
        self.page_home_body_center.setObjectName(u"page_home_body_center")
        sizePolicy.setHeightForWidth(self.page_home_body_center.sizePolicy().hasHeightForWidth())
        self.page_home_body_center.setSizePolicy(sizePolicy)
        self.page_home_body_center.setFrameShape(QFrame.NoFrame)
        self.page_home_body_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.page_home_body_center)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.page_home_body_center)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setPixmap(QPixmap(u":/logo/logo/logo v1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.page_home_body_center)

        self.page_home_body_right = QFrame(self.page_home_body)
        self.page_home_body_right.setObjectName(u"page_home_body_right")
        self.page_home_body_right.setFrameShape(QFrame.NoFrame)
        self.page_home_body_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.page_home_body_right)


        self.verticalLayout_3.addWidget(self.page_home_body)

        self.page_home_footer = QFrame(self.page_home)
        self.page_home_footer.setObjectName(u"page_home_footer")
        self.page_home_footer.setFrameShape(QFrame.NoFrame)
        self.page_home_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.page_home_footer)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.page_home_footer_left = QFrame(self.page_home_footer)
        self.page_home_footer_left.setObjectName(u"page_home_footer_left")
        self.page_home_footer_left.setFrameShape(QFrame.NoFrame)
        self.page_home_footer_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.page_home_footer_left)

        self.page_home_footer_center = QFrame(self.page_home_footer)
        self.page_home_footer_center.setObjectName(u"page_home_footer_center")
        self.page_home_footer_center.setFrameShape(QFrame.NoFrame)
        self.page_home_footer_center.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.page_home_footer_center)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 20, 151, 41))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid gray;\n"
"	border-radius: 20px;\n"
"\n"
"}")
        icon6 = QIcon()
        iconThemeName = u"applications-games"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u"../../../../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton.setIcon(icon6)
        self.pushButton.setCheckable(True)
        self.pushButton.setFlat(True)

        self.horizontalLayout_10.addWidget(self.page_home_footer_center)

        self.page_home_footerright = QFrame(self.page_home_footer)
        self.page_home_footerright.setObjectName(u"page_home_footerright")
        self.page_home_footerright.setFrameShape(QFrame.NoFrame)
        self.page_home_footerright.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.page_home_footerright)


        self.verticalLayout_3.addWidget(self.page_home_footer)

        self.stackedWidget.addWidget(self.page_home)
        self.page_analytics = QWidget()
        self.page_analytics.setObjectName(u"page_analytics")
        self.horizontalLayout_12 = QHBoxLayout(self.page_analytics)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.page_analytics_window_container = QFrame(self.page_analytics)
        self.page_analytics_window_container.setObjectName(u"page_analytics_window_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(6)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.page_analytics_window_container.sizePolicy().hasHeightForWidth())
        self.page_analytics_window_container.setSizePolicy(sizePolicy2)
        self.page_analytics_window_container.setFrameShape(QFrame.NoFrame)
        self.page_analytics_window_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.page_analytics_window_container)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_analytics_window_container)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMaximumSize(QSize(16777215, 120))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 0, 221, 51))
        self.label_13.setStyleSheet(u"font: 22pt \"MS Sans Serif\";")

        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 10, 146, 38))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.comboBox = QComboBox(self.frame_13)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_18.addWidget(self.comboBox)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(190, 10, 146, 38))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_19.addWidget(self.label_16)

        self.comboBox_2 = QComboBox(self.frame_14)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEditable(False)

        self.horizontalLayout_19.addWidget(self.comboBox_2)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.page_analytics_window_container)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy4)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(420, 300))
        self.scrollArea.setMaximumSize(QSize(12321, 600))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 541, 469))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.horizontalLayout_12.addWidget(self.page_analytics_window_container)

        self.page_analytic_points_container = QFrame(self.page_analytics)
        self.page_analytic_points_container.setObjectName(u"page_analytic_points_container")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(4)
        sizePolicy5.setVerticalStretch(4)
        sizePolicy5.setHeightForWidth(self.page_analytic_points_container.sizePolicy().hasHeightForWidth())
        self.page_analytic_points_container.setSizePolicy(sizePolicy5)
        self.page_analytic_points_container.setFrameShape(QFrame.NoFrame)
        self.page_analytic_points_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.page_analytic_points_container)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.page_analytic_points_container)
        self.label_14.setObjectName(u"label_14")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy6)
        self.label_14.setStyleSheet(u"font: 22pt \"MS Sans Serif\";")

        self.verticalLayout_14.addWidget(self.label_14)

        self.point_graph_container = QFrame(self.page_analytic_points_container)
        self.point_graph_container.setObjectName(u"point_graph_container")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(9)
        sizePolicy7.setHeightForWidth(self.point_graph_container.sizePolicy().hasHeightForWidth())
        self.point_graph_container.setSizePolicy(sizePolicy7)
        self.point_graph_container.setFrameShape(QFrame.NoFrame)
        self.point_graph_container.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.point_graph_container)

        self.frame_6 = QFrame(self.page_analytic_points_container)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(4)
        sizePolicy8.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy8)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_15.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_15.addWidget(self.label_18)


        self.verticalLayout_14.addWidget(self.frame_6)


        self.horizontalLayout_12.addWidget(self.page_analytic_points_container)

        self.stackedWidget.addWidget(self.page_analytics)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_13 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.page_settings_pages_container = QFrame(self.page_settings)
        self.page_settings_pages_container.setObjectName(u"page_settings_pages_container")
        self.page_settings_pages_container.setMinimumSize(QSize(100, 0))
        self.page_settings_pages_container.setMaximumSize(QSize(160, 16777215))
        self.page_settings_pages_container.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.page_settings_pages_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.page_settings_pages_container_top = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_top.setObjectName(u"page_settings_pages_container_top")
        self.page_settings_pages_container_top.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.page_settings_pages_container_top)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_settings_general = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_general.setObjectName(u"button_settings_general")
        self.button_settings_general.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setPointSize(10)
        self.button_settings_general.setFont(font2)
        self.button_settings_general.setStyleSheet(u"border-radius : 50")
        self.button_settings_general.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_general)

        self.button_settings_window = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_window.setObjectName(u"button_settings_window")
        self.button_settings_window.setEnabled(True)
        self.button_settings_window.setMinimumSize(QSize(100, 40))
        self.button_settings_window.setFont(font2)
        self.button_settings_window.setStyleSheet(u"border-radius : 50")
        self.button_settings_window.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_window)

        self.frame_5 = QFrame(self.page_settings_pages_container_top)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_5)

        self.button_settings_about = QPushButton(self.page_settings_pages_container_top)
        self.button_settings_about.setObjectName(u"button_settings_about")
        self.button_settings_about.setMinimumSize(QSize(100, 40))
        self.button_settings_about.setFont(font2)
        self.button_settings_about.setStyleSheet(u"border-radius : 50")
        self.button_settings_about.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_settings_about)


        self.verticalLayout_4.addWidget(self.page_settings_pages_container_top)

        self.page_settings_pages_container_center = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_center.setObjectName(u"page_settings_pages_container_center")
        self.page_settings_pages_container_center.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_center.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.page_settings_pages_container_center)

        self.page_settings_pages_container_bot = QFrame(self.page_settings_pages_container)
        self.page_settings_pages_container_bot.setObjectName(u"page_settings_pages_container_bot")
        self.page_settings_pages_container_bot.setFrameShape(QFrame.NoFrame)
        self.page_settings_pages_container_bot.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.page_settings_pages_container_bot)


        self.horizontalLayout_13.addWidget(self.page_settings_pages_container)

        self.page_settings_stacked_widget_container = QFrame(self.page_settings)
        self.page_settings_stacked_widget_container.setObjectName(u"page_settings_stacked_widget_container")
        sizePolicy9 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.page_settings_stacked_widget_container.sizePolicy().hasHeightForWidth())
        self.page_settings_stacked_widget_container.setSizePolicy(sizePolicy9)
        self.page_settings_stacked_widget_container.setFrameShape(QFrame.NoFrame)
        self.page_settings_stacked_widget_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.page_settings_stacked_widget_container)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.page_settings_stacked_widget = QStackedWidget(self.page_settings_stacked_widget_container)
        self.page_settings_stacked_widget.setObjectName(u"page_settings_stacked_widget")
        self.page_settings_stacked_widget_page_general = QWidget()
        self.page_settings_stacked_widget_page_general.setObjectName(u"page_settings_stacked_widget_page_general")
        self.verticalLayout_9 = QVBoxLayout(self.page_settings_stacked_widget_page_general)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.page_general_header = QFrame(self.page_settings_stacked_widget_page_general)
        self.page_general_header.setObjectName(u"page_general_header")
        self.page_general_header.setMinimumSize(QSize(0, 80))
        self.page_general_header.setMaximumSize(QSize(16777215, 80))
        self.page_general_header.setFrameShape(QFrame.NoFrame)
        self.page_general_header.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.page_general_header)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, -10, 221, 51))
        self.label_2.setStyleSheet(u"font: 22pt \"MS Sans Serif\";")

        self.verticalLayout_9.addWidget(self.page_general_header)

        self.page_general_footer = QFrame(self.page_settings_stacked_widget_page_general)
        self.page_general_footer.setObjectName(u"page_general_footer")
        self.page_general_footer.setFrameShape(QFrame.NoFrame)
        self.page_general_footer.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.page_general_footer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(50, 10, 403, 146))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_8.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_8)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_16.addWidget(self.label_9)

        self.textEdit = QTextEdit(self.frame_11)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 30))
        self.textEdit.setMaximumSize(QSize(16777215, 30))
        self.textEdit.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhMultiLine)
        self.textEdit.setFrameShape(QFrame.Box)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_16.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_17.addWidget(self.label_10)

        self.textEdit_2 = QTextEdit(self.frame_12)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QSize(0, 30))
        self.textEdit_2.setMaximumSize(QSize(16777215, 30))
        self.textEdit_2.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhMultiLine)
        self.textEdit_2.setFrameShape(QFrame.Box)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit_2.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_17.addWidget(self.textEdit_2)


        self.verticalLayout_12.addWidget(self.frame_12)


        self.verticalLayout_9.addWidget(self.page_general_footer)

        self.page_settings_stacked_widget.addWidget(self.page_settings_stacked_widget_page_general)
        self.page_settings_stacked_widget_page_window = QWidget()
        self.page_settings_stacked_widget_page_window.setObjectName(u"page_settings_stacked_widget_page_window")
        self.verticalLayout_10 = QVBoxLayout(self.page_settings_stacked_widget_page_window)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.page_window_header_2 = QFrame(self.page_settings_stacked_widget_page_window)
        self.page_window_header_2.setObjectName(u"page_window_header_2")
        self.page_window_header_2.setMinimumSize(QSize(0, 80))
        self.page_window_header_2.setMaximumSize(QSize(16777215, 80))
        self.page_window_header_2.setFrameShape(QFrame.NoFrame)
        self.page_window_header_2.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.page_window_header_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, -10, 221, 51))
        self.label_6.setStyleSheet(u"font: 22pt \"MS Sans Serif\";")

        self.verticalLayout_10.addWidget(self.page_window_header_2)

        self.page_window_footer_2 = QFrame(self.page_settings_stacked_widget_page_window)
        self.page_window_footer_2.setObjectName(u"page_window_footer_2")
        self.page_window_footer_2.setFrameShape(QFrame.NoFrame)
        self.page_window_footer_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.page_window_footer_2)

        self.page_settings_stacked_widget.addWidget(self.page_settings_stacked_widget_page_window)
        self.page_settings_stacked_widget_page_about = QWidget()
        self.page_settings_stacked_widget_page_about.setObjectName(u"page_settings_stacked_widget_page_about")
        self.verticalLayout_11 = QVBoxLayout(self.page_settings_stacked_widget_page_about)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.page_about_header_3 = QFrame(self.page_settings_stacked_widget_page_about)
        self.page_about_header_3.setObjectName(u"page_about_header_3")
        self.page_about_header_3.setMinimumSize(QSize(0, 80))
        self.page_about_header_3.setMaximumSize(QSize(16777215, 80))
        self.page_about_header_3.setFrameShape(QFrame.NoFrame)
        self.page_about_header_3.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.page_about_header_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, -10, 221, 51))
        self.label_7.setStyleSheet(u"font: 22pt \"MS Sans Serif\";")

        self.verticalLayout_11.addWidget(self.page_about_header_3)

        self.page_about_footer_3 = QFrame(self.page_settings_stacked_widget_page_about)
        self.page_about_footer_3.setObjectName(u"page_about_footer_3")
        self.page_about_footer_3.setFrameShape(QFrame.NoFrame)
        self.page_about_footer_3.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.page_about_footer_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 30, 141, 101))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(True)

        self.verticalLayout_13.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_10)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFlat(True)

        self.verticalLayout_13.addWidget(self.pushButton_3)

        self.label_11 = QLabel(self.page_about_footer_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 151, 20))
        self.label_11.setFont(font3)
        self.label_11.setFrameShape(QFrame.NoFrame)
        self.label_12 = QLabel(self.page_about_footer_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 150, 351, 61))
        self.label_12.setWordWrap(True)
        self.pushButton_4 = QPushButton(self.page_about_footer_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 220, 121, 31))
        self.pushButton_4.setFlat(True)

        self.verticalLayout_11.addWidget(self.page_about_footer_3)

        self.page_settings_stacked_widget.addWidget(self.page_settings_stacked_widget_page_about)

        self.horizontalLayout_14.addWidget(self.page_settings_stacked_widget)


        self.horizontalLayout_13.addWidget(self.page_settings_stacked_widget_container)

        self.stackedWidget.addWidget(self.page_settings)

        self.horizontalLayout_3.addWidget(self.stackedWidget)

        self.grip_down_left = QFrame(self.body_container_2)
        self.grip_down_left.setObjectName(u"grip_down_left")
        self.grip_down_left.setMinimumSize(QSize(10, 10))
        self.grip_down_left.setMaximumSize(QSize(10, 10))
        self.grip_down_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.grip_down_left.setFrameShape(QFrame.NoFrame)
        self.grip_down_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.grip_down_left, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.body_container_2)


        self.window_layout.addWidget(self.body_container)


        self.horizontalLayout.addLayout(self.window_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.button_go_to_settings.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)
        self.page_settings_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PyTrack", None))
        self.label_4.setText("")
        self.button_minimize.setText("")
        self.button_maximize.setText("")
        self.button_go_to_home.setText("")
        self.button_go_to_analytics.setText("")
        self.button_go_to_settings.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PyTrack Is Active", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Deactivate", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Windows", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.comboBox.setCurrentText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.comboBox_2.setCurrentText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Points Graph", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Minimum Points", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Maximum Points", None))
        self.button_settings_general.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.button_settings_window.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.button_settings_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"App", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Point Treshold(Break)", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Points (int)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Point Treshold(Break)", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Points (int)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Twitter", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Socials", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"I made this application as my year end project and my goal is to make a video out of it and post to youtube. If you would want to watch the video the link will be below.", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Youtube Video", None))
    # retranslateUi

