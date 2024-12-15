# This Python file uses the following encoding: utf-8
import sys
import json
from datetime import datetime

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class GreenHouse(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.settings = {}

        self.ui.water_zone_1_control_pushButton.clicked.connect(self.water_zone_1_clicked)
        self.ui.water_zone_2_control_pushButton.clicked.connect(self.water_zone_2_clicked)
        self.ui.save_pushButton.clicked.connect(self.save_settings_clicked)
        self.ui.reset_pushButton.clicked.connect(self.reset_settings_clicked)

        self.read_settings()
        self.init_screen_info()
        self.ui.fan_control_pushButton.clicked.connect(self.fan_clicked)

        self.center_window();

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

    def water_zone_1_clicked(self):
        if self.ui.water_zone_1_control_pushButton.text() == "ON":
            self.ui.water_zone_1_control_pushButton.setText("OFF")
        else:
            self.ui.water_zone_1_control_pushButton.setText("ON")

    def water_zone_2_clicked(self):
        if self.ui.water_zone_2_control_pushButton.text() == "ON":
            self.ui.water_zone_2_control_pushButton.setText("OFF")
        else:
            self.ui.water_zone_2_control_pushButton.setText("ON")

    def fan_clicked(self):
        if self.ui.fan_control_pushButton.text() == "ON":
            self.ui.fan_control_pushButton.setText("OFF")
        else:
            self.ui.fan_control_pushButton.setText("ON")

    # RESET ALL SETTINGS
    def reset_settings_clicked(self):
        self.settings["fan_temp"] = 95

        self.settings["zone_1_monday_time"] = "8:00AM"
        self.settings["zone_1_tuesday_time"] = "8:00AM"
        self.settings["zone_1_wednesday_time"] = "8:00AM"
        self.settings["zone_1_thursday_time"] = "8:00AM"
        self.settings["zone_1_friday_time"] = "8:00AM"
        self.settings["zone_1_saturday_time"] = "8:00AM"
        self.settings["zone_1_sunday_time"] = "8:00AM"

        self.settings["zone_1_monday_en"] = True
        self.settings["zone_1_tuesday_en"] = True
        self.settings["zone_1_wednesday_en"] = True
        self.settings["zone_1_thursday_en"] = True
        self.settings["zone_1_friday_en"] = True
        self.settings["zone_1_saturday_en"] = True
        self.settings["zone_1_sunday_en"] = True

        self.settings["zone_1_monday_duration"] = 30
        self.settings["zone_1_tuesday_duration"] = 30
        self.settings["zone_1_wednesday_duration"] = 30
        self.settings["zone_1_thursday_duration"] = 30
        self.settings["zone_1_friday_duration"] = 30
        self.settings["zone_1_saturday_duration"] = 30
        self.settings["zone_1_sunday_duration"] = 30

        self.settings["zone_2_monday_time"] = "8:00AM"
        self.settings["zone_2_tuesday_time"] = "8:00AM"
        self.settings["zone_2_wednesday_time"] = "8:00AM"
        self.settings["zone_2_thursday_time"] = "8:00AM"
        self.settings["zone_2_friday_time"] = "8:00AM"
        self.settings["zone_2_saturday_time"] = "8:00AM"
        self.settings["zone_2_sunday_time"] = "8:00AM"

        self.settings["zone_2_monday_en"] = False
        self.settings["zone_2_tuesday_en"] = False
        self.settings["zone_2_wednesday_en"] = False
        self.settings["zone_2_thursday_en"] = False
        self.settings["zone_2_friday_en"] = False
        self.settings["zone_2_saturday_en"] = False
        self.settings["zone_2_sunday_en"] = False

        self.settings["zone_2_monday_duration"] = 30
        self.settings["zone_2_tuesday_duration"] = 30
        self.settings["zone_2_wednesday_duration"] = 30
        self.settings["zone_2_thursday_duration"] = 30
        self.settings["zone_2_friday_duration"] = 30
        self.settings["zone_2_saturday_duration"] = 30
        self.settings["zone_2_sunday_duration"] = 30

        self.update_settings_file()
        self.init_screen_info()

    # SAVE ALL SETTINGS
    def save_settings_clicked(self):
        self.settings["fan_temp"] = int(self.ui.fan_temp_setting_label.text()[:-1])

        self.settings["zone_1_monday_time"] = self.ui.monday_timeEdit.time().toString('h:mmAP')
        self.settings["zone_1_tuesday_time"] = self.ui.tuesday_timeEdit.time().toString('h:mmAP')
        self.settings["zone_1_wednesday_time"] = self.ui.wednesday_timeEdit.time().toString('h:mmAP')
        self.settings["zone_1_thursday_time"] = self.ui.thursday_timeEdit.time().toString('h:mmAP')
        self.settings["zone_1_friday_time"] = self.ui.friday_timeEdit.time().toString('h:mmAP')
        self.settings["zone_1_saturday_time"] = self.ui.saturday_timeEdit.time().toString('h:mmAP')
        self.settings["zone_1_sunday_time"] = self.ui.sunday_timeEdit.time().toString('h:mmAP')

        self.settings["zone_1_monday_en"] = self.ui.monday_enable_1_checkbox.isChecked()
        self.settings["zone_1_tuesday_en"] = self.ui.tuesday_enable_1_checkbox.isChecked()
        self.settings["zone_1_wednesday_en"] = self.ui.wednesday_enable_1_checkbox.isChecked()
        self.settings["zone_1_thursday_en"] = self.ui.thursday_enable_1_checkbox.isChecked()
        self.settings["zone_1_friday_en"] = self.ui.friday_enable_1_checkbox.isChecked()
        self.settings["zone_1_saturday_en"] = self.ui.saturday_enable_1_checkbox.isChecked()
        self.settings["zone_1_sunday_en"] = self.ui.sunday_enable_1_checkbox.isChecked()

        self.settings["zone_1_monday_duration"] = self.ui.monday_duration_1_spinBox.value()
        self.settings["zone_1_tuesday_duration"] = self.ui.tuesday_duration_1_spinBox.value()
        self.settings["zone_1_wednesday_duration"] = self.ui.wednesday_duration_1_spinBox.value()
        self.settings["zone_1_thursday_duration"] = self.ui.thursday_duration_1_spinBox.value()
        self.settings["zone_1_friday_duration"] = self.ui.friday_duration_1_spinBox.value()
        self.settings["zone_1_saturday_duration"] = self.ui.saturday_duration_1_spinBox.value()
        self.settings["zone_1_sunday_duration"] = self.ui.sunday_duration_1_spinBox.value()

        self.settings["zone_2_monday_time"] = self.ui.monday_timeEdit_2.time().toString('h:mmAP')
        self.settings["zone_2_tuesday_time"] = self.ui.tuesday_timeEdit_2.time().toString('h:mmAP')
        self.settings["zone_2_wednesday_time"] = self.ui.wednesday_timeEdit_2.time().toString('h:mmAP')
        self.settings["zone_2_thursday_time"] = self.ui.thursday_timeEdit_2.time().toString('h:mmAP')
        self.settings["zone_2_friday_time"] = self.ui.friday_timeEdit_2.time().toString('h:mmAP')
        self.settings["zone_2_saturday_time"] = self.ui.saturday_timeEdit_2.time().toString('h:mmAP')
        self.settings["zone_2_sunday_time"] = self.ui.sunday_timeEdit_2.time().toString('h:mmAP')

        self.settings["zone_2_monday_en"] = self.ui.monday_enable_2_checkbox.isChecked()
        self.settings["zone_2_tuesday_en"] = self.ui.tuesday_enable_2_checkbox.isChecked()
        self.settings["zone_2_wednesday_en"] = self.ui.wednesday_enable_2_checkbox.isChecked()
        self.settings["zone_2_thursday_en"] = self.ui.thursday_enable_2_checkbox.isChecked()
        self.settings["zone_2_friday_en"] = self.ui.friday_enable_2_checkbox.isChecked()
        self.settings["zone_2_saturday_en"] = self.ui.saturday_enable_2_checkbox.isChecked()
        self.settings["zone_2_sunday_en"] = self.ui.sunday_enable_2_checkbox.isChecked()

        self.settings["zone_2_monday_duration"] = self.ui.monday_duration_2_spinBox.value()
        self.settings["zone_2_tuesday_duration"] = self.ui.tuesday_duration_2_spinBox.value()
        self.settings["zone_2_wednesday_duration"] = self.ui.wednesday_duration_2_spinBox.value()
        self.settings["zone_2_thursday_duration"] = self.ui.thursday_duration_2_spinBox.value()
        self.settings["zone_2_friday_duration"] = self.ui.friday_duration_2_spinBox.value()
        self.settings["zone_2_saturday_duration"] = self.ui.saturday_duration_2_spinBox.value()
        self.settings["zone_2_sunday_duration"] = self.ui.sunday_duration_2_spinBox.value()

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

        start_time = self.settings["zone_1_monday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.monday_timeEdit.setTime(time_object)

        start_time = self.settings["zone_1_tuesday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.tuesday_timeEdit.setTime(time_object)

        start_time = self.settings["zone_1_wednesday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.wednesday_timeEdit.setTime(time_object)

        start_time = self.settings["zone_1_thursday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.thursday_timeEdit.setTime(time_object)

        start_time = self.settings["zone_1_friday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.friday_timeEdit.setTime(time_object)

        start_time = self.settings["zone_1_saturday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.saturday_timeEdit.setTime(time_object)

        start_time = self.settings["zone_1_sunday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.sunday_timeEdit.setTime(time_object)

        duration = self.settings["zone_1_monday_duration"]
        self.ui.monday_duration_1_spinBox.setValue(duration)

        duration = self.settings["zone_1_tuesday_duration"]
        self.ui.tuesday_duration_1_spinBox.setValue(duration)

        duration = self.settings["zone_1_wednesday_duration"]
        self.ui.wednesday_duration_1_spinBox.setValue(duration)

        duration = self.settings["zone_1_thursday_duration"]
        self.ui.thursday_duration_1_spinBox.setValue(duration)

        duration = self.settings["zone_1_friday_duration"]
        self.ui.friday_duration_1_spinBox.setValue(duration)

        duration = self.settings["zone_1_saturday_duration"]
        self.ui.saturday_duration_1_spinBox.setValue(duration)

        duration = self.settings["zone_1_sunday_duration"]
        self.ui.sunday_duration_1_spinBox.setValue(duration)

        en = self.settings["zone_1_monday_en"]
        self.ui.monday_enable_1_checkbox.setChecked(en)

        en = self.settings["zone_1_tuesday_en"]
        self.ui.tuesday_enable_1_checkbox.setChecked(en)

        en = self.settings["zone_1_wednesday_en"]
        self.ui.wednesday_enable_1_checkbox.setChecked(en)

        en = self.settings["zone_1_thursday_en"]
        self.ui.thursday_enable_1_checkbox.setChecked(en)

        en = self.settings["zone_1_friday_en"]
        self.ui.friday_enable_1_checkbox.setChecked(en)

        en = self.settings["zone_1_saturday_en"]
        self.ui.saturday_enable_1_checkbox.setChecked(en)

        en = self.settings["zone_1_sunday_en"]
        self.ui.sunday_enable_1_checkbox.setChecked(en)

        start_time = self.settings["zone_2_monday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.monday_timeEdit_2.setTime(time_object)

        start_time = self.settings["zone_2_tuesday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.tuesday_timeEdit_2.setTime(time_object)

        start_time = self.settings["zone_2_wednesday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.wednesday_timeEdit_2.setTime(time_object)

        start_time = self.settings["zone_2_thursday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.thursday_timeEdit_2.setTime(time_object)

        start_time = self.settings["zone_2_friday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.friday_timeEdit_2.setTime(time_object)

        start_time = self.settings["zone_2_saturday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.saturday_timeEdit_2.setTime(time_object)

        start_time = self.settings["zone_2_sunday_time"]
        time_object = datetime.strptime(start_time, time_format).time()
        self.ui.sunday_timeEdit_2.setTime(time_object)

        duration = self.settings["zone_2_monday_duration"]
        self.ui.monday_duration_2_spinBox.setValue(duration)

        duration = self.settings["zone_2_tuesday_duration"]
        self.ui.tuesday_duration_2_spinBox.setValue(duration)

        duration = self.settings["zone_2_wednesday_duration"]
        self.ui.wednesday_duration_2_spinBox.setValue(duration)

        duration = self.settings["zone_2_thursday_duration"]
        self.ui.thursday_duration_2_spinBox.setValue(duration)

        duration = self.settings["zone_2_friday_duration"]
        self.ui.friday_duration_2_spinBox.setValue(duration)

        duration = self.settings["zone_2_saturday_duration"]
        self.ui.saturday_duration_2_spinBox.setValue(duration)

        duration = self.settings["zone_2_sunday_duration"]
        self.ui.sunday_duration_2_spinBox.setValue(duration)

        en = self.settings["zone_2_monday_en"]
        self.ui.monday_enable_2_checkbox.setChecked(en)

        en = self.settings["zone_2_tuesday_en"]
        self.ui.tuesday_enable_2_checkbox.setChecked(en)

        en = self.settings["zone_2_wednesday_en"]
        self.ui.wednesday_enable_2_checkbox.setChecked(en)

        en = self.settings["zone_2_thursday_en"]
        self.ui.thursday_enable_2_checkbox.setChecked(en)

        en = self.settings["zone_2_friday_en"]
        self.ui.friday_enable_2_checkbox.setChecked(en)

        en = self.settings["zone_2_saturday_en"]
        self.ui.saturday_enable_2_checkbox.setChecked(en)

        en = self.settings["zone_2_sunday_en"]
        self.ui.sunday_enable_2_checkbox.setChecked(en)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    greenHouse = GreenHouse()
    greenHouse.read_settings()

    greenHouse.show()
    sys.exit(app.exec())
