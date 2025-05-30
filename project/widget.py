# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QInputDialog
from PySide6.QtCore import QUrl
from PySide6.QtCore import QTimer
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QGraphicsOpacityEffect
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Sağlıklı Yaşam Hatırlatıcısı")
        self.ui.buttonBack.clicked.connect(self.go_back_to_main)

        self.repeating_timer = QTimer()
        self.repeating_timer.timeout.connect(self.show_repeating_alert)
        self.repeating_message = ""

        self.ui.buttonBack.setText("⬅  Geri")
        self.ui.radioButton1.setText("  🕐 15 Dakika")
        self.ui.radioButton2.setText("  🕒 30 Dakika")
        self.ui.radioButton3.setText("  🕟 45 Dakika")
        self.ui.radioButton4.setText("  🕕 60 Dakika")

        self.alert_sound = QSoundEffect()
        self.alert_sound.setSource(QUrl.fromLocalFile("sounds/alert.wav"))
        self.alert_sound.setVolume(0.8)

        self.click_sound = QSoundEffect()
        self.click_sound.setSource(QUrl.fromLocalFile("sounds/soft_click.wav"))
        self.click_sound.setVolume(0.5)

        self.ui.label_gorev.hide()
        self.ui.button1.hide()
        self.ui.button2.hide()
        self.ui.button3.hide()
        self.ui.button4.hide()
        self.ui.frameReminderOptions.hide()
        self.ui.startButton.clicked.connect(self.show_buttons)

        self.ui.button1.clicked.connect(lambda: self.play_and_remind("DİK DURMAYI UNUTMA"))
        self.ui.button2.clicked.connect(lambda: self.play_and_remind("SU İÇMEYİ UNUTMA!"))
        self.ui.button3.clicked.connect(lambda: self.play_and_remind("NEFES EGZERSİZİ YAP!"))
        self.ui.button4.clicked.connect(lambda: self.play_and_remind("GÖZLERİNİ DİNLENDİR!"))

        self.ui.radioButton1.clicked.connect(lambda: (self.play_sound(), self.start_repeating_reminder(15, self.reminder_message)))
        self.ui.radioButton2.clicked.connect(lambda: (self.play_sound(), self.start_repeating_reminder(30, self.reminder_message)))
        self.ui.radioButton3.clicked.connect(lambda: (self.play_sound(), self.start_repeating_reminder(45, self.reminder_message)))
        self.ui.radioButton4.clicked.connect(lambda: (self.play_sound(), self.start_repeating_reminder(60, self.reminder_message)))

    def start_repeating_reminder(self, minutes, message):
        self.repeating_message = message
        self.repeating_timer.start(minutes * 60 * 1000)

        # Hatırlatıcı oluşturuldu mesajını göster
        self.ui.label_hatirlatmaOnayi.setText("🔔 Hatırlatıcı oluşturuldu!")
        self.ui.label_hatirlatmaOnayi.show()

        # Otomatik gizlenmesi (isteğe bağlı)
        QTimer.singleShot(4000, lambda: self.ui.label_hatirlatmaOnayi.hide())


    def show_repeating_alert(self):
        self.show_alert(self.repeating_message)

    def go_back_to_main(self):
        self.play_sound()
        self.ui.frameReminderOptions.hide()
        self.ui.label_gorev.hide()

        for button in [self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4]:
         button.show()

    def show_buttons(self):
        self.play_sound()
        self.ui.labelWelcome.hide()
        self.ui.startButton.hide()

        for button in[self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4]:
         button.show()


    def play_sound(self):
        self.click_sound.play()

    def play_and_remind(self, message):
        self.play_sound()
        self.show_reminder_options(message)

    def show_reminder_options(self, message):
        self.reminder_message = message
        self.ui.label_gorev.setText("SEÇİLEN GÖREV: " + message)

        # Opacity effect
        effect = QGraphicsOpacityEffect(self.ui.frameReminderOptions)
        self.ui.frameReminderOptions.setGraphicsEffect(effect)

        # animation from 0 to 1  (become visible)
        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()

        self.ui.frameReminderOptions.show()
        self.ui.label_gorev.show()

        for button in [self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4]:
         button.hide()

    def start_timer(self, minutes, message):
        milliseconds=minutes*60*1000
        timer=QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(lambda: self.show_alert(message))
        timer.start(milliseconds)

        # Reminder confirmation
        self.ui.label_hatirlatmaOnayi.setText("🔔 Hatırlatıcı oluşturuldu!")
        self.ui.label_hatirlatmaOnayi.show()
        QTimer.singleShot(10000, lambda: self.ui.label_hatirlatmaOnayi.hide())

    def show_alert(self, message):
        alert = QMessageBox(self)
        alert.setWindowTitle("🔔 HATIRLATMA ZAMANI")
        alert.setText(message.upper())
        alert.setIcon(QMessageBox.Warning)

        #attention icon
        alert.setStyleSheet("""
        QMessageBox {
         background-color: #fff8dc;
         font-size: 16px;
         font-weight: bold;
        }
        QLabel {
        color: #b22222;
        }
        """)
        self.alert_sound.play()
        alert.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    window=Widget()
    window.show()
    sys.exit(app.exec())
