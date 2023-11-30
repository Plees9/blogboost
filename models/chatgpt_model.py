from services.chatgpt_request import ChatGPTApi

class ChatGptModel:
    def __init__(self, messages):
        self.messages = messages
    
    def content(self):
        return ChatGPTApi().chatGPTResponse(self.messages)