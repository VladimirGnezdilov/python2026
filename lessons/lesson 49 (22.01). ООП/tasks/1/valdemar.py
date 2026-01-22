from abc import ABC, abstractmethod
from typing import List
class NotificationChannel(ABC): 
    def __init__(self, sender_name: str):
        self.sender_name = sender_name
    def format_message(self, message: str) -> str:
        return f"[{self.sender_name}] {message}"
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
       print(f"EMAIL to <recipient>: <formatted_message> (from <sender_email>)")    
    @abstractmethod   
    def send(self, recipient: str, message: str) -> None:
       print(f"SMS to <recipient>: <formatted_message> (from <sender_phone>)")   
class EmailChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_email: str):
        super().__init__(sender_name)
        self.sender_email = sender_email

 
             
class SMSChannel(NotificationChannel):
   def __init__(self, sender_name: str, sender_phone: str):
        super().format_message(message)
        self.sender_phone = sender_phone

class NotificationService:
   # список получаем через инициализатор
      # self.channels = channels

   # метод notify_all
      # for channel in channels:
          # print('asdf')
