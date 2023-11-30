from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_chatgpt_35_blogwriter = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_chatgpt_35_blogwriter)


class ChatGPTApi():
    def chatGPTResponse(self, messages):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature= 1.0,
            max_tokens= 3500,
            frequency_penalty= 0,
            presence_penalty= 0.6,
            messages=messages
        )
        return response.choices[0].message.content
