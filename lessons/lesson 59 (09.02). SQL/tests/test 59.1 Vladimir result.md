Вопросы с выбором варианта: 75/100%  
Вопросы с текстовыми ответами: 0/0%  
# Вопрос 1. Тема: Основы SQL
  
**1. Какая команда используется для извлечения всех записей из таблицы в SQL?**
  
Варианты ответов:
1) SELECT 1 FROM table_name;
2) ✅ SELECT * FROM table_name;
3) SELECT all FROM table_name;
4) SELECT FROM table_name;
  
### ИИ анализ
Команда `SELECT * FROM table_name;` является правильной. Символ `*` в SQL означает "все столбцы", что позволяет извлечь все записи из указанной таблицы. Другие варианты либо синтаксически неверны, либо выбирают конкретные данные, а не все записи. Понимание этого базового синтаксиса критически важно для работы с базами данных.

# Вопрос 2. Тема: Основы SQL
  
**2. Как ограничить выборку по конкретному условию?**
  
Варианты ответов:
1) SELECT * WHERE condition FROM table_name;
2) ✅ SELECT * FROM table_name WHERE condition;
3) SELECT * FROM table_name ORDER BY condition;
4) SELECT WHERE condition FROM table_name;
  
### ИИ анализ
Правильный ответ — `SELECT * FROM table_name WHERE condition;`. В SQL ключевое слово `WHERE` используется для фильтрации записей по условию и должно следовать после указания таблицы (`FROM table_name`). Варианты с неправильным порядком ключевых слов или использованием `ORDER BY` (для сортировки) являются ошибочными. Важно запомнить корректную структуру предложения SELECT.

# Вопрос 3. Тема: Основы SQL
  
**3. Как отсортировать результаты по убыванию значения в столбце age?**
  
Варианты ответов:
1) ✅ SELECT * FROM table_name ORDER BY age DESC;
2) SELECT * FROM table_name ORDER BY DESC age;
3) SELECT * ORDER BY age FROM table_name;
4) SELECT * FROM table_name WHERE age ORDER BY DESC;
  
### ИИ анализ
Для сортировки по убыванию используется конструкция `ORDER BY column_name DESC`. Правильный ответ — `SELECT * FROM table_name ORDER BY age DESC;`. Ключевое слово `DESC` должно стоять после имени столбца. Остальные варианты нарушают синтаксис SQL, помещая `DESC` не на свое место или используя `WHERE` без условия.

# Вопрос 4. Тема: Основы SQL
  
**4. Как выбрать записи, где age меньше 30 или salary больше 50000, и отсортировать их по name?**
  
Варианты ответов:
1) ❌ SELECT * FROM table_name WHERE age < 30 AND salary > 50000 ORDER BY name;
2) SELECT * FROM table_name ORDER BY age < 30 OR salary > 50000, name;
3) SELECT * FROM table_name WHERE age < 30 OR salary > 50000 ORDER BY name;
4) SELECT * FROM table_name WHERE age < 30 OR salary > 50000 name;
  
### ИИ анализ
Вы выбрали вариант с оператором `AND`, что означает, что должны выполняться оба условия одновременно. В вопросе же требуется логическое "ИЛИ" (age < 30 ИЛИ salary > 50000). Правильный ответ — вариант 3, где используется оператор `OR`. Также важно, что для сортировки используется отдельное ключевое слово `ORDER BY`. Обратите внимание на разницу между логическими операторами `AND` и `OR`.

# Вопрос 5. Тема: Основы SQL
  
**5. Как выбрать записи, где salary больше 50000 и age больше 25?**
  
Варианты ответов:
1) ✅ SELECT * FROM table_name WHERE salary > 30000 AND age > 25;
2) SELECT * FROM table_name WHERE salary > 30000 NOT age > 25;
3) SELECT * FROM table_name WHERE salary > 30000, age > 25;
4) SELECT * FROM table_name WHERE salary > 30000 OR age > 25;
  
### ИИ анализ
Вы верно выбрали вариант с оператором `AND`, который требует выполнения обоих условий. Однако в условии вопроса указано "salary больше 50000", а в вариантах ответа везде фигурирует "30000". При условии, что "30000" — это опечатка в вариантах ответа, а логика запроса верна, ваш выбор правильный. Для соединения нескольких условий в предложении `WHERE` используется оператор `AND`, а не запятая или `OR`.
