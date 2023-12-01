import sys
from backend import Chatbot
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

        self.chatbot = Chatbot()

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
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>me:{user_input}</p>")
        self.input_field.clear()

        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color: #333333;background-color: #E9E9E9'>bot:{response}</p>")
        print("openai response recieved")


app= QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())