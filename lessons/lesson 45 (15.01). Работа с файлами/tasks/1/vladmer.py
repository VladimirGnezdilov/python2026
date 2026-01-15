def print_attendees(path: str):

     with open(path,'r') as file:
      try:
      context=file.read()
      except FileNotFoundError:
       return "Нет файла со списком участников" 
      if context==""or "          ":
         return "Список участников пуст"
      for people in range context():
         return "people"
print(print_attendees)
