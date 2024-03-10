
from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (QGridLayout, QLineEdit, QPushButton, QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: white;\n"
                                 "    background-color: #121212;\n"
                                 "    font-family: Rubik;\n"
                                 "    font-size: 16pt;\n"
                                 "    font-weight: 600;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: transparent;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #666;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #888;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")


        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox.setMinimum(1)

        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox_2.setMinimum(15)
        self.spinBox_2.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setStyleSheet("color: #999;")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setStyleSheet("color: #999;")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_4")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_5)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        #
        #
        # firedot0 = 'Режим ГОСТ 30247.0.xlsx'
        # fireugl = 'Углеводород.xlsx'
        # firenar = 'Наружный режим.xlsx'
        # firetl = 'Тлеющий режим.xlsx'
        # firefasad = 'Фасад.xlsx'
        # self.pushButton.clicked.connect(lambda: self.firedot0(int(self.spinBox.text()), (int(self.spinBox_2.text()))+4))
        # self.pushButton_2.clicked.connect(lambda: self.fireugl(int(self.spinBox.text()), (int(self.spinBox_2.text())) + 4))
        # self.pushButton_3.clicked.connect(lambda: self.firenar(int(self.spinBox.text()), (int(self.spinBox_2.text())) + 4))
        # self.pushButton_4.clicked.connect(lambda: self.firetl(int(self.spinBox.text()), (int(self.spinBox_2.text())) + 4))
        # self.pushButton_5.clicked.connect(lambda: self.firefasad())
        # self.pushButton.clicked.connect(lambda: self.func(int(self.spinBox.text()), firedot0))
        # self.pushButton_2.clicked.connect(lambda: self.func(int(self.spinBox.text()), fireugl))
        # self.pushButton_3.clicked.connect(lambda: self.func(int(self.spinBox.text()), firenar))
        # self.pushButton_4.clicked.connect(lambda: self.func(int(self.spinBox.text()), firetl))
        # self.pushButton_5.clicked.connect(lambda: self.func(7, firefasad))

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u043e\u0439, \u044f \u0447\u0442\u043e-\u0442\u043e \u043d\u0430\u0436\u0430\u043b(\u0430) \u0438 \u0432\u0441\u0451 \u043f\u0440\u043e\u043f\u0430\u043b\u043e(", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0418\u0421\u041b\u041e \u0422\u0415\u0420\u041c\u041e\u041f\u0410\u0420", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0420\u0415\u041c\u042f, \u041c\u0418\u041d", None))
        #self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u041b\u0423\u0427\u0418\u0422\u042c \u042d\u041a\u0421\u0415\u041b\u042c\u041a\u0423", None))
        self.pushButton.setText('Получить 30247.0')
        self.pushButton_2.setText('Получить углеводород (хуй в рот)')
        self.pushButton_3.setText('Получить наружный режим')
        self.pushButton_4.setText('Получить тлеющий режим')
        self.pushButton_5.setText('Получить фасад (на число тп и время похуй)')


#
#     def addfunc(self):
#         firedot0 = 'Режим ГОСТ 30247.0.xlsx'
#         fireugl = 'Углеводород.xlsx'
#         firenar = 'Наружный режим.xlsx'
#         firetl = 'Тлеющий режим.xlsx'
#         self.pushButton.clicked.connect(lambda: self.firedot0(int(self.spinBox.text()), (int(self.spinBox_2.text()))+4))
#         self.pushButton_2.clicked.connect(lambda: self.fireugl(int(self.spinBox.text()), (int(self.spinBox_2.text())) + 4))
#         self.pushButton_3.clicked.connect(lambda: self.firenar(int(self.spinBox.text()), (int(self.spinBox_2.text())) + 4))
#         self.pushButton_4.clicked.connect(lambda: self.firetl(int(self.spinBox.text()), (int(self.spinBox_2.text())) + 4))
#         self.pushButton.clicked.connect(lambda: self.func(int(self.spinBox.text()), firedot0))
#         self.pushButton_2.clicked.connect(lambda: self.func(int(self.spinBox.text()), fireugl))
#         self.pushButton_3.clicked.connect(lambda: self.func(int(self.spinBox.text()), firenar))
#         self.pushButton_4.clicked.connect(lambda: self.func(int(self.spinBox.text()), firetl))
#
#
#     def firedot0(self, a, b):
#         filename = 'Режим ГОСТ 30247.0.xlsx'
#         book = op.Workbook()
#         sheet = book.active
#         sheet['B2'] = 'Время'
#         sheet['C2'] = 'Тmin'
#         sheet['D2'] = 'Tmax'
#         sheet['E2'] = 'Tпож'
#         for i in range(3, b):
#             sheet.cell(row=i, column=2).value = i - 3
#             sheet.cell(row=i, column=5).value = 345 * math.log10((i - 3) * 8 + 1) + 20
#             if (i - 3) <= 10:
#                 sheet.cell(row=i, column=3).value = 0.85 * (345 * math.log10((i - 3) * 8 + 1) + 20)
#                 sheet.cell(row=i, column=4).value = 1.15 * (345 * math.log10((i - 3) * 8 + 1) + 20)
#             elif 11 <= (i - 3) < 30:
#                 sheet.cell(row=i, column=3).value = 0.90 * (345 * math.log10((i - 3) * 8 + 1) + 20)
#                 sheet.cell(row=i, column=4).value = 1.10 * (345 * math.log10((i - 3) * 8 + 1) + 20)
#             else:
#                 sheet.cell(row=i, column=3).value = 0.95 * (345 * math.log10((i - 3) * 8 + 1) + 20)
#                 sheet.cell(row=i, column=4).value = 1.05 * (345 * math.log10((i - 3) * 8 + 1) + 20)
#         if a > 0:
#             for u in range(a):
#                 sheet.cell(row=2, column=u+6).value = 'Т'+ str(u+1)
#                 n = 0
#                 r = random.uniform(0.98, 1.02) * random.uniform(0.99, 1.01) * random.uniform(0.99, 1.01) * random.uniform(0.99, 1.01)
#                 for y in range(3, b):
#                     if 1 < n < 5:
#                         sheet.cell(row=y, column=u + 6).value = random.uniform(0.98, 1.02) * r * 345 * math.log10((y - 3) * 8 + 1) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 30 + random.uniform(-7, 7)
#                         n += 1
#                     elif 5 <= n < 11:
#                         sheet.cell(row=y, column=u + 6).value = r * 345 * math.log10((y - 3) * 8 + 1) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 15 + random.uniform(-3, 3)
#                         n += 1
#                     else:
#                         n += 1
#                         sheet.cell(row=y, column=u + 6).value = r * 345 * math.log10((y - 3) * 8 + 1) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 7
#             sheet.cell(row=2, column=a+6).value = 'Тср'
#
#             for t in range(3, b):
#                 o = 0
#                 for m in range(a):
#                     o += sheet.cell(row=t, column=(a + 6) - (m + 1)).value
#                 sheet.cell(row=t, column=a + 6).value = o / a
#
#         book.save('Режим ГОСТ 30247.0.xlsx')
#
#     def fireugl(self, a, b):
#         filename = 'Углеводород.xlsx'
#         book = op.Workbook()
#         sheet = book.active
#         sheet['B2'] = 'Время'
#         sheet['C2'] = 'Тmin'
#         sheet['D2'] = 'Tmax'
#         sheet['E2'] = 'Tпож'
#
#         for i in range(3, b):
#             sheet.cell(row=i, column=2).value = i - 3
#             sheet.cell(row=i, column=5).value = 1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20
#             if (i - 3) <= 10:
#                 sheet.cell(row=i, column=3).value = 0.85 * (1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20)
#                 sheet.cell(row=i, column=4).value = 1.15 * (1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20)
#             elif 10 < (i - 3) <= 30:
#                 sheet.cell(row=i, column=3).value = (1 - (0.01 * (15 - 0.5 * ((i - 3) - 10)))) * (1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20)
#                 sheet.cell(row=i, column=4).value = (1 + (0.01 * (15 - 0.5 * ((i - 3) - 10)))) * (1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20)
#             elif 30 < (i - 3) <= 60:
#                 sheet.cell(row=i, column=3).value = (1 - (0.01 * (5 - 0.083 * ((i - 3) - 30)))) * (1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20)
#                 sheet.cell(row=i, column=4).value = (1 + (0.01 * (5 - 0.083 * ((i - 3) - 30)))) * (1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20)
#             else:
#                 sheet.cell(row=i, column=3).value = 0.975 * (1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20)
#                 sheet.cell(row=i, column=4).value = 1.025 * (1080 * (1 - 0.325 * math.e ** (-0.167 * (i - 3)) - 0.675 * math.e ** (-2.5 * (i - 3))) + 20)
#
#         if a > 0:
#             for u in range(a):
#                 sheet.cell(row=2, column=u + 6).value = 'Т' + str(u + 1)
#                 n = 0
#                 r = random.uniform(0.98, 1.02) * random.uniform(0.99, 1.01) * random.uniform(0.99, 1.01) * random.uniform(0.99, 1.01)
#                 for y in range(3, b):
#                     if 1 < n < 5:
#                         sheet.cell(row=y, column=u + 6).value = random.uniform(0.95, 1.01) * r * 1080 * (1 - 0.325 * math.e ** (-0.167 * (y - 3)) - 0.675 * math.e ** (-2.5 * (y - 3))) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 40 + random.uniform(-10, 10)
#                         n += 1
#                     elif 5 <= n < 11:
#                         sheet.cell(row=y, column=u + 6).value = random.uniform(0.95, 1.01) * r * 1080 * (1 - 0.325 * math.e ** (-0.167 * (y - 3)) - 0.675 * math.e ** (-2.5 * (y - 3))) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 15 + random.uniform(-5, 5)
#                         n += 1
#                     else:
#                         n += 1
#                         sheet.cell(row=y, column=u + 6).value = r * 1080 * (1 - 0.325 * math.e ** (-0.167 * (y - 3)) - 0.675 * math.e ** (-2.5 * (y - 3))) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 7
#             sheet.cell(row=2, column=a + 6).value = 'Тср'
#
#             for t in range(3, b):
#                 o = 0
#                 for m in range(a):
#                     o += sheet.cell(row=t, column=(a + 6) - (m + 1)).value
#                 sheet.cell(row=t, column=a + 6).value = o / a
#
#         book.save('Углеводород.xlsx')
#
#     def firenar(self, a, b):
#         filename = 'Наружный режим.xlsx'
#         book = op.Workbook()
#         sheet = book.active
#         sheet['B2'] = 'Время'
#         sheet['C2'] = 'Тmin'
#         sheet['D2'] = 'Tmax'
#         sheet['E2'] = 'Tпож'
#
#         for i in range(3, b):
#             sheet.cell(row=i, column=2).value = i - 3
#             sheet.cell(row=i, column=5).value = 660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20
#             if (i - 3) <= 10:
#                 sheet.cell(row=i, column=3).value = 0.85 * (660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20)
#                 sheet.cell(row=i, column=4).value = 1.15 * (660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20)
#             elif 10 < (i - 3) <= 30:
#                 sheet.cell(row=i, column=3).value = (1 - (0.01 * (15 - 0.5 * ((i - 3) - 10)))) * (660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20)
#                 sheet.cell(row=i, column=4).value = (1 + (0.01 * (15 - 0.5 * ((i - 3) - 10)))) * (660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20)
#             elif 30 < (i - 3) <= 60:
#                 sheet.cell(row=i, column=3).value = (1 - (0.01 * (5 - 0.083 * ((i - 3) - 30)))) * (660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20)
#                 sheet.cell(row=i, column=4).value = (1 + (0.01 * (5 - 0.083 * ((i - 3) - 30)))) * (660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20)
#             else:
#                 sheet.cell(row=i, column=3).value = 0.975 * (660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20)
#                 sheet.cell(row=i, column=4).value = 1.025 * (660 * (1 - 0.687 * math.e ** (-0.32 * (i - 3)) - 0.313 * math.e ** (-3.8 * (i - 3))) + 20)
#
#         if a > 0:
#             for u in range(a):
#                 sheet.cell(row=2, column=u + 6).value = 'Т' + str(u + 1)
#                 n = 0
#                 r = random.uniform(0.98, 1.02) * random.uniform(0.99, 1.01) * random.uniform(0.99, 1.01)
#                 for y in range(3, b):
#                     if 1 < n < 5:
#                         sheet.cell(row=y, column=u + 6).value = random.uniform(0.96, 1.01) * r * 660 * (1 - 0.687 * math.e ** (-0.32 * (y - 3)) - 0.313 * math.e ** (-3.8 * (y - 3))) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 30 + random.uniform(-7, 7)
#                         n += 1
#                     elif 5 <= n < 11:
#                         sheet.cell(row=y, column=u + 6).value = random.uniform(0.96, 1.01) * r * 660 * (1 - 0.687 * math.e ** (-0.32 * (y - 3)) - 0.313 * math.e ** (-3.8 * (y - 3))) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 15 + random.uniform(-3, 3)
#                         n += 1
#                     else:
#                         n += 1
#                         sheet.cell(row=y, column=u + 6).value = r * 660 * (1 - 0.687 * math.e ** (-0.32 * (y - 3)) - 0.313 * math.e ** (-3.8 * (y - 3))) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 7
#             sheet.cell(row=2, column=a + 6).value = 'Тср'
#
#             for t in range(3, b):
#                 o = 0
#                 for m in range(a):
#                     o += sheet.cell(row=t, column=(a + 6) - (m + 1)).value
#                 sheet.cell(row=t, column=a + 6).value = o / a
#
#         book.save('Наружный режим.xlsx')
#
#     def firetl(self, a, b):
#         filename = 'Тлеющий режим.xlsx'
#         book = op.Workbook()
#         sheet = book.active
#         sheet['B2'] = 'Время'
#         sheet['C2'] = 'Тmin'
#         sheet['D2'] = 'Tmax'
#         sheet['E2'] = 'Tпож'
#
#         for i in range(3, b):
#             sheet.cell(row=i, column=2).value = i - 3
#             if (i - 3) <= 10:
#                 sheet.cell(row=i, column=5).value = 154 * (i-3)**0.25 + 20
#                 sheet.cell(row=i, column=3).value = 0.85 * (154 * (i-3)**0.25 + 20)
#                 sheet.cell(row=i, column=4).value = 1.15 * (154 * (i-3)**0.25 + 20)
#             elif 10 < (i - 3) <= 21:
#                 sheet.cell(row=i, column=5).value = 154 * (i-3)**0.25 + 20
#                 sheet.cell(row=i, column=3).value = (1 - (0.01 * (15 - 0.5 * ((i - 3) - 10)))) * (154 * (i-3)**0.25 + 20)
#                 sheet.cell(row=i, column=4).value = (1 + (0.01 * (15 - 0.5 * ((i - 3) - 10)))) * (154 * (i-3)**0.25 + 20)
#             elif 21 < (i - 3) <= 30:
#                 sheet.cell(row=i, column=5).value = 345 * math.log10(8 * ((i - 3) - 20) + 1) + 20
#                 sheet.cell(row=i, column=3).value = (1 - (0.01 * (15 - 0.5 * ((i - 3) - 10)))) * (345 * math.log10(8 * ((i - 3) - 20) + 1) + 20)
#                 sheet.cell(row=i, column=4).value = (1 + (0.01 * (15 - 0.5 * ((i - 3) - 10)))) * (345 * math.log10(8 * ((i - 3) - 20) + 1) + 20)
#             elif 30 < (i - 3) <= 60:
#                 sheet.cell(row=i, column=5).value = 345 * math.log10(8 * ((i - 3) - 20) + 1) + 20
#                 sheet.cell(row=i, column=3).value = (1 - (0.01 * (5 - 0.083 * ((i - 3) - 30)))) * (345 * math.log10(8 * ((i - 3) - 20) + 1) + 20)
#                 sheet.cell(row=i, column=4).value = (1 + (0.01 * (5 - 0.083 * ((i - 3) - 30)))) * (345 * math.log10(8 * ((i - 3) - 20) + 1) + 20)
#             else:
#                 sheet.cell(row=i, column=5).value = 345 * math.log10(8 * ((i - 3) - 20) + 1) + 20
#                 sheet.cell(row=i, column=3).value = 0.975 * (345 * math.log10(8 * ((i - 3) - 20) + 1) + 20)
#                 sheet.cell(row=i, column=4).value = 1.025 * (345 * math.log10(8 * ((i - 3) - 20) + 1) + 20)
#
#         if a > 0:
#             for u in range(a):
#                 n = 0
#                 sheet.cell(row=2, column=u + 6).value = 'Т' + str(u + 1)
#                 r = random.uniform(0.98, 1.02) * random.uniform(0.99, 1.02) * random.uniform(0.99, 1.01) * random.uniform(0.99, 1.01)
#                 for y in range(3, b):
#                     if 0 <= n < 5:
#                         sheet.cell(row=y, column=u + 6).value = r * 154 * (y - 3)**0.25 + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 40 + random.uniform(-5, 5)
#                         n += 1
#                     elif 5 <= n <= 21:
#                         sheet.cell(row=y, column=u + 6).value = r * 154 * (y - 3)**0.25 + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 10 + random.uniform(-3, 3)
#                         n += 1
#                     else:
#                         sheet.cell(row=y, column=u + 6).value = r * 345 * math.log10(8 * ((y - 3) - 20) + 1) + 20 + random.randint(-1, 1) * random.betavariate(1, 3) * 5
#                         n += 1
#             sheet.cell(row=2, column=a + 6).value = 'Тср'
#
#             for t in range(3, b):
#                 o = 0
#                 for m in range(a):
#                     o += sheet.cell(row=t, column=(a + 6) - (m + 1)).value
#                 sheet.cell(row=t, column=a + 6).value = o / a
#
#         book.save('Тлеющий режим.xlsx')
#
#     def firefasad(self):
#         filename = 'Фасад.xlsx'
#         book = op.Workbook()
#         sheet = book.active
#         sheet['B2'] = 'Время'
#         sheet['C2'] = 'Тmin'
#         sheet['D2'] = 'Tmax'
#         sheet['E2'] = 'Tпож'
#         r = random.uniform(0.98, 1.02) * random.uniform(0.99, 1.01) * random.uniform(0.99, 1.01) * random.uniform(0.99,1.01)
#         r2 = random.uniform(0.93, 1.07) * random.uniform(0.99, 1.02) * random.uniform(0.99, 1.01) * random.uniform(0.99,1.01)
#         r3 = random.uniform(0.93, 1.03) * random.uniform(0.99, 1.01) * random.uniform(0.99, 1.01) * random.uniform(0.99,1.01)
#         ran2 = random.uniform(0.85, 0.95)
#         ran3 = random.uniform(0.75, 0.85)
#         ran4 = random.uniform(0.55, 0.65)
#         ran5 = random.uniform(0.45, 0.55)
#         ran6 = random.uniform(0.35, 0.45)
#         ran7 = random.uniform(0.15, 0.25)
#         for i in range(3, 49):
#             sheet.cell(row=i, column=2).value = i - 3
#             if (i - 3) <= 7:
#                 sheet.cell(row=i, column=12).value = ran7 * r2 * (105 * (i-3) + 115 + random.randint(-1, 1) * random.betavariate(1, 3) * 60 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=11).value = ran6 * r2 * (105 * (i-3) + 115 + random.randint(-1, 1) * random.betavariate(1, 3) * 60 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=10).value = ran5 * r2 * (105 * (i-3) + 115 + random.randint(-1, 1) * random.betavariate(1, 3) * 60 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=9).value = ran4 * r2 * (105 * (i-3) + 115 + random.randint(-1, 1) * random.betavariate(1, 3) * 60 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=8).value = ran3 * r2 * (105 * (i-3) + 115 + random.randint(-1, 1) * random.betavariate(1, 3) * 60 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=7).value = ran2 * r2 * (105 * (i-3) + 115 + random.randint(-1, 1) * random.betavariate(1, 3) * 60 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=6).value = r2 * (105 * (i-3) + 115) + random.randint(-1, 1) * random.betavariate(1, 3) * 60 + random.uniform(-3, 3)
#
#                 sheet.cell(row=i, column=5).value = 105 * (i-3) + 115
#                 sheet.cell(row=i, column=3).value = (105 * (i-3) + 115) * 0.8
#                 sheet.cell(row=i, column=4).value = (105 * (i-3) + 115) * 1.2
#             elif 7 < (i - 3) <= 25:
#                 sheet.cell(row=i, column=12).value = ran7 * r * (850 + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=11).value = ran6 * r * (850 + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=10).value = ran5 * r * (850 + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=9).value = ran4 * r * (850 + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=8).value = ran3 * r * (850 + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=7).value = ran2 * r * (850 + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=6).value = r * 850 + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3)
#
#                 sheet.cell(row=i, column=5).value = 850
#                 sheet.cell(row=i, column=3).value = 850 * 0.94
#                 sheet.cell(row=i, column=4).value = 850 * 1.06
#             else:
#                 sheet.cell(row=i, column=12).value = ran7 * r3 * (850 - 20 * (i - 28) + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=11).value = ran6 * r3 * (850 - 20 * (i - 28) + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=10).value = ran5 * r3 * (850 - 20 * (i - 28) + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=9).value = ran4 * r3 * (850 - 20 * (i - 28) + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=8).value = ran3 * r3 * (850 - 20 * (i - 28) + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=7).value = ran2 * r3 * (850 - 20 * (i - 28) + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3))
#                 sheet.cell(row=i, column=6).value = r3 * (850 - 20 * (i - 28)) + random.randint(-1, 1) * random.betavariate(1, 3) * 20 + random.uniform(-3, 3)
#
#                 sheet.cell(row=i, column=5).value = 850 - 20 * (i - 28)
#                 sheet.cell(row=i, column=3).value = (850 - 20 * (i - 28)) * 0.8
#                 sheet.cell(row=i, column=4).value = (850 - 20 * (i - 28)) * 1.2
#
#         book.save('Фасад.xlsx')
#
#     def func(self, a, b):
#         plt.close('all')
#         df = pd.read_excel(b)
#         data_array = df.to_numpy()
#         data_array = data_array[1:]
#         transposed_array = data_array.transpose()
#         transposed_array = transposed_array[1:]
#         if a > 1:
#             for i in range(a+1):
#                 plt.plot(np.array(transposed_array[0]), np.array(transposed_array[i+3]), color='k', linewidth=0.3)
#         if b != 'Фасад.xlsx':
#             x1, y1 = np.array(transposed_array[0]), np.array(transposed_array[a + 4])
#             plt.plot(x1, y1, color='red')
#         elif b == 'Фасад.xlsx':
#             plt.plot([10, 20], [600, 600], color='green')
#         x2, y2 = np.array(transposed_array[0]), np.array(transposed_array[1])
#         x3, y3 = np.array(transposed_array[0]), np.array(transposed_array[2])
#         x4, y4 = np.array(transposed_array[0]), np.array(transposed_array[3])
#         plt.plot(x2, y2, color='blue')
#         plt.plot(x3, y3, color='m')
#         plt.plot(x4, y4, color='black', linestyle='dashed')
#         plt.xlabel('Time')
#         plt.ylabel('Temperature')
#         window = plt.get_current_fig_manager().window
#         window.setWindowFlags(window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
#         plt.show()
#         window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
#         plt.show()
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())