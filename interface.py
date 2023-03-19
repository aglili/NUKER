from PyQt5.QtWidgets import QApplication, QLabel,Qwidget


app = QApplication([])

window = Qwidget()

window.setWindowTitle("Hello,World")

label =QLabel("hello World",parent=window)

label.move(50,50)

window.show()

app.exec()