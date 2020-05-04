# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SortingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_SortingTechniques(object):
    def setupUi(self, SortingTechniques):
        
        SortingTechniques.setObjectName("SortingTechniques")
        SortingTechniques.resize(935, 629)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SortingTechniques.sizePolicy().hasHeightForWidth())
        SortingTechniques.setSizePolicy(sizePolicy)
        SortingTechniques.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.8, fx:0.5, fy:0.505682, stop:0.3125 rgba(255, 255, 255, 255), stop:1 rgba(106, 212, 245, 255));")
        
        self.gridLayout = QtWidgets.QGridLayout(SortingTechniques)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        
        self.label = QtWidgets.QLabel(SortingTechniques)
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(200, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(-20)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        
        self.groupBox = QtWidgets.QGroupBox(SortingTechniques)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 65);")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.bubble_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bubble_sort.setFont(font)
        self.bubble_sort.setObjectName("bubble_sort")
        
        self.horizontalLayout.addWidget(self.bubble_sort)
        
        self.selection_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.selection_sort.setFont(font)
        self.selection_sort.setObjectName("selection_sort")
        
        self.horizontalLayout.addWidget(self.selection_sort)
        
        self.insertion_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.insertion_sort.setFont(font)
        self.insertion_sort.setObjectName("insertion_sort")
        
        self.horizontalLayout.addWidget(self.insertion_sort)
        
        self.merge_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.merge_sort.setFont(font)
        self.merge_sort.setObjectName("merge_sort")
        
        self.horizontalLayout.addWidget(self.merge_sort)
        
        self.quick_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.quick_sort.setFont(font)
        self.quick_sort.setObjectName("quick_sort")
        
        self.horizontalLayout.addWidget(self.quick_sort)
        
        self.heap_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.heap_sort.setFont(font)
        self.heap_sort.setObjectName("heap_sort")
        
        self.horizontalLayout.addWidget(self.heap_sort)
        
        self.count_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.count_sort.setFont(font)
        self.count_sort.setObjectName("count_sort")
        
        self.horizontalLayout.addWidget(self.count_sort)
        
        self.radix_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radix_sort.setFont(font)
        self.radix_sort.setObjectName("radix_sort")
        
        self.horizontalLayout.addWidget(self.radix_sort)
        
        self.bucket_sort = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bucket_sort.setFont(font)
        self.bucket_sort.setObjectName("bucket_sort")
        
        self.horizontalLayout.addWidget(self.bucket_sort)
        
        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)
        
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.scrollArea = QtWidgets.QScrollArea(SortingTechniques)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(400, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 398, 496))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(255,255,255,0);\n"
"color: rgb(0, 0, 65);")
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        
        self.description = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.description.setGeometry(QtCore.QRect(10, 50, 381, 441))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.description.setFont(font)
        self.description.setAutoFillBackground(False)
        self.description.setStyleSheet("background-color:rgba(255,255,255,0);")
        self.description.setDocumentTitle("")
        self.description.setReadOnly(True)
        self.description.setBackgroundVisible(False)
        self.description.setCenterOnScroll(False)
        self.description.setObjectName("description")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        
        self.gridLayout_2.addWidget(self.scrollArea, 0, 1, 1, 1)
        
        self.groupBox_2 = QtWidgets.QGroupBox(SortingTechniques)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(0, 0, 65);")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        
        self.algo_selected = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algo_selected.sizePolicy().hasHeightForWidth())
        self.algo_selected.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.algo_selected.setFont(font)
        self.algo_selected.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.algo_selected.setObjectName("algo_selected")
        
        self.gridLayout_4.addWidget(self.algo_selected, 0, 1, 1, 1)
        
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 4, 0, 1, 1)
        
        self.execute = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.execute.sizePolicy().hasHeightForWidth())
        self.execute.setSizePolicy(sizePolicy)
        self.execute.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.execute.setFont(font)
        self.execute.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"color: rgb(0, 0, 60);")
        self.execute.setObjectName("execute")
        
        self.gridLayout_4.addWidget(self.execute, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        
        self.output_display = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_display.sizePolicy().hasHeightForWidth())
        self.output_display.setSizePolicy(sizePolicy)
        self.output_display.setStyleSheet("background-color: rgb(255,255,255);")
        self.output_display.setObjectName("output_display")
        
        self.gridLayout_4.addWidget(self.output_display, 3, 1, 1, 1)
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(1, 20, 481, 41))
        self.widget.setObjectName("widget")
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.ordr_asc = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ordr_asc.setFont(font)
        self.ordr_asc.setObjectName("ordr_asc")
        
        self.horizontalLayout_3.addWidget(self.ordr_asc)
        
        self.ordr_desc = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ordr_desc.setFont(font)
        self.ordr_desc.setObjectName("ordr_desc")
        
        self.horizontalLayout_3.addWidget(self.ordr_desc)
        
        self.ordr_random = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ordr_random.setFont(font)
        self.ordr_random.setObjectName("ordr_random")
        
        self.horizontalLayout_3.addWidget(self.ordr_random)
        
        self.widget1 = QtWidgets.QWidget(self.groupBox_3)
        self.widget1.setGeometry(QtCore.QRect(1, 70, 481, 111))
        self.widget1.setObjectName("widget1")
        
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        
        self.auto_gen_input = QtWidgets.QPlainTextEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_gen_input.sizePolicy().hasHeightForWidth())
        self.auto_gen_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.auto_gen_input.setFont(font)
        self.auto_gen_input.setStyleSheet("background-color: rgb(255,255,255);")
        self.auto_gen_input.setObjectName("auto_gen_input")
        
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.auto_gen_input)
        
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 2)
        
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(False)
        self.groupBox_4.setObjectName("groupBox_4")
        
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 30, 481, 152))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setToolTip("")
        self.label_5.setToolTipDuration(-1)
        self.label_5.setObjectName("label_5")
        
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        
        self.input_size = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_size.setToolTipDuration(-1)
        self.input_size.setStyleSheet("background-color: white;")
        self.input_size.setObjectName("input_size")
        
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_size)
        
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        
        self.user_input = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_input.sizePolicy().hasHeightForWidth())
        self.user_input.setSizePolicy(sizePolicy)
        self.user_input.setStyleSheet("background-color: white;")
        self.user_input.setObjectName("user_input")
        
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.user_input)
        
        self.gridLayout_4.addWidget(self.groupBox_4, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 3)
        
        #Condition-checking variables
        self.AlgoCheck = False
        self.inputCheck = False
        
        #Event Listeners
        self.bubble_sort.toggled.connect(self.setAlgo)
        self.selection_sort.toggled.connect(self.setAlgo)
        self.insertion_sort.toggled.connect(self.setAlgo)
        self.merge_sort.toggled.connect(self.setAlgo)
        self.quick_sort.toggled.connect(self.setAlgo)
        self.heap_sort.toggled.connect(self.setAlgo)
        self.radix_sort.toggled.connect(self.setAlgo)
        self.count_sort.toggled.connect(self.setAlgo)
        self.bucket_sort.toggled.connect(self.setAlgo)
        
        self.groupBox_3.toggled.connect(self.input_method)
        self.groupBox_4.toggled.connect(self.input_method)
        
        self.ordr_asc.toggled.connect(self.getRandomInput)
        self.ordr_desc.toggled.connect(self.getRandomInput)
        self.ordr_random.toggled.connect(self.getRandomInput)
        
        self.execute.clicked.connect(self.Execute)

        self.retranslateUi(SortingTechniques)
        QtCore.QMetaObject.connectSlotsByName(SortingTechniques)

    def retranslateUi(self, SortingTechniques):
        _translate = QtCore.QCoreApplication.translate
        SortingTechniques.setWindowTitle(_translate("SortingTechniques", "Sorting"))
        self.label.setText(_translate("SortingTechniques", "Sorting Techniques"))
        self.groupBox.setTitle(_translate("SortingTechniques", "Algorithms"))
        self.bubble_sort.setText(_translate("SortingTechniques", "Bubble Sort"))
        self.selection_sort.setText(_translate("SortingTechniques", "Selection Sort"))
        self.insertion_sort.setText(_translate("SortingTechniques", "Insertion Sort"))
        self.merge_sort.setText(_translate("SortingTechniques", "Merge Sort"))
        self.quick_sort.setText(_translate("SortingTechniques", "Quick Sort"))
        self.heap_sort.setText(_translate("SortingTechniques", "Heap Sort"))
        self.count_sort.setText(_translate("SortingTechniques", "Counting Sort"))
        self.radix_sort.setText(_translate("SortingTechniques", "Radix Sort"))
        self.bucket_sort.setText(_translate("SortingTechniques", "Bucket Sort"))
        self.label_7.setText(_translate("SortingTechniques", "Sorting"))
        self.description.setPlainText(_translate("SortingTechniques", "Sorting refers to the operation or technique of arranging and rearranging sets of data in some specific order.\n"
"\n"
"A Sorting Algorithm is used to rearrange a given array or list elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of element in the respective data structure.\n"
"For example: The below list is sorted in increasing order:\n"
"[10,4,2,5,7,15] => [2,4,5,7,10,15]\n"
"\n"
"Types of Sorting Algorithms:\n"
"1. Bubble Sort\n"
"2. Selection Sort\n"
"3. Insertion Sort\n"
"4. Merge Sort\n"
"5. Quick Sort\n"
"6. Heap Sort\n"
"**Linear Time Sorting Algorithms**\n"
"7. Counting Sort\n"
"8. Radix Sort\n"
"9. Bucket Sort"))
        self.groupBox_2.setTitle(_translate("SortingTechniques", "Implementation"))
        self.label_3.setText(_translate("SortingTechniques", "Output"))
        self.label_2.setText(_translate("SortingTechniques", "Algorithm Selected"))
        self.execute.setText(_translate("SortingTechniques", "Execute"))
        self.groupBox_3.setTitle(_translate("SortingTechniques", "Auto-generated Input"))
        self.ordr_asc.setText(_translate("SortingTechniques", "Ascending"))
        self.ordr_desc.setText(_translate("SortingTechniques", "Descending"))
        self.ordr_random.setText(_translate("SortingTechniques", "Random"))
        self.label_4.setText(_translate("SortingTechniques", "Input"))
        self.auto_gen_input.setPlaceholderText(_translate("SortingTechniques", "Input goes here..."))
        self.groupBox_4.setTitle(_translate("SortingTechniques", "Custom Input"))
        self.label_5.setText(_translate("SortingTechniques", "Input Size"))
        self.input_size.setToolTip(_translate("SortingTechniques", "\"Enter no. of elements in your input...\""))
        self.input_size.setPlaceholderText(_translate("SortingTechniques", "Enter the input size..."))
        self.label_6.setText(_translate("SortingTechniques", "Input"))
        self.user_input.setToolTip(_translate("SortingTechniques", "Enter space-separated input here..."))
        self.user_input.setPlaceholderText(_translate("SortingTechniques", "Input goes here..."))
        
    def setAlgo(self):
        #Also call function to set the description on the right side...
        if self.bubble_sort.isChecked():
            self.algo_selected.setText("Bubble Sort")
            self.label_7.setText("Bubble Sort")
            self.description.setPlainText("Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.\n\n"
                                          "=>Worst and Average Case Time Complexity: O(n²). Worst case occurs when array is reverse sorted.\n"
                                          "=>Best Case Time Complexity: O(n). Best case occurs when array is already sorted.\n"
                                          "=>Auxiliary Space: O(1)\n"
                                          "=>Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.\n"
                                          "=>Sorting In Place: Yes\n"
                                          "=>Stable: Yes\n"
                                          "\nDue to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.\n"
                                          "In computer graphics it is popular for its capability to detect a very small error (like swap of just two elements) in almost-sorted arrays and fix it with just linear complexity (2n).\n"
                                          "For example, it is used in a polygon filling algorithm, where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to x axis) and with incrementing y their order changes (two elements are swapped) only at intersections of two lines...")
            self.AlgoCheck = True
        if self.selection_sort.isChecked():
            self.algo_selected.setText("Selection Sort")
            self.label_7.setText("Selection Sort")
            self.description.setPlainText("The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.\n"
                                          "The algorithm maintains two subarrays in a given array:\n"
                                          "     1) The subarray which is already sorted.\n"
                                          "     2) Remaining subarray which is unsorted.\n\n"
                                          "=> Time Complexity: O(n²) as there are two nested loops.\n"
                                          "=> Auxiliary Space: O(1)\n"
                                          "=> Stability : The default implementation is not stable. However it can be made stable.\n"
                                          "=> In Place : Yes, it does not require extra space.\n\n"
                                          "The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.")
            self.AlgoCheck = True
        if self.insertion_sort.isChecked():
            self.algo_selected.setText("Insertion Sort")
            self.label_7.setText("Insertion Sort")
            self.description.setPlainText("Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.\n"
                                          "Algorithm:\n"
                                          "InsertionSort(arr,n)\n"
                                          "     Loop from i = 1 to n-1.\n"
                                          "     Pick element arr[i] and insert it into sorted sequence arr[0…i-1]\n\n"
                                          "=> Time Complexity: O(n²)\n"
                                          "=> Auxiliary Space: O(1)\n"
                                          "=> Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.\n"
                                          "=> Algorithmic Paradigm: Incremental Approach\n"
                                          "=> Sorting In Place: Yes\n"
                                          "=> Stable: Yes\n"
                                          "\nInsertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.")
            self.AlgoCheck = True
        if self.merge_sort.isChecked():
            self.algo_selected.setText("Merge Sort")
            self.label_7.setText("Merge Sort")
            self.description.setPlainText("Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.\n"
                                          "The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.\n"
                                          "Algorithm:\n"
                                          "MergeSort(arr[],l,r)\n"
                                          "     if r>l\n"
                                          "          1. Find the middle point to divide the array into two halves: \n\tmiddle m = (l+r)/2\n"
                                          "          2. Call mergeSort for first half:\n\tCall mergeSort(arr, l, m)\n"
                                          "          3. Call mergeSort for second half:\n\tCall mergeSort(arr, m+1, r)\n"
                                          "          4. Merge the two halves sorted in step 2 and 3:\n\tCall merge(arr, l, m, r)\n\n"
                                          "=> Time Complexity: Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. T(n) = 2T(n/2) + \u03F4(n)\n"
                                          "Time complexity of Merge Sort is \u03F4(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.\n"
                                          "=> Auxiliary Space: O(n)\n"
                                          "=> Algorithmic Paradigm: Divide and Conquer\n"
                                          "=> Sorting In Place: No in a typical implementation\n"
                                          "=> Stable: Yes\n"
                                          "\nApplications:\n"
                                          "     1) Merge Sort is useful for sorting linked lists in O(nLogn) time.\n"
                                          "     2) Inversion Count Problem\n"
                                          "     3) Used in External Sorting")
            self.AlgoCheck = True
        if self.quick_sort.isChecked():
            self.algo_selected.setText("Quick Sort")
            self.label_7.setText("Quick Sort")
            self.description.setPlainText("Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.\n"
                                          "There are many different versions of quickSort that pick pivot in different ways:\n"
                                          "     1. Always pick first element as pivot.\n"
                                          "     2. Always pick last element as pivot.\n"
                                          "     3. Pick a random element as pivot.\n"
                                          "     4. Pick median as pivot.\n\n"
                                          "The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.\n"
                                          "\nAlgorithm:\n"
                                          "QuickSort(arr[],low,high\n"
                                          "     if low<high\n"
                                          "          Partition Index (pi) = partition(arr, low, high)\n"
                                          "          quickSort(arr, low, pi - 1);  // Before pi\n"
                                          "          quickSort(arr, pi + 1, high); // After pi\n"
                                          "\nAnalysis of QuickSort:\n"
                                          "Time taken by QuickSort in general can be written as following:\n"
                                          "    T(n) = T(k) + T(n-k-1) + \u03F4(n)\n"
                                          "The first two terms are for two recursive calls, the last term is for the partition process. k is the number of elements which are smaller than pivot.\n"
                                          "The time taken by QuickSort depends upon the input array and partition strategy.\n"
                                          "*Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot.The complexity of QuickSort in worst case is \u03F4(n^2).\n"
                                          "*Best Case: The best case occurs when the partition process always picks the middle element as pivot. The complexity of QuickSort in best is \u03F4(nLogn).\n"
                                          "*Average Case: To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation. We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set and O(9n/10) elements in other set. The average case time-complexity of QuickSort is \u03F4(nLogn).\n"
                                          "\n=> Stable: The default implementation is not stable.\n"
                                          "=> In-place: As per the broad definition of in-place algorithm it qualifies as an in-place sorting algorithm as it uses extra space only for storing recursive function calls but not for manipulating the input.\n"
                                          "\n\nAlthough the worst case time complexity of QuickSort is O(n²) which is more than many other sorting algorithms like Merge Sort and Heap Sort, QuickSort is faster in practice, because its inner loop can be efficiently implemented on most architectures, and in most real-world data. QuickSort can be implemented in different ways by changing the choice of pivot, so that the worst case rarely occurs for a given type of data. However, merge sort is generally considered better when data is huge and stored in external storage.")
            self.AlgoCheck = True
        if self.heap_sort.isChecked():
            self.algo_selected.setText("Heap Sort")
            self.label_7.setText("Heap Sort")
            self.description.setPlainText("Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining element.\n"
                                          "Algorithm:\n"
                                          "     1) Build a max heap from the input data.(BUILD-HEAP)\n"
                                          "     2) At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, HEAPIFY the root of tree.\n"
                                          "     3) Repeat above steps while size of heap is greater than 1.\n\n"
                                          "=> Time Complexity: Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and overall time complexity of Heap Sort is O(nLogn).\n"
                                          "=> In-place: Heap sort is an in-place algorithm.\n"
                                          "=> Stable: Its typical implementation is not stable, but can be made stable.\n"
                                          "\nApllications:\n"
                                          "     1) Sort a nearly sorted (or K-sorted) array.\n"
                                          "     2) k largest (or smallest) elements in an array.\n"
                                          "Heap sort algorithm has limited uses because Quicksort and Mergesort are better in practice. Nevertheless, the Heap data structure itself is enormously used.")
            self.AlgoCheck = True
        if self.radix_sort.isChecked():
            self.algo_selected.setText("Radix Sort")
            self.label_7.setText("Radix Sort")
            self.description.setPlainText("The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.\n"
                                          "Algorithm:\n"
                                          "Do following for each digit i where i varies from least significant digit to the most significant digit:\n"
                                          "     Sort input array using counting sort (or any stable sort) according to the i’th digit.\n\n"
                                          "Running Time of Radix Sort\n"
                                          "------------  ------  --  -------  -----\n"
                                          "Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, for example, for decimal system, b is 10. If k is the maximum possible value, then d would be O(logb(k)). So overall time complexity is O((n+b) * logb(k)).\n"
                                          "If we limit k as k <= n^c, where c is a constant, the complexity becomes O(nLogb(n)).\n"
                                          "Finally, if we set b as n, we get the time complexity as O(n). In other words, we can sort an array of integers with range from 1 to nc if the numbers are represented in base n (or every digit takes log2(n) bits).\n"
                                          "\nIf we have log2n bits for every digit, the running time of Radix appears to be better than Quick Sort for a wide range of input numbers. The constant factors hidden in asymptotic notation are higher for Radix Sort.\n"
                                          "Also, Radix sort uses counting sort as a subroutine and counting sort takes extra space to sort numbers.")
            self.AlgoCheck = True
        if self.count_sort.isChecked():
            self.algo_selected.setText("Count Sort")
            self.label_7.setText("Count Sort")
            self.description.setPlainText("Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output list.\n"
                                          "Algorithm:\n"
                                          "CountSort(arr)"
                                          "     1. Create a count (key counting) array\n"
                                          "     2. for each element in input list\n"
                                          "           increase the respective counter by 1\n"
                                          "     3. for each key in count array\n"
                                          "           restore element to the list\n"
                                          "           decrease count by 1\n\n"
                                          "=> Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.\n"
                                          "=> Auxiliary Space: O(n+k)\n"
                                          "\nImportant Points:\n"
                                          "     1. Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted.\n"
                                          "     2. It is not a comparison based sorting. Its running time complexity is O(n) with space proportional to the range of data.\n"
                                          "     3. It is often used as a sub-routine to another sorting algorithm like radix sort.\n"
                                          "     4. Counting sort uses a partial hashing to count the occurrence of the data object in O(1).\n"
                                          "     5. Counting sort can be extended to work for negative inputs also.")
            self.AlgoCheck = True
        if self.bucket_sort.isChecked():
            self.algo_selected.setText("Bucket Sort")
            self.label_7.setText("Bucket Sort")
            self.description.setPlainText("Bucket sort is mainly useful when input is uniformly distributed over a range. For example, consider the following problem:\n"
                                          "\"Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range.\"\n"
                                          "Algorithm:\n"
                                          "BucketSort(arr,n)\n"
                                          "     1. Create n empty buckets.\n"
                                          "     2. Do following for every array element arr[i].\n"
                                          "         Insert arr[i] into bucket[n*array[i]]\n"
                                          "     3. Sort individual buckets using insertion sort.\n"
                                          "     4. Concatenate all sorted buckets.\n\n"
                                          "Complexity Analysis:\n"
                                          "=> Worst Case Complexity: O(n²)\n"
                                          "When there are elements of close range in the array, they are likely to be placed in the same bucket. This may result in some buckets having more number of elements than others.\n"
                                          "It makes the complexity depend on the sorting algorithm used to sort the elements of the bucket. The complexity becomes even worse when the elements are in reverse order.\n"
                                          "=> Best Case Complexity: O(n+k)\n"
                                          "It occurs when the elements are uniformly distributed in the buckets with a nearly equal number of elements in each bucket. The complexity becomes even better if the elements inside the buckets are already sorted.\n"
                                          "=> Average Case Complexity: O(n)\n"
                                          "It occurs when the elements are distributed randomly in the array. Even if the elements are not distributed uniformly, bucket sort runs in linear time. It holds true until the sum of the squares of the bucket sizes is linear in the total number of elements.\n\n"
                                          "Bucket sort is used when:\n"
                                          "     1. input is uniformly distributed over a range.\n"
                                          "     2. there are floating point values")
            self.AlgoCheck = True
    
    def getRandomInput(self):
        if not self.bucket_sort.isChecked():            
            self.size = random.randint(1,20)
            rand_input = []
            if self.ordr_asc.isChecked():
                i = random.randint(1,20)
                for _ in range(self.size):
                    rand_input.append(i)
                    i += random.randint(1,7)
                self.array = rand_input
            elif self.ordr_desc.isChecked():
                i = random.randint(200,300)
                for _ in range(self.size):
                    rand_input.append(i)
                    i -= random.randint(8,15)
                self.array = rand_input
            else:
                rand_input = random.sample(range(1,100),self.size)
                self.array = rand_input
        else:
            self.size = random.randint(1,20)
            rand_input = []
            for i in range(self.size):
                rand_input.append(random.uniform(0,1))
            if self.ordr_asc.isChecked():
                rand_input.sort()
            elif self.ordr_desc.isChecked():
                rand_input.sort()
                rand_input = rand_input[::-1]
            self.array = rand_input
        self.auto_gen_input.setPlainText(str(self.array))
    
    def input_method(self):
        if self.groupBox_3.isChecked() or self.groupBox_4.isChecked():
            self.inputCheck = True
        else:
            self.inputCheck = False
        if self.groupBox_3.isChecked():
            self.Input_method = "Auto Generated"
        elif self.groupBox_4.isChecked():
            self.Input_method = "User Input"
    
    def bubbleSort(self,arr,n):
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
    
    def selectionSort(self,arr,n):
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
    def insertionSort(self,arr,n):
        for i in range(1,n):
            key = arr[i]
            j = i-1
            while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
    
    def merge(self,left,right):
        if not len(left) or not len(right):
            return left or right
        result = []
        i,j = 0,0
        while len(result) < len(left)+len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
            if i == len(left) or j == len(right):
                result.extend(left[i:] or right[j:])
                break
        return result
    
    def mergeSort(self,arr):
        n = len(arr)
        if n<2:
            return arr
        middle = n//2
        left = self.mergeSort(arr[:middle])
        right = self.mergeSort(arr[middle:])
        return self.merge(left,right)
    
    def partition(self,arr,low,high):
        i = low-1
        pivot = arr[high]
        for j in range(low,high):
            if arr[j] < pivot:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    
    def quickSort(self,arr,low,high):
        if low < high:
            pi = self.partition(arr,low,high)
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)
    
    def heapify(self,arr,n,i):
        largest = i
        l = 2*i+1
        r = 2*i+2
        if l<n and arr[i] < arr[l]:
            largest = l
        if r<n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    def heapSort(self,arr,n):
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,0,-1):
            arr[i],arr[0] = arr[0],arr[i]
            self.heapify(arr,i,0)
    
    def sortRadix(self,arr,exp):
        n = len(arr)
        output = [0]*(n)
        counts = [0]*(10)
        for i in range(0,n):
            index = arr[i]//exp
            counts[index%10]+=1
        for i in range(1,10):
            counts[i] += counts[i-1]
        i = n-1
        while i>=0:
            index = arr[i]//exp
            output[counts[index%10]-1] = arr[i]
            counts[index%10]-=1
            i-=1
        i = 0
        for i in range(0,len(arr)):
            arr[i] = output[i]
    
    def radixSort(self,arr):
        maxM = max(arr)
        exp = 1
        while maxM//exp > 0:
            self.sortRadix(arr,exp)
            exp*=10
    
    def countSort(self,arr,n):
        output = [0]*n
        count = [0]*(max(arr)+1)
        for i in arr:
            count[i]+=1
        for i in range(1,len(count)):
            count[i] += count[i-1]
        for i in range(len(arr)):
            output[count[arr[i]]-1] = arr[i]
            count[arr[i]] -= 1
        return output
    
    def bucketSort(self,arr):
        ans = []
        slot_num = 10
        for i in range(slot_num):
            ans.append([])
        for j in arr:
            index_b = int(slot_num * j)
            ans[index_b].append(j)
        for i in range(slot_num):
            self.insertionSort(ans[i],len(ans[i]))
        k = 0
        for i in range(slot_num):
            for j in range(len(ans[i])):
                arr[k] = ans[i][j]
                k+=1
    
    def Execute(self):
        if self.AlgoCheck and self.inputCheck:
            self.Selected_algo = self.algo_selected.text()
            if self.Input_method=="User Input":
                self.size = int(self.input_size.text())
                if self.Selected_algo != "Bucket Sort":
                    self.array = list(map(int,self.user_input.toPlainText().split()))
            if self.Selected_algo == "Bubble Sort":
                self.bubbleSort(self.array,self.size)
                self.output_display.setText(str(self.array))
            elif self.Selected_algo == "Selection Sort":
                self.selectionSort(self.array,self.size)
                self.output_display.setText(str(self.array))
            elif self.Selected_algo == "Insertion Sort":
                self.insertionSort(self.array,self.size)
                self.output_display.setText(str(self.array))
            elif self.Selected_algo == "Merge Sort":
                self.output_display.setText(str(self.mergeSort(self.array)))
            elif self.Selected_algo == "Quick Sort":
                self.quickSort(self.array,0,self.size-1)
                self.output_display.setText(str(self.array))
            elif self.Selected_algo == "Heap Sort":
                self.heapSort(self.array,self.size)
                self.output_display.setText(str(self.array))
            elif self.Selected_algo == "Radix Sort":
                self.radixSort(self.array)
                self.output_display.setText(str(self.array))
            elif self.Selected_algo == "Count Sort":
                self.output_display.setText(str(self.countSort(self.array,self.size)))
            else:
                if self.Input_method == "User Input":
                    self.array = list(map(float,self.user_input.toPlainText().split()))
                    print('Works')                
                self.bucketSort(self.array)
                self.output_display.setText(str(self.array))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SortingTechniques = QtWidgets.QWidget()
    ui = Ui_SortingTechniques()
    ui.setupUi(SortingTechniques)
    SortingTechniques.show()
    sys.exit(app.exec_())

