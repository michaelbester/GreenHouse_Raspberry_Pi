# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTimeEdit, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1384, 982)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.title_label = QLabel(Widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(340, -10, 641, 78))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.title_label.setFont(font)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 50, 631, 822))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.controls_label = QLabel(self.verticalLayoutWidget)
        self.controls_label.setObjectName(u"controls_label")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(True)
        self.controls_label.setFont(font1)
        self.controls_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.controls_label, 3, 0, 1, 1)

        self.status_label = QLabel(self.verticalLayoutWidget)
        self.status_label.setObjectName(u"status_label")
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Tahoma"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setKerning(True)
        self.status_label.setFont(font2)
        self.status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.status_label, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.fan_control_label = QLabel(self.verticalLayoutWidget)
        self.fan_control_label.setObjectName(u"fan_control_label")
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        font3.setPointSize(20)
        self.fan_control_label.setFont(font3)

        self.gridLayout_3.addWidget(self.fan_control_label, 2, 0, 1, 1)

        self.water_zone_1_control_pushButton = QPushButton(self.verticalLayoutWidget)
        self.water_zone_1_control_pushButton.setObjectName(u"water_zone_1_control_pushButton")
        self.water_zone_1_control_pushButton.setMinimumSize(QSize(0, 30))
        self.water_zone_1_control_pushButton.setMaximumSize(QSize(120, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Tahoma"])
        self.water_zone_1_control_pushButton.setFont(font4)

        self.gridLayout_3.addWidget(self.water_zone_1_control_pushButton, 0, 1, 1, 1)

        self.fan_control_pushButton = QPushButton(self.verticalLayoutWidget)
        self.fan_control_pushButton.setObjectName(u"fan_control_pushButton")
        self.fan_control_pushButton.setMinimumSize(QSize(0, 30))
        self.fan_control_pushButton.setFont(font4)

        self.gridLayout_3.addWidget(self.fan_control_pushButton, 2, 1, 1, 1)

        self.water_zone_1_control_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_1_control_label.setObjectName(u"water_zone_1_control_label")
        self.water_zone_1_control_label.setFont(font3)

        self.gridLayout_3.addWidget(self.water_zone_1_control_label, 0, 0, 1, 1)

        self.water_zone_2_control_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_2_control_label.setObjectName(u"water_zone_2_control_label")
        self.water_zone_2_control_label.setFont(font3)

        self.gridLayout_3.addWidget(self.water_zone_2_control_label, 1, 0, 1, 1)

        self.water_zone_2_control_pushButton = QPushButton(self.verticalLayoutWidget)
        self.water_zone_2_control_pushButton.setObjectName(u"water_zone_2_control_pushButton")
        self.water_zone_2_control_pushButton.setMinimumSize(QSize(0, 30))
        self.water_zone_2_control_pushButton.setFont(font4)

        self.gridLayout_3.addWidget(self.water_zone_2_control_pushButton, 1, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 4, 0, 1, 1)

        self.status_gridLayout_2 = QGridLayout()
        self.status_gridLayout_2.setObjectName(u"status_gridLayout_2")
        self.status_gridLayout_2.setVerticalSpacing(10)
        self.fan_setting_label = QLabel(self.verticalLayoutWidget)
        self.fan_setting_label.setObjectName(u"fan_setting_label")
        self.fan_setting_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.fan_setting_label, 5, 0, 1, 1)

        self.inside_temp_label = QLabel(self.verticalLayoutWidget)
        self.inside_temp_label.setObjectName(u"inside_temp_label")
        self.inside_temp_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.inside_temp_label, 1, 0, 1, 1)

        self.outside_temp_label = QLabel(self.verticalLayoutWidget)
        self.outside_temp_label.setObjectName(u"outside_temp_label")
        self.outside_temp_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.outside_temp_label, 0, 0, 1, 1)

        self.outside_temp_val_label = QLabel(self.verticalLayoutWidget)
        self.outside_temp_val_label.setObjectName(u"outside_temp_val_label")
        self.outside_temp_val_label.setFont(font3)
        self.outside_temp_val_label.setToolTipDuration(2000)

        self.status_gridLayout_2.addWidget(self.outside_temp_val_label, 0, 2, 1, 1)

        self.water_zone_1_val_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_1_val_label.setObjectName(u"water_zone_1_val_label")
        self.water_zone_1_val_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.water_zone_1_val_label, 2, 2, 1, 1)

        self.water_zone_1_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_1_label.setObjectName(u"water_zone_1_label")
        self.water_zone_1_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.water_zone_1_label, 2, 0, 1, 1)

        self.fan_status_on_off = QLabel(self.verticalLayoutWidget)
        self.fan_status_on_off.setObjectName(u"fan_status_on_off")
        self.fan_status_on_off.setFont(font3)

        self.status_gridLayout_2.addWidget(self.fan_status_on_off, 4, 2, 1, 1)

        self.water_zone_2_val_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_2_val_label.setObjectName(u"water_zone_2_val_label")
        self.water_zone_2_val_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.water_zone_2_val_label, 3, 2, 1, 1)

        self.inside_temp_val_label = QLabel(self.verticalLayoutWidget)
        self.inside_temp_val_label.setObjectName(u"inside_temp_val_label")
        self.inside_temp_val_label.setFont(font3)
        self.inside_temp_val_label.setToolTipDuration(2000)

        self.status_gridLayout_2.addWidget(self.inside_temp_val_label, 1, 2, 1, 1)

        self.water_zone_2_label = QLabel(self.verticalLayoutWidget)
        self.water_zone_2_label.setObjectName(u"water_zone_2_label")
        self.water_zone_2_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.water_zone_2_label, 3, 0, 1, 1)

        self.fan_temp_setting_label = QLabel(self.verticalLayoutWidget)
        self.fan_temp_setting_label.setObjectName(u"fan_temp_setting_label")
        self.fan_temp_setting_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.fan_temp_setting_label, 5, 2, 1, 1)

        self.fan_status_label = QLabel(self.verticalLayoutWidget)
        self.fan_status_label.setObjectName(u"fan_status_label")
        self.fan_status_label.setFont(font3)

        self.status_gridLayout_2.addWidget(self.fan_status_label, 4, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.status_gridLayout_2.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.status_gridLayout_2, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sched_zone_1_label = QLabel(self.verticalLayoutWidget)
        self.sched_zone_1_label.setObjectName(u"sched_zone_1_label")
        self.sched_zone_1_label.setFont(font1)
        self.sched_zone_1_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.sched_zone_1_label, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 48, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.zone1_mon_pushButton = QPushButton(self.verticalLayoutWidget)
        self.zone1_mon_pushButton.setObjectName(u"zone1_mon_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.zone1_mon_pushButton.sizePolicy().hasHeightForWidth())
        self.zone1_mon_pushButton.setSizePolicy(sizePolicy1)
        self.zone1_mon_pushButton.setMinimumSize(QSize(0, 50))
        font5 = QFont()
        font5.setPointSize(15)
        self.zone1_mon_pushButton.setFont(font5)
        self.zone1_mon_pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.zone1_mon_pushButton)

        self.zone1_tues_pushButton = QPushButton(self.verticalLayoutWidget)
        self.zone1_tues_pushButton.setObjectName(u"zone1_tues_pushButton")
        sizePolicy1.setHeightForWidth(self.zone1_tues_pushButton.sizePolicy().hasHeightForWidth())
        self.zone1_tues_pushButton.setSizePolicy(sizePolicy1)
        self.zone1_tues_pushButton.setMinimumSize(QSize(0, 50))
        self.zone1_tues_pushButton.setFont(font5)
        self.zone1_tues_pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.zone1_tues_pushButton)

        self.zone1_wed_pushButton = QPushButton(self.verticalLayoutWidget)
        self.zone1_wed_pushButton.setObjectName(u"zone1_wed_pushButton")
        sizePolicy1.setHeightForWidth(self.zone1_wed_pushButton.sizePolicy().hasHeightForWidth())
        self.zone1_wed_pushButton.setSizePolicy(sizePolicy1)
        self.zone1_wed_pushButton.setMinimumSize(QSize(0, 50))
        self.zone1_wed_pushButton.setFont(font5)
        self.zone1_wed_pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.zone1_wed_pushButton)

        self.zone1_thurs_pushButton = QPushButton(self.verticalLayoutWidget)
        self.zone1_thurs_pushButton.setObjectName(u"zone1_thurs_pushButton")
        sizePolicy1.setHeightForWidth(self.zone1_thurs_pushButton.sizePolicy().hasHeightForWidth())
        self.zone1_thurs_pushButton.setSizePolicy(sizePolicy1)
        self.zone1_thurs_pushButton.setMinimumSize(QSize(0, 50))
        self.zone1_thurs_pushButton.setFont(font5)
        self.zone1_thurs_pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.zone1_thurs_pushButton)

        self.zone1_fri_pushButton = QPushButton(self.verticalLayoutWidget)
        self.zone1_fri_pushButton.setObjectName(u"zone1_fri_pushButton")
        sizePolicy1.setHeightForWidth(self.zone1_fri_pushButton.sizePolicy().hasHeightForWidth())
        self.zone1_fri_pushButton.setSizePolicy(sizePolicy1)
        self.zone1_fri_pushButton.setMinimumSize(QSize(0, 50))
        self.zone1_fri_pushButton.setFont(font5)
        self.zone1_fri_pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.zone1_fri_pushButton)

        self.zone1_sat_pushButton = QPushButton(self.verticalLayoutWidget)
        self.zone1_sat_pushButton.setObjectName(u"zone1_sat_pushButton")
        sizePolicy1.setHeightForWidth(self.zone1_sat_pushButton.sizePolicy().hasHeightForWidth())
        self.zone1_sat_pushButton.setSizePolicy(sizePolicy1)
        self.zone1_sat_pushButton.setMinimumSize(QSize(0, 50))
        self.zone1_sat_pushButton.setFont(font5)
        self.zone1_sat_pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.zone1_sat_pushButton)

        self.zone1_sun_pushButton = QPushButton(self.verticalLayoutWidget)
        self.zone1_sun_pushButton.setObjectName(u"zone1_sun_pushButton")
        sizePolicy1.setHeightForWidth(self.zone1_sun_pushButton.sizePolicy().hasHeightForWidth())
        self.zone1_sun_pushButton.setSizePolicy(sizePolicy1)
        self.zone1_sun_pushButton.setMinimumSize(QSize(0, 50))
        self.zone1_sun_pushButton.setFont(font5)
        self.zone1_sun_pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.zone1_sun_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.start_time_zone_1_label = QLabel(self.verticalLayoutWidget)
        self.start_time_zone_1_label.setObjectName(u"start_time_zone_1_label")
        self.start_time_zone_1_label.setFont(font3)

        self.horizontalLayout_3.addWidget(self.start_time_zone_1_label)

        self.start_time_zone_1_val = QTimeEdit(self.verticalLayoutWidget)
        self.start_time_zone_1_val.setObjectName(u"start_time_zone_1_val")
        sizePolicy1.setHeightForWidth(self.start_time_zone_1_val.sizePolicy().hasHeightForWidth())
        self.start_time_zone_1_val.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setPointSize(20)
        self.start_time_zone_1_val.setFont(font6)

        self.horizontalLayout_3.addWidget(self.start_time_zone_1_val)

        self.horizontalSpacer_6 = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.duration_zone_1_label = QLabel(self.verticalLayoutWidget)
        self.duration_zone_1_label.setObjectName(u"duration_zone_1_label")
        self.duration_zone_1_label.setFont(font3)

        self.horizontalLayout_4.addWidget(self.duration_zone_1_label)

        self.horizontalSpacer_16 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.horizontalSpacer_5 = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.duration_zone_1_val = QSpinBox(self.verticalLayoutWidget)
        self.duration_zone_1_val.setObjectName(u"duration_zone_1_val")
        sizePolicy1.setHeightForWidth(self.duration_zone_1_val.sizePolicy().hasHeightForWidth())
        self.duration_zone_1_val.setSizePolicy(sizePolicy1)
        self.duration_zone_1_val.setMinimumSize(QSize(110, 0))
        self.duration_zone_1_val.setFont(font6)
        self.duration_zone_1_val.setAlignment(Qt.AlignCenter)
        self.duration_zone_1_val.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.duration_zone_1_val)

        self.duration_zone_1_minutes_label = QLabel(self.verticalLayoutWidget)
        self.duration_zone_1_minutes_label.setObjectName(u"duration_zone_1_minutes_label")
        self.duration_zone_1_minutes_label.setFont(font3)

        self.horizontalLayout_4.addWidget(self.duration_zone_1_minutes_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayoutWidget_2 = QWidget(Widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(660, 50, 701, 571))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 70, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.temp_chart_label = QLabel(self.verticalLayoutWidget_2)
        self.temp_chart_label.setObjectName(u"temp_chart_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.temp_chart_label.sizePolicy().hasHeightForWidth())
        self.temp_chart_label.setSizePolicy(sizePolicy2)
        self.temp_chart_label.setMaximumSize(QSize(930, 16777215))
        self.temp_chart_label.setFont(font1)
        self.temp_chart_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.temp_chart_label)

        self.chart_graphicsView = PlotWidget(self.verticalLayoutWidget_2)
        self.chart_graphicsView.setObjectName(u"chart_graphicsView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.chart_graphicsView.sizePolicy().hasHeightForWidth())
        self.chart_graphicsView.setSizePolicy(sizePolicy3)
        self.chart_graphicsView.setMinimumSize(QSize(0, 400))

        self.verticalLayout_2.addWidget(self.chart_graphicsView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.min_outdoor_temp_label = QLabel(self.verticalLayoutWidget_2)
        self.min_outdoor_temp_label.setObjectName(u"min_outdoor_temp_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.min_outdoor_temp_label.sizePolicy().hasHeightForWidth())
        self.min_outdoor_temp_label.setSizePolicy(sizePolicy4)
        font7 = QFont()
        font7.setFamilies([u"Tahoma"])
        font7.setPointSize(15)
        self.min_outdoor_temp_label.setFont(font7)

        self.horizontalLayout.addWidget(self.min_outdoor_temp_label)

        self.min_outdoor_temp_val_label = QLabel(self.verticalLayoutWidget_2)
        self.min_outdoor_temp_val_label.setObjectName(u"min_outdoor_temp_val_label")
        self.min_outdoor_temp_val_label.setMaximumSize(QSize(130, 16777215))
        self.min_outdoor_temp_val_label.setFont(font7)

        self.horizontalLayout.addWidget(self.min_outdoor_temp_val_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.max_outdoor_temp_label = QLabel(self.verticalLayoutWidget_2)
        self.max_outdoor_temp_label.setObjectName(u"max_outdoor_temp_label")
        sizePolicy4.setHeightForWidth(self.max_outdoor_temp_label.sizePolicy().hasHeightForWidth())
        self.max_outdoor_temp_label.setSizePolicy(sizePolicy4)
        self.max_outdoor_temp_label.setFont(font7)

        self.horizontalLayout.addWidget(self.max_outdoor_temp_label)

        self.max_outdoor_temp_val_label = QLabel(self.verticalLayoutWidget_2)
        self.max_outdoor_temp_val_label.setObjectName(u"max_outdoor_temp_val_label")
        self.max_outdoor_temp_val_label.setMaximumSize(QSize(130, 16777215))
        self.max_outdoor_temp_val_label.setFont(font7)

        self.horizontalLayout.addWidget(self.max_outdoor_temp_val_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(660, 630, 701, 236))
        self.gridLayout_10 = QGridLayout(self.layoutWidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.zone2_mon_pushButton = QPushButton(self.layoutWidget)
        self.zone2_mon_pushButton.setObjectName(u"zone2_mon_pushButton")
        sizePolicy1.setHeightForWidth(self.zone2_mon_pushButton.sizePolicy().hasHeightForWidth())
        self.zone2_mon_pushButton.setSizePolicy(sizePolicy1)
        self.zone2_mon_pushButton.setMinimumSize(QSize(0, 50))
        self.zone2_mon_pushButton.setFont(font5)
        self.zone2_mon_pushButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.zone2_mon_pushButton)

        self.zone2_tues_pushButton = QPushButton(self.layoutWidget)
        self.zone2_tues_pushButton.setObjectName(u"zone2_tues_pushButton")
        sizePolicy1.setHeightForWidth(self.zone2_tues_pushButton.sizePolicy().hasHeightForWidth())
        self.zone2_tues_pushButton.setSizePolicy(sizePolicy1)
        self.zone2_tues_pushButton.setMinimumSize(QSize(0, 50))
        self.zone2_tues_pushButton.setFont(font5)
        self.zone2_tues_pushButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.zone2_tues_pushButton)

        self.zone2_wed_pushButton = QPushButton(self.layoutWidget)
        self.zone2_wed_pushButton.setObjectName(u"zone2_wed_pushButton")
        sizePolicy1.setHeightForWidth(self.zone2_wed_pushButton.sizePolicy().hasHeightForWidth())
        self.zone2_wed_pushButton.setSizePolicy(sizePolicy1)
        self.zone2_wed_pushButton.setMinimumSize(QSize(0, 50))
        self.zone2_wed_pushButton.setFont(font5)
        self.zone2_wed_pushButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.zone2_wed_pushButton)

        self.zone2_thurs_pushButton = QPushButton(self.layoutWidget)
        self.zone2_thurs_pushButton.setObjectName(u"zone2_thurs_pushButton")
        sizePolicy1.setHeightForWidth(self.zone2_thurs_pushButton.sizePolicy().hasHeightForWidth())
        self.zone2_thurs_pushButton.setSizePolicy(sizePolicy1)
        self.zone2_thurs_pushButton.setMinimumSize(QSize(0, 50))
        self.zone2_thurs_pushButton.setFont(font5)
        self.zone2_thurs_pushButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.zone2_thurs_pushButton)

        self.zone2_fri_pushButton = QPushButton(self.layoutWidget)
        self.zone2_fri_pushButton.setObjectName(u"zone2_fri_pushButton")
        sizePolicy1.setHeightForWidth(self.zone2_fri_pushButton.sizePolicy().hasHeightForWidth())
        self.zone2_fri_pushButton.setSizePolicy(sizePolicy1)
        self.zone2_fri_pushButton.setMinimumSize(QSize(0, 50))
        self.zone2_fri_pushButton.setFont(font5)
        self.zone2_fri_pushButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.zone2_fri_pushButton)

        self.zone2_sat_pushButton = QPushButton(self.layoutWidget)
        self.zone2_sat_pushButton.setObjectName(u"zone2_sat_pushButton")
        sizePolicy1.setHeightForWidth(self.zone2_sat_pushButton.sizePolicy().hasHeightForWidth())
        self.zone2_sat_pushButton.setSizePolicy(sizePolicy1)
        self.zone2_sat_pushButton.setMinimumSize(QSize(0, 50))
        self.zone2_sat_pushButton.setFont(font5)
        self.zone2_sat_pushButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.zone2_sat_pushButton)

        self.zone2_sun_pushButton = QPushButton(self.layoutWidget)
        self.zone2_sun_pushButton.setObjectName(u"zone2_sun_pushButton")
        sizePolicy1.setHeightForWidth(self.zone2_sun_pushButton.sizePolicy().hasHeightForWidth())
        self.zone2_sun_pushButton.setSizePolicy(sizePolicy1)
        self.zone2_sun_pushButton.setMinimumSize(QSize(0, 50))
        self.zone2_sun_pushButton.setFont(font5)
        self.zone2_sun_pushButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.zone2_sun_pushButton)


        self.gridLayout_10.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.verticalSpacer_12, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.start_time_zone_2_label = QLabel(self.layoutWidget)
        self.start_time_zone_2_label.setObjectName(u"start_time_zone_2_label")
        self.start_time_zone_2_label.setFont(font3)

        self.horizontalLayout_13.addWidget(self.start_time_zone_2_label)

        self.start_time_zone_2_val = QTimeEdit(self.layoutWidget)
        self.start_time_zone_2_val.setObjectName(u"start_time_zone_2_val")
        sizePolicy1.setHeightForWidth(self.start_time_zone_2_val.sizePolicy().hasHeightForWidth())
        self.start_time_zone_2_val.setSizePolicy(sizePolicy1)
        self.start_time_zone_2_val.setFont(font6)

        self.horizontalLayout_13.addWidget(self.start_time_zone_2_val)

        self.horizontalSpacer_12 = QSpacerItem(160, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)


        self.gridLayout_10.addLayout(self.horizontalLayout_13, 3, 0, 1, 1)

        self.sched_zone_2_label = QLabel(self.layoutWidget)
        self.sched_zone_2_label.setObjectName(u"sched_zone_2_label")
        self.sched_zone_2_label.setFont(font1)
        self.sched_zone_2_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.sched_zone_2_label, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.duration_zone_2_label = QLabel(self.layoutWidget)
        self.duration_zone_2_label.setObjectName(u"duration_zone_2_label")
        self.duration_zone_2_label.setFont(font3)

        self.horizontalLayout_14.addWidget(self.duration_zone_2_label)

        self.horizontalSpacer_17 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_15 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_13 = QSpacerItem(128, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.duration_zone_2_val = QSpinBox(self.layoutWidget)
        self.duration_zone_2_val.setObjectName(u"duration_zone_2_val")
        sizePolicy1.setHeightForWidth(self.duration_zone_2_val.sizePolicy().hasHeightForWidth())
        self.duration_zone_2_val.setSizePolicy(sizePolicy1)
        self.duration_zone_2_val.setMinimumSize(QSize(110, 0))
        self.duration_zone_2_val.setFont(font6)
        self.duration_zone_2_val.setAlignment(Qt.AlignCenter)
        self.duration_zone_2_val.setMinimum(1)

        self.horizontalLayout_14.addWidget(self.duration_zone_2_val)

        self.duration_zone_1_minutes_label_4 = QLabel(self.layoutWidget)
        self.duration_zone_1_minutes_label_4.setObjectName(u"duration_zone_1_minutes_label_4")
        self.duration_zone_1_minutes_label_4.setFont(font3)

        self.horizontalLayout_14.addWidget(self.duration_zone_1_minutes_label_4)


        self.gridLayout_10.addLayout(self.horizontalLayout_14, 4, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 880, 1341, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.save_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")
        sizePolicy1.setHeightForWidth(self.save_pushButton.sizePolicy().hasHeightForWidth())
        self.save_pushButton.setSizePolicy(sizePolicy1)
        self.save_pushButton.setMinimumSize(QSize(200, 60))
        self.save_pushButton.setMaximumSize(QSize(16777215, 60))
        font8 = QFont()
        font8.setPointSize(15)
        font8.setBold(True)
        self.save_pushButton.setFont(font8)

        self.horizontalLayout_5.addWidget(self.save_pushButton)

        self.horizontalSpacer_7 = QSpacerItem(250, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.reset_pushButton = QPushButton(self.horizontalLayoutWidget)
        self.reset_pushButton.setObjectName(u"reset_pushButton")
        sizePolicy1.setHeightForWidth(self.reset_pushButton.sizePolicy().hasHeightForWidth())
        self.reset_pushButton.setSizePolicy(sizePolicy1)
        self.reset_pushButton.setMinimumSize(QSize(200, 60))
        self.reset_pushButton.setMaximumSize(QSize(16777215, 60))
        self.reset_pushButton.setFont(font8)

        self.horizontalLayout_5.addWidget(self.reset_pushButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"GREEN HOUSE", None))
        self.title_label.setText(QCoreApplication.translate("Widget", u"GREEN HOUSE CONTROLLER", None))
        self.controls_label.setText(QCoreApplication.translate("Widget", u"CONTROLS", None))
        self.status_label.setText(QCoreApplication.translate("Widget", u"STATUS", None))
        self.fan_control_label.setText(QCoreApplication.translate("Widget", u"FAN:", None))
        self.water_zone_1_control_pushButton.setText(QCoreApplication.translate("Widget", u"TURN ON", None))
        self.fan_control_pushButton.setText(QCoreApplication.translate("Widget", u"TURN ON", None))
        self.water_zone_1_control_label.setText(QCoreApplication.translate("Widget", u"WATER ZONE 1:", None))
        self.water_zone_2_control_label.setText(QCoreApplication.translate("Widget", u"WATER ZONE 2:", None))
        self.water_zone_2_control_pushButton.setText(QCoreApplication.translate("Widget", u"TURN ON", None))
        self.fan_setting_label.setText(QCoreApplication.translate("Widget", u"FAN SETTING:", None))
        self.inside_temp_label.setText(QCoreApplication.translate("Widget", u"INSIDE TEMPERATURE:", None))
        self.outside_temp_label.setText(QCoreApplication.translate("Widget", u"OUTSIDE TEMPERATURE:", None))
#if QT_CONFIG(tooltip)
        self.outside_temp_val_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.outside_temp_val_label.setText(QCoreApplication.translate("Widget", u"??F", None))
        self.water_zone_1_val_label.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.water_zone_1_label.setText(QCoreApplication.translate("Widget", u"WATER ZONE 1:", None))
        self.fan_status_on_off.setText(QCoreApplication.translate("Widget", u"OFF", None))
        self.water_zone_2_val_label.setText(QCoreApplication.translate("Widget", u"OFF", None))
#if QT_CONFIG(tooltip)
        self.inside_temp_val_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.inside_temp_val_label.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.inside_temp_val_label.setText(QCoreApplication.translate("Widget", u"??F", None))
        self.water_zone_2_label.setText(QCoreApplication.translate("Widget", u"WATER ZONE 2:", None))
        self.fan_temp_setting_label.setText(QCoreApplication.translate("Widget", u"??F", None))
        self.fan_status_label.setText(QCoreApplication.translate("Widget", u"FAN:", None))
        self.sched_zone_1_label.setText(QCoreApplication.translate("Widget", u"SCHEDULE - ZONE 1", None))
        self.zone1_mon_pushButton.setText(QCoreApplication.translate("Widget", u"MON", None))
        self.zone1_tues_pushButton.setText(QCoreApplication.translate("Widget", u"TUES", None))
        self.zone1_wed_pushButton.setText(QCoreApplication.translate("Widget", u"WED", None))
        self.zone1_thurs_pushButton.setText(QCoreApplication.translate("Widget", u"THURS", None))
        self.zone1_fri_pushButton.setText(QCoreApplication.translate("Widget", u"FRI", None))
        self.zone1_sat_pushButton.setText(QCoreApplication.translate("Widget", u"SAT", None))
        self.zone1_sun_pushButton.setText(QCoreApplication.translate("Widget", u"SUN", None))
        self.start_time_zone_1_label.setText(QCoreApplication.translate("Widget", u"START TIME:", None))
        self.duration_zone_1_label.setText(QCoreApplication.translate("Widget", u"DURATION:", None))
        self.duration_zone_1_minutes_label.setText(QCoreApplication.translate("Widget", u"Minutes", None))
        self.temp_chart_label.setText(QCoreApplication.translate("Widget", u"TEMPERATURE CHART", None))
        self.min_outdoor_temp_label.setText(QCoreApplication.translate("Widget", u"MIN OUTDOOR TEMP:", None))
        self.min_outdoor_temp_val_label.setText(QCoreApplication.translate("Widget", u"??F", None))
        self.max_outdoor_temp_label.setText(QCoreApplication.translate("Widget", u"MAX OUTDOOR TEMP:", None))
        self.max_outdoor_temp_val_label.setText(QCoreApplication.translate("Widget", u"??F", None))
        self.zone2_mon_pushButton.setText(QCoreApplication.translate("Widget", u"MON", None))
        self.zone2_tues_pushButton.setText(QCoreApplication.translate("Widget", u"TUES", None))
        self.zone2_wed_pushButton.setText(QCoreApplication.translate("Widget", u"WED", None))
        self.zone2_thurs_pushButton.setText(QCoreApplication.translate("Widget", u"THURS", None))
        self.zone2_fri_pushButton.setText(QCoreApplication.translate("Widget", u"FRI", None))
        self.zone2_sat_pushButton.setText(QCoreApplication.translate("Widget", u"SAT", None))
        self.zone2_sun_pushButton.setText(QCoreApplication.translate("Widget", u"SUN", None))
        self.start_time_zone_2_label.setText(QCoreApplication.translate("Widget", u"START TIME:", None))
        self.sched_zone_2_label.setText(QCoreApplication.translate("Widget", u"SCHEDULE - ZONE 2", None))
        self.duration_zone_2_label.setText(QCoreApplication.translate("Widget", u"DURATION:", None))
        self.duration_zone_1_minutes_label_4.setText(QCoreApplication.translate("Widget", u"Minutes", None))
        self.save_pushButton.setText(QCoreApplication.translate("Widget", u"SAVE SETTINGS", None))
        self.reset_pushButton.setText(QCoreApplication.translate("Widget", u"RESET SETTINGS", None))
    # retranslateUi

