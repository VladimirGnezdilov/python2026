class Book:
   title=1984
   author="Dima Yakovlev"
   pages=384

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

Book25=Book("kirk","charlie",384)
Book25.open("kirk")
Book25.read("kirk","charlie")
Book25.close("kirk")
Book25.info("kirk","charlie",384)
