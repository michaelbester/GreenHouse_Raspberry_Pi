# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setWindowModality(Qt.WindowModality.NonModal)
        Widget.resize(1789, 953)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setWindowOpacity(1.000000000000000)
        Widget.setToolTipDuration(2000)
        Widget.setAutoFillBackground(False)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 70, 821, 766))
        self.verticalLayout_1 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.status_label = QLabel(self.verticalLayoutWidget)
        self.status_label.setObjectName(u"status_label")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        self.status_label.setFont(font)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_1.addWidget(self.status_label)

        self.status_gridLayout = QGridLayout()
        self.status_gridLayout.setObjectName(u"status_gridLayout")
        self.inside_temp_label = QLabel(self.verticalLayoutWidget)
        self.inside_temp_label.setObjectName(u"inside_temp_label")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(20)
        self.inside_temp_label.setFont(font1)

        self.status_gridLayout.addWidget(self.inside_temp_label, 1, 0, 1, 1)

        self.inside_temp_val_label = QLabel(self.verticalLayoutWidget)
        self.inside_temp_val_label.setObjectName(u"inside_temp_val_label")
        self.inside_temp_val_label.setFont(font1)
        self.inside_temp_val_label.setToolTipDuration(2000)
        self.inside_temp_val_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_gridLayout.addWidget(self.inside_temp_val_label, 1, 2, 1, 1)

        self.outside_temp_label = QLabel(self.verticalLayoutWidget)
        self.outside_temp_label.setObjectName(u"outside_temp_label")
        self.outside_temp_label.setFont(font1)

        self.status_gridLayout.addWidget(self.outside_temp_label, 0, 0, 1, 1)

        self.water_zone_2_val_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_2_val_label.setObjectName(u"water_zone_2_val_label")
        self.water_zone_2_val_label.setFont(font1)
        self.water_zone_2_val_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_gridLayout.addWidget(self.water_zone_2_val_label, 3, 2, 1, 1)

        self.water_zone_1_val_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_1_val_label.setObjectName(u"water_zone_1_val_label")
        self.water_zone_1_val_label.setFont(font1)
        self.water_zone_1_val_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_gridLayout.addWidget(self.water_zone_1_val_label, 2, 2, 1, 1)

        self.outside_temp_val_label = QLabel(self.verticalLayoutWidget)
        self.outside_temp_val_label.setObjectName(u"outside_temp_val_label")
        self.outside_temp_val_label.setFont(font1)
        self.outside_temp_val_label.setToolTipDuration(2000)
        self.outside_temp_val_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_gridLayout.addWidget(self.outside_temp_val_label, 0, 2, 1, 1)

        self.fan_temp_setting_label = QLabel(self.verticalLayoutWidget)
        self.fan_temp_setting_label.setObjectName(u"fan_temp_setting_label")
        self.fan_temp_setting_label.setFont(font1)
        self.fan_temp_setting_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_gridLayout.addWidget(self.fan_temp_setting_label, 5, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.status_gridLayout.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.fan_setting_label = QLabel(self.verticalLayoutWidget)
        self.fan_setting_label.setObjectName(u"fan_setting_label")
        self.fan_setting_label.setFont(font1)

        self.status_gridLayout.addWidget(self.fan_setting_label, 5, 0, 1, 1)

        self.water_zone_1_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_1_label.setObjectName(u"water_zone_1_label")
        self.water_zone_1_label.setFont(font1)

        self.status_gridLayout.addWidget(self.water_zone_1_label, 2, 0, 1, 1)

        self.fan_status_on_off = QLabel(self.verticalLayoutWidget)
        self.fan_status_on_off.setObjectName(u"fan_status_on_off")
        self.fan_status_on_off.setFont(font1)
        self.fan_status_on_off.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_gridLayout.addWidget(self.fan_status_on_off, 4, 2, 1, 1)

        self.water_zone_2_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_2_label.setObjectName(u"water_zone_2_label")
        self.water_zone_2_label.setFont(font1)

        self.status_gridLayout.addWidget(self.water_zone_2_label, 3, 0, 1, 1)

        self.fan_status_label = QLabel(self.verticalLayoutWidget)
        self.fan_status_label.setObjectName(u"fan_status_label")
        self.fan_status_label.setFont(font1)

        self.status_gridLayout.addWidget(self.fan_status_label, 4, 0, 1, 1)


        self.verticalLayout_1.addLayout(self.status_gridLayout)

        self.controls_label = QLabel(self.verticalLayoutWidget)
        self.controls_label.setObjectName(u"controls_label")
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(30)
        font2.setBold(True)
        self.controls_label.setFont(font2)
        self.controls_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_1.addWidget(self.controls_label)

        self.controls_gridLayout = QGridLayout()
        self.controls_gridLayout.setObjectName(u"controls_gridLayout")
        self.water_zone_1_control_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_1_control_label.setObjectName(u"water_zone_1_control_label")
        self.water_zone_1_control_label.setFont(font1)

        self.controls_gridLayout.addWidget(self.water_zone_1_control_label, 0, 0, 1, 1)

        self.water_zone_1_control_pushButton = QPushButton(self.verticalLayoutWidget)
        self.water_zone_1_control_pushButton.setObjectName(u"water_zone_1_control_pushButton")
        self.water_zone_1_control_pushButton.setMaximumSize(QSize(120, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        self.water_zone_1_control_pushButton.setFont(font3)

        self.controls_gridLayout.addWidget(self.water_zone_1_control_pushButton, 0, 2, 1, 1)

        self.water_zone_2_control_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_2_control_label.setObjectName(u"water_zone_2_control_label")
        self.water_zone_2_control_label.setFont(font1)

        self.controls_gridLayout.addWidget(self.water_zone_2_control_label, 1, 0, 1, 1)

        self.fan_control_label = QLabel(self.verticalLayoutWidget)
        self.fan_control_label.setObjectName(u"fan_control_label")
        self.fan_control_label.setFont(font1)

        self.controls_gridLayout.addWidget(self.fan_control_label, 2, 0, 1, 1)

        self.water_zone_2_control_pushButton = QPushButton(self.verticalLayoutWidget)
        self.water_zone_2_control_pushButton.setObjectName(u"water_zone_2_control_pushButton")
        self.water_zone_2_control_pushButton.setFont(font3)

        self.controls_gridLayout.addWidget(self.water_zone_2_control_pushButton, 1, 2, 1, 1)

        self.fan_control_pushButton = QPushButton(self.verticalLayoutWidget)
        self.fan_control_pushButton.setObjectName(u"fan_control_pushButton")
        self.fan_control_pushButton.setFont(font3)

        self.controls_gridLayout.addWidget(self.fan_control_pushButton, 2, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.controls_gridLayout.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)


        self.verticalLayout_1.addLayout(self.controls_gridLayout)

        self.verticalSpacer_2 = QSpacerItem(2, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_1.addItem(self.verticalSpacer_2)

        self.schedule_1_label = QLabel(self.verticalLayoutWidget)
        self.schedule_1_label.setObjectName(u"schedule_1_label")
        self.schedule_1_label.setFont(font2)
        self.schedule_1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_1.addWidget(self.schedule_1_label)

        self.schedule_1_gridLayout = QGridLayout()
        self.schedule_1_gridLayout.setObjectName(u"schedule_1_gridLayout")
        self.wednesday_schedule_label = QLabel(self.verticalLayoutWidget)
        self.wednesday_schedule_label.setObjectName(u"wednesday_schedule_label")
        self.wednesday_schedule_label.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.wednesday_schedule_label, 4, 0, 1, 1)

        self.friday_enable_1_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.friday_enable_1_checkbox.setObjectName(u"friday_enable_1_checkbox")
        self.friday_enable_1_checkbox.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.friday_enable_1_checkbox, 6, 6, 1, 1)

        self.tuesday_enable_1_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.tuesday_enable_1_checkbox.setObjectName(u"tuesday_enable_1_checkbox")
        self.tuesday_enable_1_checkbox.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.tuesday_enable_1_checkbox, 2, 6, 1, 1)

        self.thursday_schedule_label = QLabel(self.verticalLayoutWidget)
        self.thursday_schedule_label.setObjectName(u"thursday_schedule_label")
        self.thursday_schedule_label.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.thursday_schedule_label, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.schedule_1_gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.monday_schedule_label = QLabel(self.verticalLayoutWidget)
        self.monday_schedule_label.setObjectName(u"monday_schedule_label")
        self.monday_schedule_label.setMaximumSize(QSize(130, 16777215))
        self.monday_schedule_label.setFont(font1)
        self.monday_schedule_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.schedule_1_gridLayout.addWidget(self.monday_schedule_label, 0, 0, 1, 1)

        self.sunday_duration_1_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.sunday_duration_1_spinBox.setObjectName(u"sunday_duration_1_spinBox")
        self.sunday_duration_1_spinBox.setFont(font1)
        self.sunday_duration_1_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sunday_duration_1_spinBox.setMinimum(1)
        self.sunday_duration_1_spinBox.setMaximum(60)

        self.schedule_1_gridLayout.addWidget(self.sunday_duration_1_spinBox, 8, 4, 1, 1)

        self.tuesday_schedule_label = QLabel(self.verticalLayoutWidget)
        self.tuesday_schedule_label.setObjectName(u"tuesday_schedule_label")
        self.tuesday_schedule_label.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.tuesday_schedule_label, 2, 0, 1, 1)

        self.monday_enable_1_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.monday_enable_1_checkbox.setObjectName(u"monday_enable_1_checkbox")
        self.monday_enable_1_checkbox.setMaximumSize(QSize(200, 16777215))
        self.monday_enable_1_checkbox.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.monday_enable_1_checkbox, 0, 6, 1, 1)

        self.tuesday_timeEdit = QTimeEdit(self.verticalLayoutWidget)
        self.tuesday_timeEdit.setObjectName(u"tuesday_timeEdit")
        self.tuesday_timeEdit.setMaximumSize(QSize(110, 16777215))
        self.tuesday_timeEdit.setFont(font1)
        self.tuesday_timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout.addWidget(self.tuesday_timeEdit, 2, 2, 1, 1)

        self.friday_duration_1_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.friday_duration_1_spinBox.setObjectName(u"friday_duration_1_spinBox")
        self.friday_duration_1_spinBox.setFont(font1)
        self.friday_duration_1_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.friday_duration_1_spinBox.setMinimum(1)
        self.friday_duration_1_spinBox.setMaximum(60)

        self.schedule_1_gridLayout.addWidget(self.friday_duration_1_spinBox, 6, 4, 1, 1)

        self.sunday_timeEdit = QTimeEdit(self.verticalLayoutWidget)
        self.sunday_timeEdit.setObjectName(u"sunday_timeEdit")
        self.sunday_timeEdit.setFont(font1)
        self.sunday_timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout.addWidget(self.sunday_timeEdit, 8, 2, 1, 1)

        self.thursday_enable_1_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.thursday_enable_1_checkbox.setObjectName(u"thursday_enable_1_checkbox")
        self.thursday_enable_1_checkbox.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.thursday_enable_1_checkbox, 5, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.schedule_1_gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.saturday_enable_1_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.saturday_enable_1_checkbox.setObjectName(u"saturday_enable_1_checkbox")
        self.saturday_enable_1_checkbox.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.saturday_enable_1_checkbox, 7, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(70, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.schedule_1_gridLayout.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)

        self.thursday_duration_1_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.thursday_duration_1_spinBox.setObjectName(u"thursday_duration_1_spinBox")
        self.thursday_duration_1_spinBox.setFont(font1)
        self.thursday_duration_1_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thursday_duration_1_spinBox.setMinimum(1)
        self.thursday_duration_1_spinBox.setMaximum(60)

        self.schedule_1_gridLayout.addWidget(self.thursday_duration_1_spinBox, 5, 4, 1, 1)

        self.wednesday_duration_1_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.wednesday_duration_1_spinBox.setObjectName(u"wednesday_duration_1_spinBox")
        self.wednesday_duration_1_spinBox.setFont(font1)
        self.wednesday_duration_1_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wednesday_duration_1_spinBox.setMinimum(1)
        self.wednesday_duration_1_spinBox.setMaximum(60)

        self.schedule_1_gridLayout.addWidget(self.wednesday_duration_1_spinBox, 4, 4, 1, 1)

        self.monday_timeEdit = QTimeEdit(self.verticalLayoutWidget)
        self.monday_timeEdit.setObjectName(u"monday_timeEdit")
        self.monday_timeEdit.setMaximumSize(QSize(110, 16777215))
        self.monday_timeEdit.setFont(font1)
        self.monday_timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout.addWidget(self.monday_timeEdit, 0, 2, 1, 1)

        self.saturday_duration_1_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.saturday_duration_1_spinBox.setObjectName(u"saturday_duration_1_spinBox")
        self.saturday_duration_1_spinBox.setFont(font1)
        self.saturday_duration_1_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.saturday_duration_1_spinBox.setMinimum(1)
        self.saturday_duration_1_spinBox.setMaximum(60)

        self.schedule_1_gridLayout.addWidget(self.saturday_duration_1_spinBox, 7, 4, 1, 1)

        self.wednesday_enable_1_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.wednesday_enable_1_checkbox.setObjectName(u"wednesday_enable_1_checkbox")
        self.wednesday_enable_1_checkbox.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.wednesday_enable_1_checkbox, 4, 6, 1, 1)

        self.friday_timeEdit = QTimeEdit(self.verticalLayoutWidget)
        self.friday_timeEdit.setObjectName(u"friday_timeEdit")
        self.friday_timeEdit.setFont(font1)
        self.friday_timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout.addWidget(self.friday_timeEdit, 6, 2, 1, 1)

        self.friday_schedule_label = QLabel(self.verticalLayoutWidget)
        self.friday_schedule_label.setObjectName(u"friday_schedule_label")
        self.friday_schedule_label.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.friday_schedule_label, 6, 0, 1, 1)

        self.thursday_timeEdit = QTimeEdit(self.verticalLayoutWidget)
        self.thursday_timeEdit.setObjectName(u"thursday_timeEdit")
        self.thursday_timeEdit.setFont(font1)
        self.thursday_timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout.addWidget(self.thursday_timeEdit, 5, 2, 1, 1)

        self.tuesday_duration_1_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.tuesday_duration_1_spinBox.setObjectName(u"tuesday_duration_1_spinBox")
        self.tuesday_duration_1_spinBox.setFont(font1)
        self.tuesday_duration_1_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tuesday_duration_1_spinBox.setMinimum(1)
        self.tuesday_duration_1_spinBox.setMaximum(60)

        self.schedule_1_gridLayout.addWidget(self.tuesday_duration_1_spinBox, 2, 4, 1, 1)

        self.sunday_enable_1_checkbox = QCheckBox(self.verticalLayoutWidget)
        self.sunday_enable_1_checkbox.setObjectName(u"sunday_enable_1_checkbox")
        self.sunday_enable_1_checkbox.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.sunday_enable_1_checkbox, 8, 6, 1, 1)

        self.sunday_schedule_label = QLabel(self.verticalLayoutWidget)
        self.sunday_schedule_label.setObjectName(u"sunday_schedule_label")
        self.sunday_schedule_label.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.sunday_schedule_label, 8, 0, 1, 1)

        self.wednesday_timeEdit = QTimeEdit(self.verticalLayoutWidget)
        self.wednesday_timeEdit.setObjectName(u"wednesday_timeEdit")
        self.wednesday_timeEdit.setFont(font1)
        self.wednesday_timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout.addWidget(self.wednesday_timeEdit, 4, 2, 1, 1)

        self.saturday_schedule_label = QLabel(self.verticalLayoutWidget)
        self.saturday_schedule_label.setObjectName(u"saturday_schedule_label")
        self.saturday_schedule_label.setFont(font1)

        self.schedule_1_gridLayout.addWidget(self.saturday_schedule_label, 7, 0, 1, 1)

        self.saturday_timeEdit = QTimeEdit(self.verticalLayoutWidget)
        self.saturday_timeEdit.setObjectName(u"saturday_timeEdit")
        self.saturday_timeEdit.setFont(font1)
        self.saturday_timeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout.addWidget(self.saturday_timeEdit, 7, 2, 1, 1)

        self.monday_duration_1_spinBox = QSpinBox(self.verticalLayoutWidget)
        self.monday_duration_1_spinBox.setObjectName(u"monday_duration_1_spinBox")
        self.monday_duration_1_spinBox.setMinimumSize(QSize(80, 0))
        self.monday_duration_1_spinBox.setMaximumSize(QSize(80, 16777215))
        self.monday_duration_1_spinBox.setFont(font1)
        self.monday_duration_1_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.monday_duration_1_spinBox.setMinimum(1)
        self.monday_duration_1_spinBox.setMaximum(60)

        self.schedule_1_gridLayout.addWidget(self.monday_duration_1_spinBox, 0, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.schedule_1_gridLayout.addItem(self.horizontalSpacer_9, 0, 7, 1, 1)


        self.verticalLayout_1.addLayout(self.schedule_1_gridLayout)

        self.verticalLayoutWidget_2 = QWidget(Widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(850, 70, 921, 761))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.temp_chart_label = QLabel(self.verticalLayoutWidget_2)
        self.temp_chart_label.setObjectName(u"temp_chart_label")
        self.temp_chart_label.setMaximumSize(QSize(930, 16777215))
        self.temp_chart_label.setFont(font2)
        self.temp_chart_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.temp_chart_label)

        self.graphicsView = QGraphicsView(self.verticalLayoutWidget_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMaximumSize(QSize(900, 1000))

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.schedule_2_label = QLabel(self.verticalLayoutWidget_2)
        self.schedule_2_label.setObjectName(u"schedule_2_label")
        self.schedule_2_label.setFont(font2)
        self.schedule_2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.schedule_2_label)

        self.schedule_1_gridLayout_2 = QGridLayout()
        self.schedule_1_gridLayout_2.setObjectName(u"schedule_1_gridLayout_2")
        self.saturday_enable_2_checkbox = QCheckBox(self.verticalLayoutWidget_2)
        self.saturday_enable_2_checkbox.setObjectName(u"saturday_enable_2_checkbox")
        self.saturday_enable_2_checkbox.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.saturday_enable_2_checkbox, 7, 6, 1, 1)

        self.thursday_schedule_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.thursday_schedule_label_2.setObjectName(u"thursday_schedule_label_2")
        self.thursday_schedule_label_2.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.thursday_schedule_label_2, 5, 0, 1, 1)

        self.saturday_timeEdit_2 = QTimeEdit(self.verticalLayoutWidget_2)
        self.saturday_timeEdit_2.setObjectName(u"saturday_timeEdit_2")
        self.saturday_timeEdit_2.setFont(font1)
        self.saturday_timeEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout_2.addWidget(self.saturday_timeEdit_2, 7, 2, 1, 1)

        self.friday_timeEdit_2 = QTimeEdit(self.verticalLayoutWidget_2)
        self.friday_timeEdit_2.setObjectName(u"friday_timeEdit_2")
        self.friday_timeEdit_2.setFont(font1)
        self.friday_timeEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout_2.addWidget(self.friday_timeEdit_2, 6, 2, 1, 1)

        self.sunday_timeEdit_2 = QTimeEdit(self.verticalLayoutWidget_2)
        self.sunday_timeEdit_2.setObjectName(u"sunday_timeEdit_2")
        self.sunday_timeEdit_2.setFont(font1)
        self.sunday_timeEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout_2.addWidget(self.sunday_timeEdit_2, 8, 2, 1, 1)

        self.wednesday_duration_2_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.wednesday_duration_2_spinBox.setObjectName(u"wednesday_duration_2_spinBox")
        self.wednesday_duration_2_spinBox.setFont(font1)
        self.wednesday_duration_2_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wednesday_duration_2_spinBox.setMinimum(1)
        self.wednesday_duration_2_spinBox.setMaximum(60)

        self.schedule_1_gridLayout_2.addWidget(self.wednesday_duration_2_spinBox, 4, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.schedule_1_gridLayout_2.addItem(self.horizontalSpacer_7, 1, 3, 1, 1)

        self.wednesday_enable_2_checkbox = QCheckBox(self.verticalLayoutWidget_2)
        self.wednesday_enable_2_checkbox.setObjectName(u"wednesday_enable_2_checkbox")
        self.wednesday_enable_2_checkbox.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.wednesday_enable_2_checkbox, 4, 6, 1, 1)

        self.thursday_enable_2_checkbox = QCheckBox(self.verticalLayoutWidget_2)
        self.thursday_enable_2_checkbox.setObjectName(u"thursday_enable_2_checkbox")
        self.thursday_enable_2_checkbox.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.thursday_enable_2_checkbox, 5, 6, 1, 1)

        self.saturday_duration_2_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.saturday_duration_2_spinBox.setObjectName(u"saturday_duration_2_spinBox")
        self.saturday_duration_2_spinBox.setFont(font1)
        self.saturday_duration_2_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.saturday_duration_2_spinBox.setMinimum(1)
        self.saturday_duration_2_spinBox.setMaximum(60)

        self.schedule_1_gridLayout_2.addWidget(self.saturday_duration_2_spinBox, 7, 4, 1, 1)

        self.monday_duration_2_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.monday_duration_2_spinBox.setObjectName(u"monday_duration_2_spinBox")
        self.monday_duration_2_spinBox.setMinimumSize(QSize(80, 0))
        self.monday_duration_2_spinBox.setMaximumSize(QSize(80, 16777215))
        self.monday_duration_2_spinBox.setFont(font1)
        self.monday_duration_2_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.monday_duration_2_spinBox.setMinimum(1)
        self.monday_duration_2_spinBox.setMaximum(60)

        self.schedule_1_gridLayout_2.addWidget(self.monday_duration_2_spinBox, 1, 4, 1, 1)

        self.monday_enable_2_checkbox = QCheckBox(self.verticalLayoutWidget_2)
        self.monday_enable_2_checkbox.setObjectName(u"monday_enable_2_checkbox")
        self.monday_enable_2_checkbox.setMaximumSize(QSize(200, 16777215))
        self.monday_enable_2_checkbox.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.monday_enable_2_checkbox, 1, 6, 1, 1)

        self.tuesday_timeEdit_2 = QTimeEdit(self.verticalLayoutWidget_2)
        self.tuesday_timeEdit_2.setObjectName(u"tuesday_timeEdit_2")
        self.tuesday_timeEdit_2.setMaximumSize(QSize(110, 16777215))
        self.tuesday_timeEdit_2.setFont(font1)
        self.tuesday_timeEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout_2.addWidget(self.tuesday_timeEdit_2, 3, 2, 1, 1)

        self.tuesday_duration_2_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.tuesday_duration_2_spinBox.setObjectName(u"tuesday_duration_2_spinBox")
        self.tuesday_duration_2_spinBox.setFont(font1)
        self.tuesday_duration_2_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tuesday_duration_2_spinBox.setMinimum(1)
        self.tuesday_duration_2_spinBox.setMaximum(60)

        self.schedule_1_gridLayout_2.addWidget(self.tuesday_duration_2_spinBox, 3, 4, 1, 1)

        self.tuesday_schedule_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.tuesday_schedule_label_2.setObjectName(u"tuesday_schedule_label_2")
        self.tuesday_schedule_label_2.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.tuesday_schedule_label_2, 3, 0, 1, 1)

        self.thursday_timeEdit_2 = QTimeEdit(self.verticalLayoutWidget_2)
        self.thursday_timeEdit_2.setObjectName(u"thursday_timeEdit_2")
        self.thursday_timeEdit_2.setFont(font1)
        self.thursday_timeEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout_2.addWidget(self.thursday_timeEdit_2, 5, 2, 1, 1)

        self.monday_schedule_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.monday_schedule_label_2.setObjectName(u"monday_schedule_label_2")
        self.monday_schedule_label_2.setMaximumSize(QSize(130, 16777215))
        self.monday_schedule_label_2.setFont(font1)
        self.monday_schedule_label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.schedule_1_gridLayout_2.addWidget(self.monday_schedule_label_2, 1, 0, 1, 1)

        self.friday_duration_2_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.friday_duration_2_spinBox.setObjectName(u"friday_duration_2_spinBox")
        self.friday_duration_2_spinBox.setFont(font1)
        self.friday_duration_2_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.friday_duration_2_spinBox.setMinimum(1)
        self.friday_duration_2_spinBox.setMaximum(60)

        self.schedule_1_gridLayout_2.addWidget(self.friday_duration_2_spinBox, 6, 4, 1, 1)

        self.wednesday_timeEdit_2 = QTimeEdit(self.verticalLayoutWidget_2)
        self.wednesday_timeEdit_2.setObjectName(u"wednesday_timeEdit_2")
        self.wednesday_timeEdit_2.setFont(font1)
        self.wednesday_timeEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout_2.addWidget(self.wednesday_timeEdit_2, 4, 2, 1, 1)

        self.thursday_duration_2_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.thursday_duration_2_spinBox.setObjectName(u"thursday_duration_2_spinBox")
        self.thursday_duration_2_spinBox.setFont(font1)
        self.thursday_duration_2_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thursday_duration_2_spinBox.setMinimum(1)
        self.thursday_duration_2_spinBox.setMaximum(60)

        self.schedule_1_gridLayout_2.addWidget(self.thursday_duration_2_spinBox, 5, 4, 1, 1)

        self.sunday_duration_2_spinBox = QSpinBox(self.verticalLayoutWidget_2)
        self.sunday_duration_2_spinBox.setObjectName(u"sunday_duration_2_spinBox")
        self.sunday_duration_2_spinBox.setFont(font1)
        self.sunday_duration_2_spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sunday_duration_2_spinBox.setMinimum(1)
        self.sunday_duration_2_spinBox.setMaximum(60)

        self.schedule_1_gridLayout_2.addWidget(self.sunday_duration_2_spinBox, 8, 4, 1, 1)

        self.friday_schedule_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.friday_schedule_label_2.setObjectName(u"friday_schedule_label_2")
        self.friday_schedule_label_2.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.friday_schedule_label_2, 6, 0, 1, 1)

        self.sunday_schedule_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.sunday_schedule_label_2.setObjectName(u"sunday_schedule_label_2")
        self.sunday_schedule_label_2.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.sunday_schedule_label_2, 8, 0, 1, 1)

        self.sunday_enable_2_checkbox = QCheckBox(self.verticalLayoutWidget_2)
        self.sunday_enable_2_checkbox.setObjectName(u"sunday_enable_2_checkbox")
        self.sunday_enable_2_checkbox.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.sunday_enable_2_checkbox, 8, 6, 1, 1)

        self.wednesday_schedule_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.wednesday_schedule_label_2.setObjectName(u"wednesday_schedule_label_2")
        self.wednesday_schedule_label_2.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.wednesday_schedule_label_2, 4, 0, 1, 1)

        self.tuesday_enable_2_checkbox = QCheckBox(self.verticalLayoutWidget_2)
        self.tuesday_enable_2_checkbox.setObjectName(u"tuesday_enable_2_checkbox")
        self.tuesday_enable_2_checkbox.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.tuesday_enable_2_checkbox, 3, 6, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.schedule_1_gridLayout_2.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

        self.friday_enable_2_checkbox = QCheckBox(self.verticalLayoutWidget_2)
        self.friday_enable_2_checkbox.setObjectName(u"friday_enable_2_checkbox")
        self.friday_enable_2_checkbox.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.friday_enable_2_checkbox, 6, 6, 1, 1)

        self.monday_timeEdit_2 = QTimeEdit(self.verticalLayoutWidget_2)
        self.monday_timeEdit_2.setObjectName(u"monday_timeEdit_2")
        self.monday_timeEdit_2.setMaximumSize(QSize(110, 16777215))
        self.monday_timeEdit_2.setFont(font1)
        self.monday_timeEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.schedule_1_gridLayout_2.addWidget(self.monday_timeEdit_2, 1, 2, 1, 1)

        self.saturday_schedule_label_2 = QLabel(self.verticalLayoutWidget_2)
        self.saturday_schedule_label_2.setObjectName(u"saturday_schedule_label_2")
        self.saturday_schedule_label_2.setFont(font1)

        self.schedule_1_gridLayout_2.addWidget(self.saturday_schedule_label_2, 7, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.schedule_1_gridLayout_2.addItem(self.horizontalSpacer_8, 1, 5, 1, 1)


        self.verticalLayout_2.addLayout(self.schedule_1_gridLayout_2)

        self.title_label = QLabel(Widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(10, 0, 1771, 61))
        font4 = QFont()
        font4.setFamilies([u"Tahoma"])
        font4.setPointSize(50)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(True)
        self.title_label.setFont(font4)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 840, 1751, 100))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(325, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.save_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_pushButton.sizePolicy().hasHeightForWidth())
        self.save_pushButton.setSizePolicy(sizePolicy1)
        self.save_pushButton.setMinimumSize(QSize(200, 80))

        self.horizontalLayout.addWidget(self.save_pushButton)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.reset_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.reset_pushButton.setObjectName(u"reset_pushButton")
        sizePolicy1.setHeightForWidth(self.reset_pushButton.sizePolicy().hasHeightForWidth())
        self.reset_pushButton.setSizePolicy(sizePolicy1)
        self.reset_pushButton.setMinimumSize(QSize(200, 80))

        self.horizontalLayout.addWidget(self.reset_pushButton)

        self.horizontalSpacer_12 = QSpacerItem(425, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_12)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"GREEN HOUSE", None))
        self.status_label.setText(QCoreApplication.translate("Widget", u"STATUS", None))
        self.inside_temp_label.setText(QCoreApplication.translate("Widget", u"INSIDE TEMPERATURE:", None))
#if QT_CONFIG(tooltip)
        self.inside_temp_val_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inside_temp_val_label.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.inside_temp_val_label.setText(QCoreApplication.translate("Widget", u"75F", None))
        self.outside_temp_label.setText(QCoreApplication.translate("Widget", u"OUTSIDE TEMPERATURE:", None))
        self.water_zone_2_val_label.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.water_zone_1_val_label.setText(QCoreApplication.translate("Widget", u"OFF", None))
#if QT_CONFIG(tooltip)
        self.outside_temp_val_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.outside_temp_val_label.setText(QCoreApplication.translate("Widget", u"56F", None))
        self.fan_temp_setting_label.setText(QCoreApplication.translate("Widget", u"90F", None))
        self.fan_setting_label.setText(QCoreApplication.translate("Widget", u"FAN SETTING:", None))
        self.water_zone_1_label.setText(QCoreApplication.translate("Widget", u"WATER ZONE 1:", None))
        self.fan_status_on_off.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.water_zone_2_label.setText(QCoreApplication.translate("Widget", u"WATER ZONE 2:", None))
        self.fan_status_label.setText(QCoreApplication.translate("Widget", u"FAN:", None))
        self.controls_label.setText(QCoreApplication.translate("Widget", u"CONTROLS", None))
        self.water_zone_1_control_label.setText(QCoreApplication.translate("Widget", u"WATER ZONE 1:", None))
        self.water_zone_1_control_pushButton.setText(QCoreApplication.translate("Widget", u"ON", None))
        self.water_zone_2_control_label.setText(QCoreApplication.translate("Widget", u"WATER ZONE 2:", None))
        self.fan_control_label.setText(QCoreApplication.translate("Widget", u"FAN:", None))
        self.water_zone_2_control_pushButton.setText(QCoreApplication.translate("Widget", u"ON", None))
        self.fan_control_pushButton.setText(QCoreApplication.translate("Widget", u"ON", None))
        self.schedule_1_label.setText(QCoreApplication.translate("Widget", u"SCHEDULE - ZONE 1", None))
        self.wednesday_schedule_label.setText(QCoreApplication.translate("Widget", u"WEDNESDAY:", None))
        self.friday_enable_1_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.tuesday_enable_1_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.thursday_schedule_label.setText(QCoreApplication.translate("Widget", u"THURSDAY:", None))
        self.monday_schedule_label.setText(QCoreApplication.translate("Widget", u"MONDAY:", None))
        self.tuesday_schedule_label.setText(QCoreApplication.translate("Widget", u"TUESDAY:", None))
        self.monday_enable_1_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.thursday_enable_1_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.saturday_enable_1_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.wednesday_enable_1_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.friday_schedule_label.setText(QCoreApplication.translate("Widget", u"FRIDAY:", None))
        self.sunday_enable_1_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.sunday_schedule_label.setText(QCoreApplication.translate("Widget", u"SUNDAY:", None))
        self.saturday_schedule_label.setText(QCoreApplication.translate("Widget", u"SATURDAY:", None))
        self.temp_chart_label.setText(QCoreApplication.translate("Widget", u"TEMPERATURE CHART", None))
        self.schedule_2_label.setText(QCoreApplication.translate("Widget", u"SCHEDULE - ZONE 2", None))
        self.saturday_enable_2_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.thursday_schedule_label_2.setText(QCoreApplication.translate("Widget", u"THURSDAY:", None))
        self.wednesday_enable_2_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.thursday_enable_2_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.monday_enable_2_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.tuesday_schedule_label_2.setText(QCoreApplication.translate("Widget", u"TUESDAY:", None))
        self.monday_schedule_label_2.setText(QCoreApplication.translate("Widget", u"MONDAY:", None))
        self.friday_schedule_label_2.setText(QCoreApplication.translate("Widget", u"FRIDAY:", None))
        self.sunday_schedule_label_2.setText(QCoreApplication.translate("Widget", u"SUNDAY:", None))
        self.sunday_enable_2_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.wednesday_schedule_label_2.setText(QCoreApplication.translate("Widget", u"WEDNESDAY:", None))
        self.tuesday_enable_2_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.friday_enable_2_checkbox.setText(QCoreApplication.translate("Widget", u"ENABLED", None))
        self.saturday_schedule_label_2.setText(QCoreApplication.translate("Widget", u"SATURDAY:", None))
        self.title_label.setText(QCoreApplication.translate("Widget", u"GREEN HOUSE CONTROLLER", None))
        self.save_pushButton.setText(QCoreApplication.translate("Widget", u"SAVE SETTINGS", None))
        self.reset_pushButton.setText(QCoreApplication.translate("Widget", u"RESET SETTINGS", None))
    # retranslateUi

