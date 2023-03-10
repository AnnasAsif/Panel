from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Window')
        self.setFixedSize(800, 600)

        # Create a label and a button
        self.label = QLabel('Hello, world!')
        self.button = QPushButton('Click me')

        # Create a list of image paths
        image_paths = ['./bruce.jpg', './idris.jpg', './person.jpg']

        # Create a list of labels to hold the images
        self.image_labels = []

        # Loop through the image paths and create a label and pixmap for each image
        for path in image_paths:
            pixmap = QPixmap(path)
            scaled_pixmap = pixmap.scaled(300, 200)
            label = QLabel()
            label.setPixmap(scaled_pixmap)
            label.setFixedSize(300, 200)
            self.image_labels.append(label)

        # Create a widget to hold the image labels
        widget = QWidget()
        vbox = QHBoxLayout()
        for label in self.image_labels:
            vbox.addWidget(label)
        widget.setLayout(vbox)

        # Create a scroll area and set its widget to the image label widget
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)

        # Create a horizontal box layout to hold the label, button, and scroll area
        hbox = QVBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.button)
        hbox.addWidget(scroll_area)

        # Create a widget to hold the layout
        widget = QWidget()
        widget.setLayout(hbox)

        # Set the widget as the central widget of the main window
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()