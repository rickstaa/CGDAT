# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ricks\OneDrive\Development\Tools\CGDAT\scripts\..\qt\cgdat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../media/CGDAT.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(15, 15, 15, 0)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.additional_options_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.additional_options_groupbox.setFont(font)
        self.additional_options_groupbox.setObjectName("additional_options_groupbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.additional_options_groupbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.additional_options_layout = QtWidgets.QGridLayout()
        self.additional_options_layout.setObjectName("additional_options_layout")
        self.time_file_path = QtWidgets.QLineEdit(self.additional_options_groupbox)
        self.time_file_path.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_file_path.setFont(font)
        self.time_file_path.setReadOnly(True)
        self.time_file_path.setObjectName("time_file_path")
        self.additional_options_layout.addWidget(self.time_file_path, 0, 2, 1, 1)
        self.time_range_value = QtWidgets.QDoubleSpinBox(self.additional_options_groupbox)
        self.time_range_value.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_range_value.sizePolicy().hasHeightForWidth())
        self.time_range_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_range_value.setFont(font)
        self.time_range_value.setPrefix("")
        self.time_range_value.setMaximum(1000.0)
        self.time_range_value.setSingleStep(0.1)
        self.time_range_value.setObjectName("time_range_value")
        self.additional_options_layout.addWidget(self.time_range_value, 1, 2, 1, 1)
        self.player_filter_toggle = QtWidgets.QCheckBox(self.additional_options_groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.player_filter_toggle.setFont(font)
        self.player_filter_toggle.setText("")
        self.player_filter_toggle.setObjectName("player_filter_toggle")
        self.additional_options_layout.addWidget(self.player_filter_toggle, 2, 0, 1, 1)
        self.player_filter_label = QtWidgets.QLabel(self.additional_options_groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.player_filter_label.setFont(font)
        self.player_filter_label.setToolTip("")
        self.player_filter_label.setObjectName("player_filter_label")
        self.additional_options_layout.addWidget(self.player_filter_label, 2, 1, 1, 1)
        self.time_file_toggle = QtWidgets.QCheckBox(self.additional_options_groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_file_toggle.setFont(font)
        self.time_file_toggle.setStyleSheet("")
        self.time_file_toggle.setText("")
        self.time_file_toggle.setObjectName("time_file_toggle")
        self.additional_options_layout.addWidget(self.time_file_toggle, 0, 0, 1, 1)
        self.time_selection_file_label = QtWidgets.QLabel(self.additional_options_groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_selection_file_label.setFont(font)
        self.time_selection_file_label.setToolTip("")
        self.time_selection_file_label.setObjectName("time_selection_file_label")
        self.additional_options_layout.addWidget(self.time_selection_file_label, 0, 1, 1, 1)
        self.time_range_label = QtWidgets.QLabel(self.additional_options_groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_range_label.setFont(font)
        self.time_range_label.setToolTip("")
        self.time_range_label.setObjectName("time_range_label")
        self.additional_options_layout.addWidget(self.time_range_label, 1, 1, 1, 1)
        self.time_range_toggle = QtWidgets.QCheckBox(self.additional_options_groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_range_toggle.setFont(font)
        self.time_range_toggle.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.time_range_toggle.setText("")
        self.time_range_toggle.setObjectName("time_range_toggle")
        self.additional_options_layout.addWidget(self.time_range_toggle, 1, 0, 1, 1)
        self.time_file_browser_btn = QtWidgets.QToolButton(self.additional_options_groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_file_browser_btn.setFont(font)
        self.time_file_browser_btn.setObjectName("time_file_browser_btn")
        self.additional_options_layout.addWidget(self.time_file_browser_btn, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.additional_options_layout)
        self.gridLayout.addWidget(self.additional_options_groupbox, 2, 0, 1, 1)
        self.control_group_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_group_box.sizePolicy().hasHeightForWidth())
        self.control_group_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.control_group_box.setFont(font)
        self.control_group_box.setStyleSheet("QGroupBox{padding-top:0px; margin-top:0px}")
        self.control_group_box.setTitle("")
        self.control_group_box.setObjectName("control_group_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.control_group_box)
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.analyse_data_btn = QtWidgets.QPushButton(self.control_group_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.analyse_data_btn.setFont(font)
        self.analyse_data_btn.setObjectName("analyse_data_btn")
        self.horizontalLayout.addWidget(self.analyse_data_btn)
        self.reset_conditions_grid_btn = QtWidgets.QPushButton(self.control_group_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset_conditions_grid_btn.setFont(font)
        self.reset_conditions_grid_btn.setObjectName("reset_conditions_grid_btn")
        self.horizontalLayout.addWidget(self.reset_conditions_grid_btn)
        self.output_settings_btn = QtWidgets.QPushButton(self.control_group_box)
        self.output_settings_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../media/settings_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.output_settings_btn.setIcon(icon1)
        self.output_settings_btn.setObjectName("output_settings_btn")
        self.horizontalLayout.addWidget(self.output_settings_btn)
        self.gridLayout.addWidget(self.control_group_box, 4, 0, 1, 1)
        self.conditions_group_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conditions_group_box.sizePolicy().hasHeightForWidth())
        self.conditions_group_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.conditions_group_box.setFont(font)
        self.conditions_group_box.setStyleSheet("")
        self.conditions_group_box.setObjectName("conditions_group_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.conditions_group_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.conditions_group_box)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContent = QtWidgets.QWidget()
        self.scrollAreaContent.setGeometry(QtCore.QRect(0, 0, 750, 221))
        self.scrollAreaContent.setObjectName("scrollAreaContent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaContent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.conditions_grid = QtWidgets.QGridLayout()
        self.conditions_grid.setObjectName("conditions_grid")
        self.verticalLayout.addLayout(self.conditions_grid)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaContent)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.conditions_grid2 = QtWidgets.QGridLayout()
        self.conditions_grid2.setObjectName("conditions_grid2")
        self.verticalLayout_3.addLayout(self.conditions_grid2)
        self.gridLayout.addWidget(self.conditions_group_box, 3, 0, 1, 1)
        self.general_settings_group_box = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.general_settings_group_box.setFont(font)
        self.general_settings_group_box.setAutoFillBackground(False)
        self.general_settings_group_box.setObjectName("general_settings_group_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.general_settings_group_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.general_settings_layout = QtWidgets.QGridLayout()
        self.general_settings_layout.setObjectName("general_settings_layout")
        self.output_data_folder_label = QtWidgets.QLabel(self.general_settings_group_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_data_folder_label.setFont(font)
        self.output_data_folder_label.setToolTip("")
        self.output_data_folder_label.setObjectName("output_data_folder_label")
        self.general_settings_layout.addWidget(self.output_data_folder_label, 1, 0, 1, 1)
        self.input_data_label = QtWidgets.QLabel(self.general_settings_group_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_data_label.setFont(font)
        self.input_data_label.setToolTip("")
        self.input_data_label.setObjectName("input_data_label")
        self.general_settings_layout.addWidget(self.input_data_label, 0, 0, 1, 1)
        self.output_file_path = QtWidgets.QLineEdit(self.general_settings_group_box)
        self.output_file_path.setEnabled(False)
        self.output_file_path.setText("")
        self.output_file_path.setReadOnly(True)
        self.output_file_path.setObjectName("output_file_path")
        self.general_settings_layout.addWidget(self.output_file_path, 1, 2, 1, 1)
        self.input_file_browser_btn = QtWidgets.QToolButton(self.general_settings_group_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_file_browser_btn.setFont(font)
        self.input_file_browser_btn.setObjectName("input_file_browser_btn")
        self.general_settings_layout.addWidget(self.input_file_browser_btn, 0, 3, 1, 1)
        self.output_file_browser_btn = QtWidgets.QToolButton(self.general_settings_group_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_file_browser_btn.setFont(font)
        self.output_file_browser_btn.setObjectName("output_file_browser_btn")
        self.general_settings_layout.addWidget(self.output_file_browser_btn, 1, 3, 1, 1)
        self.input_file_path = QtWidgets.QLineEdit(self.general_settings_group_box)
        self.input_file_path.setEnabled(False)
        self.input_file_path.setText("")
        self.input_file_path.setReadOnly(True)
        self.input_file_path.setObjectName("input_file_path")
        self.general_settings_layout.addWidget(self.input_file_path, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.general_settings_layout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.general_settings_group_box, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../media/about_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../media/docs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDocumentation.setIcon(icon3)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.menuFile.addAction(self.actionDocumentation)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CGDAT"))
        self.additional_options_groupbox.setTitle(_translate("MainWindow", "Additional options"))
        self.time_file_path.setToolTip(_translate("MainWindow", "<html><head/><body><p>Here you have the possibility to add a file containing time points at which you want to analyse the data.</p></body></html>"))
        self.time_range_value.setToolTip(_translate("MainWindow", "<html><head/><body><p>Here you define how many seconds you want to include in your analysis before and after a given condition is met.</p></body></html>"))
        self.time_range_value.setSuffix(_translate("MainWindow", " [s]"))
        self.player_filter_label.setText(_translate("MainWindow", "Filter by player"))
        self.time_selection_file_label.setText(_translate("MainWindow", "Use time section file"))
        self.time_range_label.setText(_translate("MainWindow", "Add time borders"))
        self.time_file_browser_btn.setText(_translate("MainWindow", "..."))
        self.analyse_data_btn.setToolTip(_translate("MainWindow", "Start data analysis."))
        self.analyse_data_btn.setText(_translate("MainWindow", "Analyse Data"))
        self.reset_conditions_grid_btn.setToolTip(_translate("MainWindow", "Reset conditions."))
        self.reset_conditions_grid_btn.setText(_translate("MainWindow", "Reset conditions"))
        self.output_settings_btn.setToolTip(_translate("MainWindow", "Additional result output file options."))
        self.conditions_group_box.setTitle(_translate("MainWindow", "Conditions"))
        self.general_settings_group_box.setTitle(_translate("MainWindow", "Settings"))
        self.output_data_folder_label.setText(_translate("MainWindow", "Results output folder"))
        self.input_data_label.setText(_translate("MainWindow", "Input data file"))
        self.output_file_path.setToolTip(_translate("MainWindow", "<html><head/><body><p>Here you define the output location of the file containing the data analysis.</p></body></html>"))
        self.input_file_browser_btn.setText(_translate("MainWindow", "..."))
        self.output_file_browser_btn.setText(_translate("MainWindow", "..."))
        self.input_file_path.setToolTip(_translate("MainWindow", "<html><head/><body><p>Here you define the data file you want to analyse.</p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "F1"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionDocumentation.setShortcut(_translate("MainWindow", "F2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

