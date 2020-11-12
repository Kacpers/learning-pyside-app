import sys
from PySide2 import QtCore, QtWidgets, QtGui


class InlineTranslation:
    def __init__(self, to_translate, input_form, translated, correct_translation):
        self.to_translate = to_translate
        self.input_form = input_form
        self.translated = translated
        self.correct_translation = correct_translation


class AppWidget(QtWidgets.QWidget):
    def __init__(self, words):
        super().__init__()
        self.points = 0
        self.words = words
        self.state = []
        self.layout = self.initialize_layout()
        self.setLayout(self.layout)

    def on_submit(self):
        self.points = 0
        for inline in self.state:
            if inline.correct_translation ==  inline.input_form.text():
                self.points += 1

        print(f'Zdobywasz {self.points} punktów!')
        msg = QtWidgets.QMessageBox()
        msg.setText(f'Zdobywasz {self.points} punktów!')
        msg.exec()


    def initialize_layout(self):
        row = 0
        grid = QtWidgets.QGridLayout()

        for key, correct_translation in self.words.items():
            to_translate = QtWidgets.QLabel(key)
            input_form = QtWidgets.QLineEdit()
            self.state.append(InlineTranslation(key, input_form, '', correct_translation))

            grid.addWidget(to_translate, row, 0)
            grid.addWidget(input_form, row, 1)
            row += 1

        submit = QtWidgets.QPushButton('Sprawdź')
        submit.clicked.connect(self.on_submit)
        grid.addWidget(submit, row, 1)

        return grid


if __name__ == '__main__':
    words = {
        'dog': 'pies',
        'cat': 'kot',
        'snake': 'wąż',
        'cow': 'krowa'
    }

    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Nauka słówek by Kacper')
    appWidget = AppWidget(words)
    appWidget.resize(800, 600)
    appWidget.show()
    sys.exit(app.exec_())
