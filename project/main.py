import requests as requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QListWidget, QGridLayout, QPushButton, \
    QLineEdit, QComboBox, QTextEdit, QLabel, QTextBrowser

import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Request Sender")

        self.layout = QGridLayout(self)

        self.createLeftMenu()
        self.createContent()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def createLeftMenu(self):
        self.saves = []
        self.left_menu = QListWidget()
        add_button = QPushButton('Добавить')
        remove_button = QPushButton('Удалить')

        self.left_menu.addItems(['http://'])
        self.left_menu.setCurrentRow(0)
        self.left_menu.currentRowChanged.connect(lambda: {
            self.loadSave()
        })

        self.layout.addWidget(self.left_menu, 0, 0, 16, 2)
        self.layout.addWidget(add_button, 16, 0, 1, 1)
        self.layout.addWidget(remove_button, 16, 1, 1, 1)

        add_button.clicked.connect(lambda: self.createNewPage())

        remove_button.clicked.connect(lambda: self.removePage())

    def createNewPage(self):
        new_index = self.left_menu.count()
        self.saves.append({
            'url': 'http://',
            'method': 0,
            'body': ''
        })
        self.left_menu.addItem('http://')
        self.left_menu.setCurrentRow(new_index)
        self.loadSave()

    def removePage(self):
        if self.left_menu.count() == 1:
            return

        row = self.left_menu.currentRow()

        next_row = row - 1
        if next_row < 0:
            next_row = 1

        self.left_menu.setCurrentRow(next_row)
        self.left_menu.takeItem(row)
        self.saves.remove(self.saves[row])

    def createContent(self):
        self.createSendWidgets()
        self.createBodyWidget()
        self.createResponseWidget()
        self.saveChanges()

    def createSendWidgets(self):
        self.url_editor = QLineEdit('http://')
        self.method_selector = QComboBox()
        self.method_selector.addItems(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
        button_send = QPushButton('Отправить')
        button_send.clicked.connect(lambda: self.sendRequest())

        self.url_editor.textChanged.connect(lambda: self.saveChanges())
        self.method_selector.currentIndexChanged.connect(lambda: self.saveChanges())

        self.layout.addWidget(self.method_selector, 0, 2, 1, 1)
        self.layout.addWidget(self.url_editor, 0, 3, 1, 5)
        self.layout.addWidget(button_send, 0, 8, 1, 1)

    def createBodyWidget(self):
        self.body_editor = QTextEdit()
        body_text = QLabel('Body')
        self.layout.addWidget(body_text, 1, 2, 1, 1)
        self.layout.addWidget(self.body_editor, 2, 2, 7, 7)
        self.body_editor.textChanged.connect(lambda: self.saveChanges())

    def createResponseWidget(self):
        self.response = QTextBrowser()
        self.response.setReadOnly(True)

        response_text = QLabel('Response')
        self.layout.addWidget(response_text, 9, 2, 1, 1)
        self.layout.addWidget(self.response, 10, 2, 7, 7)

    def sendRequest(self):
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        method = self.method_selector.currentText()
        url = self.url_editor.text()
        body = self.body_editor.toPlainText()
        print(body)
        try:
            req = requests.request(method, url, data=body, headers=headers)
            self.response.setHtml(req.text)
        except Exception as e:
            self.response.setText(str(e))

    def saveChanges(self):
        row = self.left_menu.currentRow()
        if row >= len(self.saves):
            self.saves.append({})

        self.saves[row] = {
            'url': self.url_editor.text(),
            'method': self.method_selector.currentIndex(),
            'body': self.body_editor.toPlainText()
        }
        self.left_menu.currentItem().setText(self.url_editor.text())

    def loadSave(self):
        save = self.saves[self.left_menu.currentRow()]
        self.url_editor.setText(save['url'])
        self.method_selector.setCurrentIndex(save['method'])
        self.body_editor.setText(save['body'])


window = MainWindow()
window.show()

app.exec()
