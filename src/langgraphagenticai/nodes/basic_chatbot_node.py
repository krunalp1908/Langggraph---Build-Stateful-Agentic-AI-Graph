from src.langgraphagenticai.state.state import State

class BasicChatbotNode():
    """
    Basic Chatbot login implimentation
    """

    def __init__(self,model):
        self.llm = model

    def process(self,state:State)->dict:
        messages = state.get("messages", [])
        return {"messages": self.llm.invoke(messages)}