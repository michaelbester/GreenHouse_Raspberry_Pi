
#!/usr/bin/python3
import sys
import json
from datetime import datetime, timedelta
import requests
import pyqtgraph as pg
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer
from ui_form import Ui_Widget
import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

LED_FAN = 10
FAN_GPIO_PIN = 10

LED_WATER_1_GPIO_PIN = 7
LED_WATER_2_GPIO_PIN = 11

SOLENOID_1A_GPIO_PIN = 3
SOLENOID_1B_GPIO_PIN = 18

SOLENOID_2A_GPIO_PIN = 23
SOLENOID_2B_GPIO_PIN = 24

class GreenHouse(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.chart_x_data = []
        self.chart_outside_data = []
        self.chart_inside_data = []
        self.inside_temp = 60
        self.settings = {}

        self.ui.water_zone_1_control_pushButton.clicked.connect(self.water_zone_1_clicked)
        self.ui.water_zone_2_control_pushButton.clicked.connect(self.water_zone_2_clicked)
        self.ui.save_pushButton.clicked.connect(self.save_settings_clicked)
        self.ui.reset_pushButton.clicked.connect(self.reset_settings_clicked)

        self.read_settings()
        self.init_screen_info()
        self.ui.fan_control_pushButton.clicked.connect(self.fan_clicked)

        self.ui.zone1_mon_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_1_mon"))
        self.ui.zone1_tues_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_1_tues"))
        self.ui.zone1_wed_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_1_wed"))
        self.ui.zone1_thurs_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_1_thurs"))
        self.ui.zone1_fri_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_1_fri"))
        self.ui.zone1_sat_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_1_sat"))
        self.ui.zone1_sun_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_1_sun"))

        self.ui.zone2_mon_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_2_mon"))
        self.ui.zone2_tues_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_2_tues"))
        self.ui.zone2_wed_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_2_wed"))
        self.ui.zone2_thurs_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_2_thurs"))
        self.ui.zone2_fri_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_2_fri"))
        self.ui.zone2_sat_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_2_sat"))
        self.ui.zone2_sun_pushButton.clicked.connect(lambda: self.zone1_en_clicked("zone_2_sun"))

        self.old_indoor_temp = 0
        self.dht_device = adafruit_dht.DHT11(board.D4)
        self.temp_plot = self.ui.chart_graphicsView.plot(self.chart_x_data, self.chart_outside_data, pen=pg.mkPen('r', width=4))
        #self.get_weather()
        self.center_window()

        GPIO.setup(LED_WATER_1_GPIO_PIN, GPIO.OUT)
        GPIO.setup(LED_WATER_2_GPIO_PIN, GPIO.OUT)
        GPIO.setup(LED_FAN.GPIO_PIN, GPIO.OUT)

        GPIO.setup(SOLENOID_1A_GPIO_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_1B_GPIO_PIN, GPIO.OUT)

        GPIO.setup(SOLENOID_2A_GPIO_PIN, GPIO.OUT)
        GPIO.setup(SOLENOID_2B_GPIO_PIN, GPIO.OUT)

        GPIO.output(LED_WATER_1_GPIO_PIN, False)
        GPIO.output(LED_WATER_2_GPIO_PIN, False)
        GPIO.output(LED_FAN.GPIO_PIN, False)

        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
        GPIO.output(SOLENOID_1B_GPIO_PIN, False)

        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
        GPIO.output(SOLENOID_2B_GPIO_PIN, False)

    def center_window(self):
            # Get the screen geometry
            screen_geometry = QApplication.primaryScreen().availableGeometry()

            # Get the window geometry
            window_geometry = self.frameGeometry()

            # Calculate the center position
            center_x = int(screen_geometry.center().x() - window_geometry.width() / 2)
            center_y = int(screen_geometry.center().y() - window_geometry.height() / 2)

            # Move the window to the center
            self.move(center_x, center_y)

    def update_graph(self, temp_outside, temp_inside):
        size_x = len(self.chart_x_data)
        self.chart_outside_data.append(temp_outside)
        self.chart_inside_data.append(temp_inside)

        if(size_x < 288):
            self.chart_x_data.append(size_x * 5)

        if(size_x == 288):
            self.chart_outside_data.pop(0)
            self.chart_inside_data.pop(0)

        self.ui.chart_graphicsView.clear()
        self.ui.chart_graphicsView.plot(self.chart_x_data, self.chart_outside_data, pen=pg.mkPen('r', width=4),name="outside")
        self.ui.chart_graphicsView.plot(self.chart_x_data, self.chart_inside_data, pen=pg.mkPen('b', width=4),name="inside")

        self.ui.min_indoor_temp_label.setStyleSheet("color: green;")
        self.ui.max_indoor_temp_label.setStyleSheet("color: green;")
        self.ui.min_indoor_temp_val_label.setStyleSheet("color: green;")
        self.ui.max_indoor_temp_val_label.setStyleSheet("color: green;")
        self.ui.min_indoor_temp_val_label.setText(str(round(min(self.chart_inside_data))) + "F")
        self.ui.max_indoor_temp_val_label.setText(str(round(max(self.chart_inside_data))) + "F")

    def get_weather(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ce1c9c671cdba754b71c0526e8667ff3&units=imperial'.format("Pickens")
        res = requests.get(url)
        data = res.json()
        outside_temp = data['main']['temp']
        self.ui.outside_temp_val_label.setText(str(round(outside_temp)) + "F")
        print(datetime.now())
        print(outside_temp)

        try:
            inside_temp_c = self.dht_device.temperature
            inside_temp = inside_temp_c * (9/5) +32
            #humidity = self.dht_device.humidity
        except:
            print("DHT11 Read Failure!")
            inside_temp = self.old_inside_temp

        self.old_inside_temp = inside_temp
        self.ui.inside_temp_val_label.setText(str(int(inside_temp)) + "F")
        self.update_graph(outside_temp, inside_temp)

    def water_zone_1_clicked(self):
        if self.ui.water_zone_1_control_pushButton.text() == "TURN OFF":
            self.ui.water_zone_1_control_pushButton.setText("TURN ON")
            self.ui.water_zone_1_val_label.setText("OFF")
            controls_zone1_update_timer.start(1000 * 60 * 1)
        else:
            self.ui.water_zone_1_control_pushButton.setText("TURN OFF")
            self.ui.water_zone_1_val_label.setText("ON")
            #turn on water
            controls_zone1_update_timer.stop()

    def water_zone_2_clicked(self):
        if self.ui.water_zone_2_control_pushButton.text() == "TURN OFF":
            self.ui.water_zone_2_control_pushButton.setText("TURN ON")
            self.ui.water_zone_2_val_label.setText("OFF")
            controls_zone2_update_timer.start(1000 * 60 * 1)
        else:
            self.ui.water_zone_2_control_pushButton.setText("TURN OFF")
            self.ui.water_zone_2_val_label.setText("ON")
            controls_zone1_update_timer.stop

    def fan_clicked(self):
        if self.ui.fan_control_pushButton.text() == "TURN OFF":
            self.ui.fan_control_pushButton.setText("TURN ON")
            self.ui.fan_status_on_off.setText("OFF")
        else:
            self.ui.fan_control_pushButton.setText("TURN OFF")
            self.ui.fan_status_on_off.setText("ON")


    def zone1_en_clicked(self, name):
        match name:
            case "zone_1_mon":
                if  self.ui.zone1_mon_pushButton.isChecked():
                    self.ui.zone1_mon_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone1_mon_pushButton.setStyleSheet("color: gray;")

            case "zone_1_tues":
                if  self.ui.zone1_tues_pushButton.isChecked():
                    self.ui.zone1_tues_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone1_tues_pushButton.setStyleSheet("color: gray;")

            case "zone_1_wed":
                if  self.ui.zone1_wed_pushButton.isChecked():
                    self.ui.zone1_wed_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone1_wed_pushButton.setStyleSheet("color: gray;")

            case "zone_1_thurs":
                if  self.ui.zone1_thurs_pushButton.isChecked():
                    self.ui.zone1_thurs_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone1_thurs_pushButton.setStyleSheet("color: gray;")

            case "zone_1_fri":
                if  self.ui.zone1_fri_pushButton.isChecked():
                    self.ui.zone1_fri_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone1_fri_pushButton.setStyleSheet("color: gray;")

            case "zone_1_sat":
                if  self.ui.zone1_sat_pushButton.isChecked():
                    self.ui.zone1_sat_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone1_sat_pushButton.setStyleSheet("color: gray;")

            case "zone_1_sun":
                if  self.ui.zone1_sun_pushButton.isChecked():
                    self.ui.zone1_sun_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone1_sun_pushButton.setStyleSheet("color: gray;")

            case "zone_2_mon":
                if  self.ui.zone2_mon_pushButton.isChecked():
                    self.ui.zone2_mon_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone2_mon_pushButton.setStyleSheet("color: gray;")

            case "zone_2_tues":
                if  self.ui.zone2_tues_pushButton.isChecked():
                    self.ui.zone2_tues_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone2_tues_pushButton.setStyleSheet("color: gray;")

            case "zone_2_wed":
                if  self.ui.zone2_wed_pushButton.isChecked():
                    self.ui.zone2_wed_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone2_wed_pushButton.setStyleSheet("color: gray;")

            case "zone_2_thurs":
                if  self.ui.zone2_thurs_pushButton.isChecked():
                    self.ui.zone2_thurs_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone2_thurs_pushButton.setStyleSheet("color: gray;")

            case "zone_2_fri":
                if  self.ui.zone2_fri_pushButton.isChecked():
                    self.ui.zone2_fri_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone2_fri_pushButton.setStyleSheet("color: gray;")

            case "zone_2_sat":
                if  self.ui.zone2_sat_pushButton.isChecked():
                    self.ui.zone2_sat_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone2_sat_pushButton.setStyleSheet("color: gray;")

            case "zone_2_sun":
                if  self.ui.zone2_sun_pushButton.isChecked():
                    self.ui.zone2_sun_pushButton.setStyleSheet("color: green;")
                else:
                    self.ui.zone2_sun_pushButton.setStyleSheet("color: gray;")
    # RESET ALL SETTINGS
    def reset_settings_clicked(self):
        self.settings["fan_temp"] = 95

        self.settings["zone_1_start_time"] = "8:00AM"

        self.settings["zone_1_monday_en"] = True
        self.settings["zone_1_tuesday_en"] = True
        self.settings["zone_1_wednesday_en"] = True
        self.settings["zone_1_thursday_en"] = True
        self.settings["zone_1_friday_en"] = True
        self.settings["zone_1_saturday_en"] = True
        self.settings["zone_1_sunday_en"] = True

        self.settings["zone_1_duration"] = 30


        self.settings["zone_2_start_time"] = "8:00AM"

        self.settings["zone_2_monday_en"] = False
        self.settings["zone_2_tuesday_en"] = False
        self.settings["zone_2_wednesday_en"] = False
        self.settings["zone_2_thursday_en"] = False
        self.settings["zone_2_friday_en"] = False
        self.settings["zone_2_saturday_en"] = False
        self.settings["zone_2_sunday_en"] = False

        self.settings["zone_2_duration"] = 30

        self.update_settings_file()
        self.init_screen_info()

    # SAVE ALL SETTINGS
    def save_settings_clicked(self):
        self.settings["fan_temp"] = int(self.ui.fan_temp_setting_label.text()[:-1])

        self.settings["zone_1_start_time"] = self.ui.start_time_zone_1_val.time().toString('h:mmAP')

        self.settings["zone_1_monday_en"] = self.ui.zone1_mon_pushButton.isChecked()
        self.settings["zone_1_tuesday_en"] = self.ui.zone1_tues_pushButton.isChecked()
        self.settings["zone_1_wednesday_en"] = self.ui.zone1_wed_pushButton.isChecked()
        self.settings["zone_1_thursday_en"] = self.ui.zone1_thurs_pushButton.isChecked()
        self.settings["zone_1_friday_en"] = self.ui.zone1_fri_pushButton.isChecked()
        self.settings["zone_1_saturday_en"] = self.ui.zone1_sat_pushButton.isChecked()
        self.settings["zone_1_sunday_en"] = self.ui.zone1_sun_pushButton.isChecked()

        self.settings["zone_1_duration"] = self.ui.duration_zone_1_val.value()

        self.settings["zone_2_start_time"] = self.ui.start_time_zone_2_val.time().toString('h:mmAP')

        self.settings["zone_2_monday_en"] = self.ui.zone2_mon_pushButton.isChecked()
        self.settings["zone_2_tuesday_en"] = self.ui.zone2_tues_pushButton.isChecked()
        self.settings["zone_2_wednesday_en"] = self.ui.zone2_wed_pushButton.isChecked()
        self.settings["zone_2_thursday_en"] = self.ui.zone2_thurs_pushButton.isChecked()
        self.settings["zone_2_friday_en"] = self.ui.zone2_fri_pushButton.isChecked()
        self.settings["zone_2_saturday_en"] = self.ui.zone2_sat_pushButton.isChecked()
        self.settings["zone_2_sunday_en"] = self.ui.zone2_sun_pushButton.isChecked()

        self.settings["zone_2_duration"] = self.ui.duration_zone_2_val.value()

        self.update_settings_file()

    def read_settings(self):
        with open("settings.json") as file:
            self.settings = json.load(file)

    def update_settings_file(self):
        with open("settings.json", 'w') as json_file:
            json.dump(self.settings, json_file, indent=4)

    def init_screen_info(self):
        time_format = "%I:%M%p"

        temp = str(self.settings["fan_temp"]) + "F"
        self.ui.fan_temp_setting_label.setText(temp)

        zone_1_start_time = self.settings["zone_1_start_time"]
        time_object = datetime.strptime(zone_1_start_time, time_format).time()
        self.ui.start_time_zone_1_val.setTime(time_object)

        duration = self.settings["zone_1_duration"]
        self.ui.duration_zone_1_val.setValue(duration)

        en = self.settings["zone_1_monday_en"]
        if(en):
            self.ui.zone1_mon_pushButton.setStyleSheet("color: green;")
            self.ui.zone1_mon_pushButton.setChecked(True)
        else:
            self.ui.zone1_mon_pushButton.setStyleSheet("color: gray;")
            self.ui.zone1_mon_pushButton.setChecked(False)

        en = self.settings["zone_1_tuesday_en"]
        if(en):
            self.ui.zone1_tues_pushButton.setStyleSheet("color: green;")
            self.ui.zone1_tues_pushButton.setChecked(True)
        else:
            self.ui.zone1_tues_pushButton.setStyleSheet("color: gray;")
            self.ui.zone1_tues_pushButton.setChecked(False)

        en = self.settings["zone_1_wednesday_en"]
        if(en):
            self.ui.zone1_wed_pushButton.setStyleSheet("color: green;")
            self.ui.zone1_wed_pushButton.setChecked(True)
        else:
            self.ui.zone1_wed_pushButton.setStyleSheet("color: gray;")
            self.ui.zone1_wed_pushButton.setChecked(False)

        en = self.settings["zone_1_thursday_en"]
        if(en):
            self.ui.zone1_thurs_pushButton.setStyleSheet("color: green;")
            self.ui.zone1_thurs_pushButton.setChecked(True)
        else:
            self.ui.zone1_thurs_pushButton.setStyleSheet("color: gray;")
            self.ui.zone1_thurs_pushButton.setChecked(False)

        en = self.settings["zone_1_friday_en"]
        if(en):
            self.ui.zone1_fri_pushButton.setStyleSheet("color: green;")
            self.ui.zone1_fri_pushButton.setChecked(True)
        else:
            self.ui.zone1_fri_pushButton.setStyleSheet("color: gray;")
            self.ui.zone1_fri_pushButton.setChecked(False)

        en = self.settings["zone_1_saturday_en"]
        if(en):
            self.ui.zone1_sat_pushButton.setStyleSheet("color: green;")
            self.ui.zone1_sat_pushButton.setChecked(True)
        else:
            self.ui.zone1_sat_pushButton.setStyleSheet("color: gray;")
            self.ui.zone1_sat_pushButton.setChecked(False)

        en = self.settings["zone_1_sunday_en"]
        if(en):
            self.ui.zone1_sun_pushButton.setStyleSheet("color: green;")
            self.ui.zone1_sun_pushButton.setChecked(True)
        else:
            self.ui.zone1_sun_pushButton.setStyleSheet("color: gray;")
            self.ui.zone1_sun_pushButton.setChecked(False)

        start_time = self.settings["zone_2_start_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.start_time_zone_2_val.setTime(time_object)

        duration = self.settings["zone_2_duration"]
        self.ui.duration_zone_2_val.setValue(duration)

        en = self.settings["zone_2_monday_en"]

        if(en):
            self.ui.zone2_mon_pushButton.setStyleSheet("color: green;")
            self.ui.zone2_mon_pushButton.setChecked(True)
        else:
            self.ui.zone2_mon_pushButton.setStyleSheet("color: gray;")
            self.ui.zone2_mon_pushButton.setChecked(False)

        en = self.settings["zone_2_tuesday_en"]
        if(en):
            self.ui.zone2_tues_pushButton.setStyleSheet("color: green;")
            self.ui.zone2_tues_pushButton.setChecked(True)
        else:
            self.ui.zone2_tues_pushButton.setStyleSheet("color: gray;")
            self.ui.zone2_tues_pushButton.setChecked(False)

        en = self.settings["zone_2_wednesday_en"]
        if(en):
            self.ui.zone2_wed_pushButton.setStyleSheet("color: green;")
            self.ui.zone2_wed_pushButton.setChecked(True)
        else:
            self.ui.zone2_wed_pushButton.setStyleSheet("color: gray;")
            self.ui.zone2_wed_pushButton.setChecked(True)

        en = self.settings["zone_2_thursday_en"]
        if(en):
            self.ui.zone2_thurs_pushButton.setStyleSheet("color: green;")
            self.ui.zone2_thurs_pushButton.setChecked(True)
        else:
            self.ui.zone2_thurs_pushButton.setStyleSheet("color: gray;")
            self.ui.zone2_thurs_pushButton.setChecked(False)

        en = self.settings["zone_2_friday_en"]
        if(en):
            self.ui.zone2_fri_pushButton.setStyleSheet("color: green;")
            self.ui.zone2_fri_pushButton.setChecked(True)
        else:
            self.ui.zone2_fri_pushButton.setStyleSheet("color: gray;")
            self.ui.zone2_fri_pushButton.setChecked(False)

        en = self.settings["zone_2_saturday_en"]
        if(en):
            self.ui.zone2_sat_pushButton.setStyleSheet("color: green;")
            self.ui.zone2_sat_pushButton.setChecked(True)
        else:
            self.ui.zone2_sat_pushButton.setStyleSheet("color: gray;")
            self.ui.zone2_sat_pushButton.setChecked(False)

        en = self.settings["zone_2_sunday_en"]
        if(en):
            self.ui.zone2_sun_pushButton.setStyleSheet("color: green;")
            self.ui.zone2_sun_pushButton.setChecked(True)
        else:
            self.ui.zone2_sun_pushButton.setStyleSheet("color: gray;")
            self.ui.zone2_sun_pushButton.setChecked(False)

    def update_zone_1_controls(self):
        start_time = self.settings["zone_1_start_time"]
        duration = self.settings["zone_1_duration"]
        current_date = datetime.now()
        day_of_week = current_date.strftime('%A')
        time_of_day = current_date.strftime('%I:%M%p')
        match day_of_week:
            case "Monday":
                if self.ui.zone1_mon_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_1_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_1_val_label.setText("ON")
                        GPIO.output(LED_WATER_1_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)

                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_1_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                elif (self.ui.water_zone_1_val_label.text != "OFF") and (self.ui.water_zone_1_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)

            case "Tuesday":
                if self.ui.zone1_tues_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_1_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_1_val_label.setText("ON")
                        GPIO.output(LED_WATER_1_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_1_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                elif (self.ui.water_zone_1_val_label.text != "OFF") and (self.ui.water_zone_1_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)

            case "Wednesday":
                if self.ui.zone1_wed_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_1_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_1_val_label.setText("ON")
                        GPIO.output(LED_WATER_1_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_1_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                elif (self.ui.water_zone_1_val_label.text != "OFF") and (self.ui.water_zone_1_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)

            case "Thursday":
                if self.ui.zone1_thurs_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_1_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_1_val_label.setText("ON")
                        GPIO.output(LED_WATER_1_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_1_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                elif (self.ui.water_zone_1_val_label.text != "OFF") and (self.ui.water_zone_1_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)


            case "Friday":
                if self.ui.zone1_fri_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_1_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_1_val_label.setText("ON")
                        GPIO.output(LED_WATER_1_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_1_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                elif (self.ui.water_zone_1_val_label.text != "OFF") and (self.ui.water_zone_1_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)


            case "Saturday":
                if self.ui.zone1_sat_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_1_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_1_val_label.setText("ON")
                        GPIO.output(LED_WATER_1_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_1_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                elif (self.ui.water_zone_1_val_label.text != "OFF") and (self.ui.water_zone_1_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)


            case "Sunday":
                if self.ui.zone1_sun_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_1_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_1_val_label.setText("ON")
                        GPIO.output(LED_WATER_1_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_1_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)
                elif (self.ui.water_zone_1_val_label.text != "OFF") and (self.ui.water_zone_1_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_1_val_label.setText("OFF")
                        GPIO.output(LED_WATER_1_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_1A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_1B_GPIO_PIN, False)


    def update_zone_2_controls(self):
        start_time = self.settings["zone_2_start_time"]
        duration = self.settings["zone_2_duration"]
        current_date = datetime.now()
        day_of_week = current_date.strftime('%A')
        time_of_day = current_date.strftime('%I:%M%p')
        match day_of_week:
            case "Monday":
                if self.ui.zone2_mon_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_2_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_2_val_label.setText("ON")
                        GPIO.output(LED_WATER_2_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_2_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                elif (self.ui.water_zone_2_val_label.text != "OFF") and (self.ui.water_zone_2_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)


            case "Tuesday":
                if self.ui.zone2_tues_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_2_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_2_val_label.setText("ON")
                        GPIO.output(LED_WATER_2_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_2_val_label.text != "OFF"):
                        #turn off water
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                        self.ui.water_zone_2_val_label.setText("OFF")
                elif (self.ui.water_zone_2_val_label.text != "OFF") and (self.ui.water_zone_2_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
            case "Wednesday":
                if self.ui.zone2_wed_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_2_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_2_val_label.setText("ON")
                        GPIO.output(LED_WATER_2_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_2_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                elif (self.ui.water_zone_2_val_label.text != "OFF") and (self.ui.water_zone_2_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)

            case "Thursday":
                if self.ui.zone2_thurs_pushButton.isChecked() == True:
                    if self.compare_time_strings(time_of_day, start_time, duration) == 1:
                        #turn on water
                        self.ui.water_zone_2_val_label.setText("ON")
                        GPIO.output(LED_WATER_2_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    else:
                        #turn off water
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                elif (self.ui.water_zone_2_val_label.text != "OFF") and (self.ui.water_zone_2_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
            case "Friday":
                if self.ui.zone2_fri_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_2_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_2_val_label.setText("ON")
                        GPIO.output(LED_WATER_2_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_2_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                elif (self.ui.water_zone_2_val_label.text != "OFF") and (self.ui.water_zone_2_control_pushButton.text() == "TURN ON"):
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)

            case "Saturday":
                if self.ui.zone2_sat_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_2_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_2_val_label.setText("ON")
                        GPIO.output(LED_WATER_2_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_2_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    elif (self.ui.water_zone_2_val_label.text != "OFF") and (self.ui.water_zone_2_control_pushButton.text() == "TURN ON"):
                            self.ui.water_zone_2_val_label.setText("OFF")
                            GPIO.output(LED_WATER_2_GPIO_PIN, False)
                            GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                            GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                            time.sleep(0.1)
                            GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                            GPIO.output(SOLENOID_2B_GPIO_PIN, False)

            case "Sunday":
                if self.ui.zone2_sun_pushButton.isChecked() == True:
                    if (self.compare_time_strings(time_of_day, start_time, duration) == 1) and (self.ui.water_zone_2_val_label.text != "ON"):
                        #turn on water
                        self.ui.water_zone_2_val_label.setText("ON")
                        GPIO.output(LED_WATER_2_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, True)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    elif (self.compare_time_strings(time_of_day, start_time, duration) != 1) and (self.ui.water_zone_2_val_label.text != "OFF"):
                        #turn off water
                        self.ui.water_zone_2_val_label.setText("OFF")
                        GPIO.output(LED_WATER_2_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                        time.sleep(0.1)
                        GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                        GPIO.output(SOLENOID_2B_GPIO_PIN, False)
                    elif (self.ui.water_zone_2_val_label.text != "OFF") and (self.ui.water_zone_2_control_pushButton.text() == "TURN ON"):
                            self.ui.water_zone_2_val_label.setText("OFF")
                            GPIO.output(LED_WATER_2_GPIO_PIN, False)
                            GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                            GPIO.output(SOLENOID_2B_GPIO_PIN, True)
                            time.sleep(0.1)
                            GPIO.output(SOLENOID_2A_GPIO_PIN, False)
                            GPIO.output(SOLENOID_2B_GPIO_PIN, False)

    def update_fan_controls(self):
        if (self.inside_temp >= self.settings["fan_temp"]) and (self.ui.fan_status_on_off.text != "ON"):
            print("FAN ON")
            self.ui.fan_status_on_off.setText("ON")
            GPIO.output(FAN_GPIO_PIN, True)
        elif self.inside_temp <= (self.settings["fan_temp"] - 2) and (self.ui.fan_status_on_off.text != "OFF"):
            print("FAN OFF")
            self.ui.fan_status_on_off.setText("OFF")
            GPIO.output(FAN_GPIO_PIN, False)

    def compare_time_strings(self, time_of_day, start_time, duration):
        time_format = '%I:%M%p'
        now = datetime.strptime(time_of_day, time_format)
        start = datetime.strptime(start_time, time_format)

        stop = start + timedelta(minutes = duration)

        if (now >= start) and (now < stop):
            return 1
        else:
            return 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GPIO.setmode(GPIO.BCM)
    greenHouse = GreenHouse()
    greenHouse.read_settings()

    weather_update_timer = QTimer()
    weather_update_timer.timeout.connect(greenHouse.get_weather)
    weather_update_timer.start(1000 * 60 * 5)

    controls_zone1_update_timer = QTimer()
    controls_zone1_update_timer.timeout.connect(greenHouse.update_zone_1_controls)
    controls_zone1_update_timer.start(1000 * 10 * 1)

    controls_zone2_update_timer = QTimer()
    controls_zone2_update_timer.timeout.connect(greenHouse.update_zone_2_controls)
    controls_zone2_update_timer.start(1000 * 10 * 1)

    controls_fan_update_timer = QTimer()
    controls_fan_update_timer.timeout.connect(greenHouse.update_fan_controls)
    controls_fan_update_timer.start(1000 * 10 * 1)

    greenHouse.show()
    sys.exit(app.exec())
