import os

from dotenv import load_dotenv

import openai

load_dotenv()
class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv('API_KEY')

    def get_response(self,user_input):
        response = openai.completions.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5,
        ).choices[0].text

        return response

if __name__ == "__main__":
    response =Chatbot().get_response("create a pyqt6 application for interating with openai")
    print(response)