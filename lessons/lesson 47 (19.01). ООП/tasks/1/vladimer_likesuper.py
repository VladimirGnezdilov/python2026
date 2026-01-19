
class Book:
   def __init__ (self,title,author,pages):
      self.title=title
      self.author=author
      self.pages=pages

   def open(self,title):
      self.title=title
      print(f"Книга {title} открыта на первой странице")

   def read(self,title,author):
      self.title=title
      self.author=author
      print(f"Читаем книгу {title} автора {author}")
   def close(self,title):
      self.title=title
      print(f"Книга {title} закрыта")
   def info(self,title,author,pages):
      self.title=title
      self.author=author
      self.pages=pages
      print(f"{title} - {author}, {pages} стр.")

Book25=Book("Mao ","Zedong",384)
Book25.open("Mao")
Book25.read("Mao","Zedong")
Book25.close("Mao")
Book25.info("Mao","Zedong",384)
