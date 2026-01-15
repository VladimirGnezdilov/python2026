def print_attendees(path: str):
    try:
     with open(path,'r') as file:
        context=file.read()
    except FileNotFoundError:
       return "Нет файла со списком участников" 
      if not names:
         return "Список участников пуст"
      for people in range context():
         return f"people"
print_attendees('../example.txt')
