import sys

from PyQt6.QtWidgets import QMainWindow,QApplication,QTextEdit,QLineEdit,QPushButton


from dotenv import load_dotenv
import os


load_dotenv()

# for debugging purpose
os.environ['QT_DEBUG_PLUGINS'] = '1'
os.environ['QT_FATAL_WARNINGS']='1'

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']=os.getenv('QT_QPA_PLATFORM_PLUGIN_PATH')

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800,600)

        #Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,580,480)
        self.chat_area.setReadOnly(True)

        #input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,510,580,50)

        # button send
        self.button = QPushButton('send',self)
        self.button.setGeometry(610,510,100,50)

        self.show()


app= QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())