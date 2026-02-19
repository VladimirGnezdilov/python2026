Вопросы с выбором варианта: 67/78%  
# Вопрос 1. Блок 3. Текстовый контент, ссылки, списки, изображения
  
### Содержание и вопросы

- Как сделать ссылку и какие бывают `href`?
- Чем `ul` отличается от `ol`?
- Зачем нужен `alt` у изображения?
- Как структурировать “карточку” проекта только HTML-ом?

### Материал (лаконично)

- Ссылка это тег `a`. Внутри должен быть текст, по которому понятно, куда ведет ссылка.
- `href` может быть:
  - обычным адресом сайта
  - якорем внутри страницы
  - `mailto:` для письма
- Списки:
  - `ul` когда порядок не важен, например “навыки”
  - `ol` когда это шаги, порядок важен
- Картинка это `img`. `alt` обязателен. Если картинка не загрузится, текст `alt` подскажет, что там должно быть.
- “Карточка” проекта это просто блок. Обычно внутри: заголовок, текст, ссылка.
  
Варианты ответов:
1) ✅ Прочитано
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 2. Практическое задание (Блок 3)
  
### Условия

Добавь контент в `index.html` пошагово:

1. В одной из секций добавь заголовок и под ним список.
2. Заполни список из 5 пунктов.
3. В секции с проектами создай контейнер для карточек.
4. Создай минимум 3 карточки. В каждой карточке сделай:
   - заголовок карточки
   - короткий текст-описание
   - ссылку
5. В шапке добавь изображение-аватар.
6. В подвале сделай блок контактов и добавь минимум 3 ссылки.
7. Проверь, что у всех `img` есть `alt`, а у всех `a` есть `href`.

Проверка:

- Все ссылки кликабельны.
- Все изображения имеют `alt`.

### Псевдокод решения

```text
IN SECTION_B
  CREATE LIST
    ADD LIST_ITEM (REPEAT 5 TIMES)

IN SECTION_C
  CREATE CARDS_CONTAINER
    REPEAT 3 TIMES
      CREATE CARD
        ADD CARD_TITLE
        ADD CARD_TEXT
        ADD CARD_LINK

IN HEADER
  ADD IMAGE_WITH_ALT

IN FOOTER
  CREATE CONTACTS_LIST
    ADD LINK_ITEM (REPEAT 3 TIMES)
END
```

### Если использовал ИИ, обязательные изменения вручную

- Замени один тип списка на другой (например, `ul` на `ol` или наоборот) и объясни почему это подходит.
- Добавь еще одну ссылку с другим типом `href` (например, `mailto:`).

---

**Вставь решение в комментарий ниже:**
  
### Ответ
<!DOCTYPE html>  
<html lang="ru">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Заголовок страницы</title>  
    <link rel="stylesheet" href="style.css">  
  
</head>  
<body>  
     <header class="header">  
      <h1>Главный заголовок страницы</h1>  
      <h2>Короткая строка описание</h2>  
     </header>  
      <img src="https://www.google.com/imgres?q=%D0%BA%D0%B0%D0%BA%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%B2%D0%B0%D1%82%D1%8C%20%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20%D0%B2%20%D1%85%D1%82%D0%BC%D0%BB&imgurl=https%3A%2F%2Fsitehere.ru%2Fwp-content%2Fuploads%2F2013%2F08%2Fkak-sdelat-vlozhennyui-spisok-html.jpg&imgrefurl=https%3A%2F%2Fsitehere.ru%2Furok-3-spiski&docid=CTCvgPYrBFJVyM&tbnid=bxAh4QQFO6xwWM&vet=12ahUKEwio-aSL2-WSAxXA2wIHHUeHKOYQM3oECB4QAA..i&w=780&h=410&hcb=2&ved=2ahUKEwio-aSL2-WSAxXA2wIHHUeHKOYQM3oECB4QAA" alt="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCvevZW734M4wZbtKh6gguCmvEM5aRLjYuSQ&s">  
     <main class="main">  
        <h2>Секция а</h2>  
        <h3>То, что должно находится в секции а</h3>  
        <ul>  
            <li>Первый пункт</li>  
            <li>Второй пункт</li>  
            <li>Третий пункт</li>  
            <li>Четвертый пункт</li>  
            <li>Шестой пункт</li>  
        </ul>  
      SECTION_B  
        <h2>Секция б(проекты)</h2>  
        <h3>То, что должно находится в секции б</h3>  
  
      SECTION_C  
        <h2>Секция с</h2>  
        <h3>То, что должно находится в секции с</h3>  
        <div class="card">  
            <h2 class="card-title">Название карточки</h2>  
            <p class="card-description">Краткое описание товара или услуги</p>  
            <a href="#" class="card-button">Подробнее</a>  
        </div>  
     </main>  
     <footer class="footer">  
       <h3>Подвал</h3>  
       <a href="https://github.com/VladimirGnezdilov/python2026/discussions/7"></a><a href="https://github.com/VladimirGnezdilov/python2026/discussions/7"></a><a href="https://github.com/VladimirGnezdilov/python2026/discussions/7"></a>  
     </footer>  
</body>  
</html>  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Какой тег используют обычной ссылки?
  
  
Варианты ответов:
1) `img`
2) `p`
3) `div`
4) `span`
5) ✅ `a`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Какой список лучше подходит для “навыки”, где порядок не важен?
  
  
Варианты ответов:
1) ✅ `ul`
2) `nav`
3) `ol`
4) `form`
5) `table`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Зачем нужен атрибут `alt` у изображения?
  
  
Варианты ответов:
1) Для изменения размера картинки
2) ✅ Для текстового описания картинки
3) Для создания отступов
4) Для подключения CSS
5) Для выравнивания текста
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 6. Какой `href` используют для ссылки на email?
  
  
Варианты ответов:
1) `mailto:`
2) `file:`
3) `css:`
4) `ftp:`
5) ❌ `http:`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 7. Что обычно должно быть внутри “карточки проекта”?
  
  
Варианты ответов:
1) Только `script` код
2) Только `meta` теги
3) ✅ Заголовок, текст, ссылка
4) Только картинка без текста
5) Только таблица с данными
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 8. Что проверяет в конце блока про контент?
  
  
Варианты ответов:
1) Что нет `section`
2) Что нет `footer`
3) Что `head` пустой
4) Что нет `main`
5) ✅ Что все ссылки имеют `href`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 9. Что важно для текста ссылки?
  
  
Варианты ответов:
1) Чтобы он был на одной букве
2) Чтобы он был скрыт стилями
3) Чтобы он был только цифрами
4) ✅ Чтобы он был понятным
5) Чтобы он был пустым
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
