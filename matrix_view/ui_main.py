# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        icon = QIcon()
        icon.addFile(u":/images/images/images/power.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Inter Medium\" 400;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(189, 147, 249);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"	font: 10pt \"Inter\";\n"
"}\n"
"\n"
"#home QPushButton {\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"	border: 1px solid white;\n"
"}\n"
"#"
                        "home QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border: 1px solid white;\n"
"	image: url(:/icons/images/icons/cil-plus.png);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #001010;\n"
"	border: 1px solid rgb(33,39,38);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(4, 10, 11);\n"
"	border-radius: 10px;\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(4, 10, 11);\n"
"	background-image: url(:/images/images/images/Polaris.png);\n"
"	background-position: center center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#titleLeftDescription { color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border:"
                        " none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	font: 10pt \"Inter Medium\";\n"
"	color: rgb(95, 106, 106);\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	font: 10pt \"Inter SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	font: 10pt \"Inter Medium\";\n"
"	color: rgb(95, 106, 106);\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Inter SemiBold\""
                        ";\n"
"}\n"
"\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(33,39,38);\n"
"}\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { \n"
"	padding-left: 10px; \n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(4, 10, 11);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgb"
                        "a(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(189, 147, 249); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(33,39,38);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	font: 10pt \"Inter SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Inter SemiBold\";	\n"
"}\n"
"\n"
"/* //////////////////////////"
                        "///////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(4, 10, 11);\n"
"	border-radius: 10px;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(33,39,38);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(4, 10, 11);\n"
"	border-bottom-left-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
" }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left:"
                        " 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	font: 10pt \"Inter SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Inter SemiBold\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(33,39,38);\n"
"}\n"
"QTableWidget::item{\n"
""
                        "	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(33,39,38);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(33,39,38);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(33,39,38);\n"
"    border-right: 1px solid rgb(33,39,38);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33,39,38);\n"
"	background-color: rgb(33,39,38);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, "
                        "43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33,39,38);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(189, 147, 249);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(189, 147, 249);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////"
                        "///////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScroll"
                        "Bar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     backgroun"
                        "d: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(33,39,38);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButto"
                        "n::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33,39,38);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox Q"
                        "AbstractItemView {\n"
"	color: rgb(189, 147, 249);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	backgroun"
                        "d-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(189, 147, 249);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* //////////////////////////////"
                        "///////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(33,39,38);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	font: 10pt \"Inter SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	font: 10pt \"Inter SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bg1 = QLabel(self.bgApp)
        self.bg1.setObjectName(u"bg1")
        self.bg1.setGeometry(QRect(0, 0, 191, 701))
        self.bg1.setStyleSheet(u"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"background-color: rgba(20, 79, 71, 150);\n"
"border: 1px solid #144F47;")
        self.bg2 = QLabel(self.bgApp)
        self.bg2.setObjectName(u"bg2")
        self.bg2.setGeometry(QRect(191, 1, 1071, 101))
        self.bg2.setStyleSheet(u"border-top-right-radius: 20px;\n"
"background-color: rgba(20, 79, 71, 150);\n"
"border-bottom: 1px solid #144F47;\n"
"border-right: 1px solid #144F47;\n"
"border-top: 1px solid #144F47;")
        self.bg3 = QLabel(self.bgApp)
        self.bg3.setObjectName(u"bg3")
        self.bg3.setGeometry(QRect(211, 121, 1051, 581))
        self.bg3.setStyleSheet(u"border-top-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"background-color: rgba(20, 79, 71, 150);\n"
"border: 1px solid #144F47;")
        self.matrix_title = QLabel(self.bgApp)
        self.matrix_title.setObjectName(u"matrix_title")
        self.matrix_title.setGeometry(QRect(90, 70, 81, 16))
        self.matrix_title.setMaximumSize(QSize(16777215, 16))
        font = QFont()
        font.setFamilies([u"Space Grotesk Medium"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.matrix_title.setFont(font)
        self.matrix_title.setStyleSheet(u"background-color: transparent;\n"
"font: 500 9pt \"Space Grotesk Medium\";\n"
"color: rgb(145, 145, 145);\n"
"text-align: left;")
        self.matrix_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dragBar = QFrame(self.bgApp)
        self.dragBar.setObjectName(u"dragBar")
        self.dragBar.setGeometry(QRect(0, 0, 1261, 71))
        self.dragBar.setStyleSheet(u"border: none;\n"
"background: transparent;")
        self.dragBar.setFrameShape(QFrame.StyledPanel)
        self.dragBar.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.dragBar)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(1220, 10, 31, 31))
        self.btn_close.setMinimumSize(QSize(10, 10))
        font1 = QFont()
        font1.setFamilies([u"Be Vietnam Pro"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_close.setFont(font1)
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"#btn_close {\n"
"background-color: transparent;\n"
"font: 500 9pt \"Be Vietnam Pro\";\n"
"text-align: left;\n"
"color: #A29F9F;\n"
"background-image: url(:/icons/images/icons/x.png);\n"
"background-position: center center;\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"background-repeat: no-repeat;\n"
"background-size: cover; \n"
"padding: 0;\n"
"margin: 0;\n"
"border-radius: 5px;\n"
"}\n"
"#btn_close:hover {\n"
"background-color: #2e3043;\n"
"border-color: rgb(238, 238, 238);\n"
"border: 2px solid;\n"
"font: 500 9pt \"Be Vietnam Pro\";\n"
"text-align: left;\n"
"color: #A29F9F;\n"
"background-image: url(:/icons/images/icons/x.png);\n"
"background-position: center center;\n"
"background-repeat: no-repeat;\n"
"border-radius: 5px;\n"
"border: 1px solid rgba(40, 27, 40, 150);\n"
"}\n"
"#btn_close:pressed {\n"
"background-color: rgb(93, 93, 93);\n"
"border: 1px solid #2e3043;\n"
"font: 500 9pt \"Be Vietnam Pro\";\n"
"text-align: left;\n"
"color: #A29F9F;\n"
"background-image: url(:/ic"
                        "ons/images/icons/x.png);\n"
"background-position: center center;\n"
"background-repeat: no-repeat;\n"
"border-radius: 5px;\n"
"}\n"
"")
        self.btn_close.setIconSize(QSize(21, 21))
        self.logo = QLabel(self.bgApp)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 40, 61, 61))
        self.logo.setPixmap(QPixmap(u":/images/images/images/power.jpg"))
        self.logo.setScaledContents(True)
        self.kato_title = QLabel(self.bgApp)
        self.kato_title.setObjectName(u"kato_title")
        self.kato_title.setGeometry(QRect(90, 50, 91, 16))
        self.kato_title.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Space Grotesk Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.kato_title.setFont(font2)
        self.kato_title.setStyleSheet(u"background-color: transparent;\n"
"font: 500 14pt \"Space Grotesk Medium\";\n"
"color: rgb(241, 241, 241);\n"
"text-align: left;")
        self.kato_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.key_title = QLabel(self.bgApp)
        self.key_title.setObjectName(u"key_title")
        self.key_title.setGeometry(QRect(21, 130, 81, 16))
        self.key_title.setMaximumSize(QSize(16777215, 16))
        self.key_title.setFont(font)
        self.key_title.setStyleSheet(u"background-color: transparent;\n"
"font: 500 9pt \"Space Grotesk Medium\";\n"
"color: rgb(145, 145, 145);\n"
"text-align: left;")
        self.key_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.key_field = QLineEdit(self.bgApp)
        self.key_field.setObjectName(u"key_field")
        self.key_field.setGeometry(QRect(20, 150, 161, 30))
        self.key_field.setMinimumSize(QSize(0, 30))
        self.key_field.setStyleSheet(u"background: solid rgb(16, 11, 16);\n"
"border: 2px solid #186b60;\n"
"border-radius: 10px;\n"
"font: 600 10pt \"Space Grotesk\";\n"
"color: white;")
        self.key_field.setMaxLength(16)
        self.key_field.setReadOnly(False)
        self.plaintext_field = QLineEdit(self.bgApp)
        self.plaintext_field.setObjectName(u"plaintext_field")
        self.plaintext_field.setGeometry(QRect(20, 220, 161, 30))
        self.plaintext_field.setMinimumSize(QSize(0, 30))
        self.plaintext_field.setStyleSheet(u"background: solid rgb(16, 11, 16);\n"
"border: 2px solid #186b60;\n"
"border-radius: 10px;\n"
"font: 600 10pt \"Space Grotesk\";\n"
"color: white;")
        self.plaintext_field.setMaxLength(16)
        self.plaintext_field.setReadOnly(False)
        self.plaintext_title = QLabel(self.bgApp)
        self.plaintext_title.setObjectName(u"plaintext_title")
        self.plaintext_title.setGeometry(QRect(21, 200, 81, 16))
        self.plaintext_title.setMaximumSize(QSize(16777215, 16))
        self.plaintext_title.setFont(font)
        self.plaintext_title.setStyleSheet(u"background-color: transparent;\n"
"font: 500 9pt \"Space Grotesk Medium\";\n"
"color: rgb(145, 145, 145);\n"
"text-align: left;")
        self.plaintext_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.iv_field = QLineEdit(self.bgApp)
        self.iv_field.setObjectName(u"iv_field")
        self.iv_field.setGeometry(QRect(20, 290, 161, 30))
        self.iv_field.setMinimumSize(QSize(0, 30))
        self.iv_field.setStyleSheet(u"background: solid rgb(16, 11, 16);\n"
"border: 2px solid #186b60;\n"
"border-radius: 10px;\n"
"font: 600 10pt \"Space Grotesk\";\n"
"color: white;")
        self.iv_field.setMaxLength(16)
        self.iv_field.setReadOnly(False)
        self.iv_title = QLabel(self.bgApp)
        self.iv_title.setObjectName(u"iv_title")
        self.iv_title.setGeometry(QRect(21, 270, 81, 16))
        self.iv_title.setMaximumSize(QSize(16777215, 16))
        self.iv_title.setFont(font)
        self.iv_title.setStyleSheet(u"background-color: transparent;\n"
"font: 500 9pt \"Space Grotesk Medium\";\n"
"color: rgb(145, 145, 145);\n"
"text-align: left;")
        self.iv_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ciphertext_title = QLabel(self.bgApp)
        self.ciphertext_title.setObjectName(u"ciphertext_title")
        self.ciphertext_title.setGeometry(QRect(21, 340, 81, 16))
        self.ciphertext_title.setMaximumSize(QSize(16777215, 16))
        self.ciphertext_title.setFont(font)
        self.ciphertext_title.setStyleSheet(u"background-color: transparent;\n"
"font: 500 9pt \"Space Grotesk Medium\";\n"
"color: rgb(145, 145, 145);\n"
"text-align: left;")
        self.ciphertext_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ciphertext_field = QLineEdit(self.bgApp)
        self.ciphertext_field.setObjectName(u"ciphertext_field")
        self.ciphertext_field.setGeometry(QRect(20, 360, 161, 131))
        self.ciphertext_field.setMinimumSize(QSize(0, 30))
        self.ciphertext_field.setStyleSheet(u"background: solid rgb(16, 11, 16);\n"
"border: 2px solid #186b60;\n"
"border-radius: 10px;\n"
"font: 600 10pt \"Space Grotesk\";\n"
"color: white;")
        self.ciphertext_field.setAlignment(Qt.AlignCenter)
        self.ciphertext_field.setReadOnly(False)
        self.encrypt_button = QPushButton(self.bgApp)
        self.encrypt_button.setObjectName(u"encrypt_button")
        self.encrypt_button.setGeometry(QRect(20, 510, 161, 30))
        self.encrypt_button.setMinimumSize(QSize(150, 30))
        font3 = QFont()
        font3.setFamilies([u"Space Grotesk Medium"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.encrypt_button.setFont(font3)
        self.encrypt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.encrypt_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(40, 27, 40);\n"
"	border: 2px solid #186b60;\n"
"	background: solid;\n"
"	border-radius: 5px;\n"
"	font: 500 10pt \"Space Grotesk Medium\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(40, 27, 40, 170);\n"
"	border: 2px solid #186b60;\n"
"	border-radius: 5px;\n"
"	font: 500 10pt \"Space Grotesk Medium\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255, 243, 239);\n"
"	font: 500 10pt \"Space Grotesk Medium\";\n"
"	icon: url(:/icons/images/icons/lock_green.png);\n"
"	color: #186b60;\n"
"	border-radius: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/lock_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.encrypt_button.setIcon(icon1)
        self.decrypt_button = QPushButton(self.bgApp)
        self.decrypt_button.setObjectName(u"decrypt_button")
        self.decrypt_button.setGeometry(QRect(20, 560, 161, 30))
        self.decrypt_button.setMinimumSize(QSize(150, 30))
        self.decrypt_button.setFont(font3)
        self.decrypt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.decrypt_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(40, 27, 40);\n"
"	border: 2px solid #186b60;\n"
"	background: solid;\n"
"	border-radius: 5px;\n"
"	font: 500 10pt \"Space Grotesk Medium\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(40, 27, 40, 170);\n"
"	border: 2px solid #186b60;\n"
"	border-radius: 5px;\n"
"	font: 500 10pt \"Space Grotesk Medium\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255, 243, 239);\n"
"	font: 500 10pt \"Space Grotesk Medium\";\n"
"	icon: url(:/icons/images/icons/unlock_green.png);\n"
"	color: #186b60;\n"
"	border-radius: 5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/unlock_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.decrypt_button.setIcon(icon2)
        self.frame = QFrame(self.bgApp)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(230, 150, 131, 541))
        self.frame.setStyleSheet(u"border: 2px solid white;\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.matrix00 = QLabel(self.frame)
        self.matrix00.setObjectName(u"matrix00")
        self.matrix00.setGeometry(QRect(10, 40, 111, 101))
        self.matrix00.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix10 = QLabel(self.frame)
        self.matrix10.setObjectName(u"matrix10")
        self.matrix10.setGeometry(QRect(10, 170, 111, 101))
        self.matrix10.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix20 = QLabel(self.frame)
        self.matrix20.setObjectName(u"matrix20")
        self.matrix20.setGeometry(QRect(10, 300, 111, 101))
        self.matrix20.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix30 = QLabel(self.frame)
        self.matrix30.setObjectName(u"matrix30")
        self.matrix30.setGeometry(QRect(10, 430, 111, 101))
        self.matrix30.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_title_2 = QLabel(self.frame)
        self.matrix_title_2.setObjectName(u"matrix_title_2")
        self.matrix_title_2.setGeometry(QRect(10, 20, 111, 16))
        self.matrix_title_2.setMaximumSize(QSize(16777215, 16))
        self.matrix_title_2.setFont(font)
        self.matrix_title_2.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.matrix_title_2.setAlignment(Qt.AlignCenter)
        self.placeholder_1 = QLabel(self.frame)
        self.placeholder_1.setObjectName(u"placeholder_1")
        self.placeholder_1.setGeometry(QRect(10, 150, 111, 16))
        self.placeholder_1.setMaximumSize(QSize(16777215, 16))
        self.placeholder_1.setFont(font)
        self.placeholder_1.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_1.setAlignment(Qt.AlignCenter)
        self.placeholder_2 = QLabel(self.frame)
        self.placeholder_2.setObjectName(u"placeholder_2")
        self.placeholder_2.setGeometry(QRect(10, 280, 111, 16))
        self.placeholder_2.setMaximumSize(QSize(16777215, 16))
        self.placeholder_2.setFont(font)
        self.placeholder_2.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_2.setAlignment(Qt.AlignCenter)
        self.placeholder_3 = QLabel(self.frame)
        self.placeholder_3.setObjectName(u"placeholder_3")
        self.placeholder_3.setGeometry(QRect(10, 410, 111, 16))
        self.placeholder_3.setMaximumSize(QSize(16777215, 16))
        self.placeholder_3.setFont(font)
        self.placeholder_3.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_3.setAlignment(Qt.AlignCenter)
        self.kato_title_2 = QLabel(self.bgApp)
        self.kato_title_2.setObjectName(u"kato_title_2")
        self.kato_title_2.setGeometry(QRect(230, 130, 131, 16))
        self.kato_title_2.setMaximumSize(QSize(16777215, 16))
        self.kato_title_2.setFont(font2)
        self.kato_title_2.setStyleSheet(u"background-color: transparent;\n"
"font: 500 14pt \"Space Grotesk Medium\";\n"
"color: rgb(241, 241, 241);\n"
"text-align: left;")
        self.kato_title_2.setAlignment(Qt.AlignCenter)
        self.kato_title_3 = QLabel(self.bgApp)
        self.kato_title_3.setObjectName(u"kato_title_3")
        self.kato_title_3.setGeometry(QRect(390, 130, 131, 16))
        self.kato_title_3.setMaximumSize(QSize(16777215, 16))
        self.kato_title_3.setFont(font2)
        self.kato_title_3.setStyleSheet(u"background-color: transparent;\n"
"font: 500 14pt \"Space Grotesk Medium\";\n"
"color: rgb(241, 241, 241);\n"
"text-align: left;")
        self.kato_title_3.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.bgApp)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(390, 150, 131, 541))
        self.frame_2.setStyleSheet(u"border: 2px solid white;\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.matrix01 = QLabel(self.frame_2)
        self.matrix01.setObjectName(u"matrix01")
        self.matrix01.setGeometry(QRect(10, 40, 111, 101))
        self.matrix01.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix11 = QLabel(self.frame_2)
        self.matrix11.setObjectName(u"matrix11")
        self.matrix11.setGeometry(QRect(10, 170, 111, 101))
        self.matrix11.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix21 = QLabel(self.frame_2)
        self.matrix21.setObjectName(u"matrix21")
        self.matrix21.setGeometry(QRect(10, 300, 111, 101))
        self.matrix21.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix31 = QLabel(self.frame_2)
        self.matrix31.setObjectName(u"matrix31")
        self.matrix31.setGeometry(QRect(10, 430, 111, 101))
        self.matrix31.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_title_3 = QLabel(self.frame_2)
        self.matrix_title_3.setObjectName(u"matrix_title_3")
        self.matrix_title_3.setGeometry(QRect(10, 20, 111, 16))
        self.matrix_title_3.setMaximumSize(QSize(16777215, 16))
        self.matrix_title_3.setFont(font)
        self.matrix_title_3.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.matrix_title_3.setAlignment(Qt.AlignCenter)
        self.placeholder_4 = QLabel(self.frame_2)
        self.placeholder_4.setObjectName(u"placeholder_4")
        self.placeholder_4.setGeometry(QRect(10, 150, 111, 16))
        self.placeholder_4.setMaximumSize(QSize(16777215, 16))
        self.placeholder_4.setFont(font)
        self.placeholder_4.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_4.setAlignment(Qt.AlignCenter)
        self.placeholder_5 = QLabel(self.frame_2)
        self.placeholder_5.setObjectName(u"placeholder_5")
        self.placeholder_5.setGeometry(QRect(10, 280, 111, 16))
        self.placeholder_5.setMaximumSize(QSize(16777215, 16))
        self.placeholder_5.setFont(font)
        self.placeholder_5.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_5.setAlignment(Qt.AlignCenter)
        self.placeholder_6 = QLabel(self.frame_2)
        self.placeholder_6.setObjectName(u"placeholder_6")
        self.placeholder_6.setGeometry(QRect(10, 410, 111, 16))
        self.placeholder_6.setMaximumSize(QSize(16777215, 16))
        self.placeholder_6.setFont(font)
        self.placeholder_6.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_6.setAlignment(Qt.AlignCenter)
        self.kato_title_4 = QLabel(self.bgApp)
        self.kato_title_4.setObjectName(u"kato_title_4")
        self.kato_title_4.setGeometry(QRect(550, 130, 131, 16))
        self.kato_title_4.setMaximumSize(QSize(16777215, 16))
        self.kato_title_4.setFont(font2)
        self.kato_title_4.setStyleSheet(u"background-color: transparent;\n"
"font: 500 14pt \"Space Grotesk Medium\";\n"
"color: rgb(241, 241, 241);\n"
"text-align: left;")
        self.kato_title_4.setAlignment(Qt.AlignCenter)
        self.frame_3 = QFrame(self.bgApp)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(550, 150, 131, 541))
        self.frame_3.setStyleSheet(u"border: 2px solid white;\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.matrix02 = QLabel(self.frame_3)
        self.matrix02.setObjectName(u"matrix02")
        self.matrix02.setGeometry(QRect(10, 40, 111, 101))
        self.matrix02.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix12 = QLabel(self.frame_3)
        self.matrix12.setObjectName(u"matrix12")
        self.matrix12.setGeometry(QRect(10, 170, 111, 101))
        self.matrix12.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix22 = QLabel(self.frame_3)
        self.matrix22.setObjectName(u"matrix22")
        self.matrix22.setGeometry(QRect(10, 300, 111, 101))
        self.matrix22.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix32 = QLabel(self.frame_3)
        self.matrix32.setObjectName(u"matrix32")
        self.matrix32.setGeometry(QRect(10, 430, 111, 101))
        self.matrix32.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_title_4 = QLabel(self.frame_3)
        self.matrix_title_4.setObjectName(u"matrix_title_4")
        self.matrix_title_4.setGeometry(QRect(10, 20, 111, 16))
        self.matrix_title_4.setMaximumSize(QSize(16777215, 16))
        self.matrix_title_4.setFont(font)
        self.matrix_title_4.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.matrix_title_4.setAlignment(Qt.AlignCenter)
        self.placeholder_7 = QLabel(self.frame_3)
        self.placeholder_7.setObjectName(u"placeholder_7")
        self.placeholder_7.setGeometry(QRect(10, 150, 111, 16))
        self.placeholder_7.setMaximumSize(QSize(16777215, 16))
        self.placeholder_7.setFont(font)
        self.placeholder_7.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_7.setAlignment(Qt.AlignCenter)
        self.placeholder_8 = QLabel(self.frame_3)
        self.placeholder_8.setObjectName(u"placeholder_8")
        self.placeholder_8.setGeometry(QRect(10, 280, 111, 16))
        self.placeholder_8.setMaximumSize(QSize(16777215, 16))
        self.placeholder_8.setFont(font)
        self.placeholder_8.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_8.setAlignment(Qt.AlignCenter)
        self.placeholder_9 = QLabel(self.frame_3)
        self.placeholder_9.setObjectName(u"placeholder_9")
        self.placeholder_9.setGeometry(QRect(10, 410, 111, 16))
        self.placeholder_9.setMaximumSize(QSize(16777215, 16))
        self.placeholder_9.setFont(font)
        self.placeholder_9.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_9.setAlignment(Qt.AlignCenter)
        self.frame_4 = QFrame(self.bgApp)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(710, 150, 131, 541))
        self.frame_4.setStyleSheet(u"border: 2px solid white;\n"
"border-radius: 20px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.matrix03 = QLabel(self.frame_4)
        self.matrix03.setObjectName(u"matrix03")
        self.matrix03.setGeometry(QRect(10, 40, 111, 101))
        self.matrix03.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix13 = QLabel(self.frame_4)
        self.matrix13.setObjectName(u"matrix13")
        self.matrix13.setGeometry(QRect(10, 170, 111, 101))
        self.matrix13.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix23 = QLabel(self.frame_4)
        self.matrix23.setObjectName(u"matrix23")
        self.matrix23.setGeometry(QRect(10, 300, 111, 101))
        self.matrix23.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix33 = QLabel(self.frame_4)
        self.matrix33.setObjectName(u"matrix33")
        self.matrix33.setGeometry(QRect(10, 430, 111, 101))
        self.matrix33.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_title_5 = QLabel(self.frame_4)
        self.matrix_title_5.setObjectName(u"matrix_title_5")
        self.matrix_title_5.setGeometry(QRect(10, 20, 111, 16))
        self.matrix_title_5.setMaximumSize(QSize(16777215, 16))
        self.matrix_title_5.setFont(font)
        self.matrix_title_5.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.matrix_title_5.setAlignment(Qt.AlignCenter)
        self.placeholder_10 = QLabel(self.frame_4)
        self.placeholder_10.setObjectName(u"placeholder_10")
        self.placeholder_10.setGeometry(QRect(10, 150, 111, 16))
        self.placeholder_10.setMaximumSize(QSize(16777215, 16))
        self.placeholder_10.setFont(font)
        self.placeholder_10.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_10.setAlignment(Qt.AlignCenter)
        self.placeholder_11 = QLabel(self.frame_4)
        self.placeholder_11.setObjectName(u"placeholder_11")
        self.placeholder_11.setGeometry(QRect(10, 280, 111, 16))
        self.placeholder_11.setMaximumSize(QSize(16777215, 16))
        self.placeholder_11.setFont(font)
        self.placeholder_11.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_11.setAlignment(Qt.AlignCenter)
        self.placeholder_12 = QLabel(self.frame_4)
        self.placeholder_12.setObjectName(u"placeholder_12")
        self.placeholder_12.setGeometry(QRect(10, 410, 111, 16))
        self.placeholder_12.setMaximumSize(QSize(16777215, 16))
        self.placeholder_12.setFont(font)
        self.placeholder_12.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_12.setAlignment(Qt.AlignCenter)
        self.kato_title_5 = QLabel(self.bgApp)
        self.kato_title_5.setObjectName(u"kato_title_5")
        self.kato_title_5.setGeometry(QRect(710, 130, 131, 16))
        self.kato_title_5.setMaximumSize(QSize(16777215, 16))
        self.kato_title_5.setFont(font2)
        self.kato_title_5.setStyleSheet(u"background-color: transparent;\n"
"font: 500 14pt \"Space Grotesk Medium\";\n"
"color: rgb(241, 241, 241);\n"
"text-align: left;")
        self.kato_title_5.setAlignment(Qt.AlignCenter)
        self.kato_title_6 = QLabel(self.bgApp)
        self.kato_title_6.setObjectName(u"kato_title_6")
        self.kato_title_6.setGeometry(QRect(870, 130, 131, 16))
        self.kato_title_6.setMaximumSize(QSize(16777215, 16))
        self.kato_title_6.setFont(font2)
        self.kato_title_6.setStyleSheet(u"background-color: transparent;\n"
"font: 500 14pt \"Space Grotesk Medium\";\n"
"color: rgb(241, 241, 241);\n"
"text-align: left;")
        self.kato_title_6.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.bgApp)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(870, 150, 131, 541))
        self.frame_5.setStyleSheet(u"border: 2px solid white;\n"
"border-radius: 20px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.matrix04 = QLabel(self.frame_5)
        self.matrix04.setObjectName(u"matrix04")
        self.matrix04.setGeometry(QRect(10, 40, 111, 101))
        self.matrix04.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix14 = QLabel(self.frame_5)
        self.matrix14.setObjectName(u"matrix14")
        self.matrix14.setGeometry(QRect(10, 170, 111, 101))
        self.matrix14.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix24 = QLabel(self.frame_5)
        self.matrix24.setObjectName(u"matrix24")
        self.matrix24.setGeometry(QRect(10, 300, 111, 101))
        self.matrix24.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix34 = QLabel(self.frame_5)
        self.matrix34.setObjectName(u"matrix34")
        self.matrix34.setGeometry(QRect(10, 430, 111, 101))
        self.matrix34.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_title_6 = QLabel(self.frame_5)
        self.matrix_title_6.setObjectName(u"matrix_title_6")
        self.matrix_title_6.setGeometry(QRect(10, 20, 111, 16))
        self.matrix_title_6.setMaximumSize(QSize(16777215, 16))
        self.matrix_title_6.setFont(font)
        self.matrix_title_6.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.matrix_title_6.setAlignment(Qt.AlignCenter)
        self.placeholder_13 = QLabel(self.frame_5)
        self.placeholder_13.setObjectName(u"placeholder_13")
        self.placeholder_13.setGeometry(QRect(10, 150, 111, 16))
        self.placeholder_13.setMaximumSize(QSize(16777215, 16))
        self.placeholder_13.setFont(font)
        self.placeholder_13.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_13.setAlignment(Qt.AlignCenter)
        self.placeholder_14 = QLabel(self.frame_5)
        self.placeholder_14.setObjectName(u"placeholder_14")
        self.placeholder_14.setGeometry(QRect(10, 280, 111, 16))
        self.placeholder_14.setMaximumSize(QSize(16777215, 16))
        self.placeholder_14.setFont(font)
        self.placeholder_14.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_14.setAlignment(Qt.AlignCenter)
        self.placeholder_15 = QLabel(self.frame_5)
        self.placeholder_15.setObjectName(u"placeholder_15")
        self.placeholder_15.setGeometry(QRect(10, 410, 111, 16))
        self.placeholder_15.setMaximumSize(QSize(16777215, 16))
        self.placeholder_15.setFont(font)
        self.placeholder_15.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_15.setAlignment(Qt.AlignCenter)
        self.kato_title_7 = QLabel(self.bgApp)
        self.kato_title_7.setObjectName(u"kato_title_7")
        self.kato_title_7.setGeometry(QRect(1100, 130, 131, 16))
        self.kato_title_7.setMaximumSize(QSize(16777215, 16))
        self.kato_title_7.setFont(font2)
        self.kato_title_7.setStyleSheet(u"background-color: transparent;\n"
"font: 500 14pt \"Space Grotesk Medium\";\n"
"color: rgb(241, 241, 241);\n"
"text-align: left;")
        self.kato_title_7.setAlignment(Qt.AlignCenter)
        self.frame_6 = QFrame(self.bgApp)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(1100, 150, 131, 541))
        self.frame_6.setStyleSheet(u"border: 2px solid white;\n"
"border-radius: 20px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.matrix_final_00 = QLabel(self.frame_6)
        self.matrix_final_00.setObjectName(u"matrix_final_00")
        self.matrix_final_00.setGeometry(QRect(10, 40, 111, 101))
        self.matrix_final_00.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_final_10 = QLabel(self.frame_6)
        self.matrix_final_10.setObjectName(u"matrix_final_10")
        self.matrix_final_10.setGeometry(QRect(10, 170, 111, 101))
        self.matrix_final_10.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_final_20 = QLabel(self.frame_6)
        self.matrix_final_20.setObjectName(u"matrix_final_20")
        self.matrix_final_20.setGeometry(QRect(10, 300, 111, 101))
        self.matrix_final_20.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_final_30 = QLabel(self.frame_6)
        self.matrix_final_30.setObjectName(u"matrix_final_30")
        self.matrix_final_30.setGeometry(QRect(10, 430, 111, 101))
        self.matrix_final_30.setStyleSheet(u"border: 2px solid #186b60;\n"
"border-radius: 15px;")
        self.matrix_title_7 = QLabel(self.frame_6)
        self.matrix_title_7.setObjectName(u"matrix_title_7")
        self.matrix_title_7.setGeometry(QRect(10, 20, 111, 16))
        self.matrix_title_7.setMaximumSize(QSize(16777215, 16))
        self.matrix_title_7.setFont(font)
        self.matrix_title_7.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.matrix_title_7.setAlignment(Qt.AlignCenter)
        self.placeholder_16 = QLabel(self.frame_6)
        self.placeholder_16.setObjectName(u"placeholder_16")
        self.placeholder_16.setGeometry(QRect(10, 150, 111, 16))
        self.placeholder_16.setMaximumSize(QSize(16777215, 16))
        self.placeholder_16.setFont(font)
        self.placeholder_16.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_16.setAlignment(Qt.AlignCenter)
        self.placeholder_17 = QLabel(self.frame_6)
        self.placeholder_17.setObjectName(u"placeholder_17")
        self.placeholder_17.setGeometry(QRect(10, 280, 111, 16))
        self.placeholder_17.setMaximumSize(QSize(16777215, 16))
        self.placeholder_17.setFont(font)
        self.placeholder_17.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_17.setAlignment(Qt.AlignCenter)
        self.placeholder_18 = QLabel(self.frame_6)
        self.placeholder_18.setObjectName(u"placeholder_18")
        self.placeholder_18.setGeometry(QRect(10, 410, 111, 16))
        self.placeholder_18.setMaximumSize(QSize(16777215, 16))
        self.placeholder_18.setFont(font)
        self.placeholder_18.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_18.setAlignment(Qt.AlignCenter)
        self.placeholder_19 = QLabel(self.bgApp)
        self.placeholder_19.setObjectName(u"placeholder_19")
        self.placeholder_19.setGeometry(QRect(1030, 390, 51, 16))
        self.placeholder_19.setMaximumSize(QSize(16777215, 16))
        self.placeholder_19.setFont(font)
        self.placeholder_19.setStyleSheet(u"border: none;\n"
"font: 500 9pt \"Space Grotesk Medium\";")
        self.placeholder_19.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.bgApp)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1053, 130, 6, 251))
        self.label.setStyleSheet(u"background-color: white;")
        self.label_2 = QLabel(self.bgApp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1053, 420, 6, 270))
        self.label_2.setStyleSheet(u"background-color: white;")
        self.status_label = QLabel(self.bgApp)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(20, 610, 161, 81))
        self.status_label.setMaximumSize(QSize(16777215, 100))
        self.status_label.setFont(font2)
        self.status_label.setStyleSheet(u"background-color: transparent;\n"
"font: 500 14pt \"Space Grotesk Medium\";\n"
"color: rgb(203, 0, 0);\n"
"text-align: left;")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kato | Matrix View", None))
        self.bg1.setText("")
        self.bg2.setText("")
        self.bg3.setText("")
        self.matrix_title.setText(QCoreApplication.translate("MainWindow", u"Matrix View", None))
        self.btn_close.setText("")
        self.logo.setText("")
        self.kato_title.setText(QCoreApplication.translate("MainWindow", u"Kato", None))
        self.key_title.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.key_field.setText("")
        self.key_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.plaintext_field.setText("")
        self.plaintext_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.plaintext_title.setText(QCoreApplication.translate("MainWindow", u"Plaintext", None))
        self.iv_field.setText("")
        self.iv_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.iv_title.setText(QCoreApplication.translate("MainWindow", u"IV (Optional)", None))
        self.ciphertext_title.setText(QCoreApplication.translate("MainWindow", u"Ciphertext", None))
        self.ciphertext_field.setText("")
        self.ciphertext_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.encrypt_button.setText(QCoreApplication.translate("MainWindow", u" Encrypt", None))
        self.decrypt_button.setText(QCoreApplication.translate("MainWindow", u" Decrypt", None))
        self.matrix00.setText("")
        self.matrix10.setText("")
        self.matrix20.setText("")
        self.matrix30.setText("")
        self.matrix_title_2.setText(QCoreApplication.translate("MainWindow", u"Initial Matrix", None))
        self.placeholder_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.kato_title_2.setText(QCoreApplication.translate("MainWindow", u"Round 1", None))
        self.kato_title_3.setText(QCoreApplication.translate("MainWindow", u"Round 2", None))
        self.matrix01.setText("")
        self.matrix11.setText("")
        self.matrix21.setText("")
        self.matrix31.setText("")
        self.matrix_title_3.setText(QCoreApplication.translate("MainWindow", u"Initial Matrix", None))
        self.placeholder_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.kato_title_4.setText(QCoreApplication.translate("MainWindow", u"Round 3", None))
        self.matrix02.setText("")
        self.matrix12.setText("")
        self.matrix22.setText("")
        self.matrix32.setText("")
        self.matrix_title_4.setText(QCoreApplication.translate("MainWindow", u"Initial Matrix", None))
        self.placeholder_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_8.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_9.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.matrix03.setText("")
        self.matrix13.setText("")
        self.matrix23.setText("")
        self.matrix33.setText("")
        self.matrix_title_5.setText(QCoreApplication.translate("MainWindow", u"Initial Matrix", None))
        self.placeholder_10.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_11.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_12.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.kato_title_5.setText(QCoreApplication.translate("MainWindow", u"Round 4", None))
        self.kato_title_6.setText(QCoreApplication.translate("MainWindow", u"Round 5", None))
        self.matrix04.setText("")
        self.matrix14.setText("")
        self.matrix24.setText("")
        self.matrix34.setText("")
        self.matrix_title_6.setText(QCoreApplication.translate("MainWindow", u"Initial Matrix", None))
        self.placeholder_13.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_14.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_15.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.kato_title_7.setText(QCoreApplication.translate("MainWindow", u"Round 10", None))
        self.matrix_final_00.setText("")
        self.matrix_final_10.setText("")
        self.matrix_final_20.setText("")
        self.matrix_final_30.setText("")
        self.matrix_title_7.setText(QCoreApplication.translate("MainWindow", u"Initial Matrix", None))
        self.placeholder_16.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_17.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_18.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.placeholder_19.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText("")
        self.label_2.setText("")
        self.status_label.setText("")
    # retranslateUi

