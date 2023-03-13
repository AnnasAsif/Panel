from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QScrollArea
from PyQt5.QtGui import QPixmap

import requests
import json

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Window')
        self.setFixedSize(800, 600)

        # Check for internet connectivity
        if self.check_internet == False:
            print('Internet is not available')
        else:
            print('Internet is available')
            # Create a label and a button
            self.label = QLabel('Hello, world!')
            self.button = QPushButton('Click me')

            # Create a list of image paths
            response = requests.get('http://161.97.164.28:8080/api/categories/seemore')
            data = json.loads(response.text)
            image_paths = data['content']
            
            # print(data['content'][0])


            # Create a list of labels to hold the images
            self.image_labels = []

            # Create a widget to hold the image labels
            widget = QWidget()
            hbox = QHBoxLayout()

            # Loop through the image paths and create a label and pixmap for each image
            for path in image_paths:
                vbox = QVBoxLayout()

                img = requests.get(path['thumbnail'])
                pixmap = QPixmap()
                pixmap.loadFromData(img.content)
                scaled_pixmap = pixmap.scaled(300, 200)
                label = QLabel()
                label.setPixmap(scaled_pixmap)
                label.setFixedSize(300, 200)
                
                vbox.addWidget(label)
                button= QPushButton(path['name'], self)
                vbox.addWidget(button)
                hbox.addLayout(vbox)
                
            widget.setLayout(hbox)

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


    def check_internet():
        try:
            # Send a GET request to a reliable server, such as Google
            response = requests.get('https://www.google.com/')
            # If the response is successful (status code 200), return True
            if response.status_code == 200:
                return True
        except:
            pass
        # Otherwise, return False
        return False


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()