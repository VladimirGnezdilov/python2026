# Практическое задание 63.2 (CSS)

## Задание
Оформи страницу сделанную на занятии «Моя визитка» с помощью CSS.

### Требования
- Создай файл `styles.css`.
- Подключи его в `index.html` через тег `link` в `head`.
- Добавь стили:
  - Для `body`: шрифт без засечек, фон светлый, отступы страницы
  - Для `h1`: другой цвет текста и небольшой нижний отступ
  - Для `ul` и `li`: аккуратные отступы
  - Для ссылки `a`: убери подчеркивание и задай цвет, при наведении цвет меняется
  - Для картинки `img`: скругление углов и тонкая рамка

### Критерии проверки
- В HTML есть подключение `styles.css`.
- CSS реально применяется (видно изменение цветов, отступов, шрифта).
- Стили написаны без ошибок, страница не ломается.

### Пример (можно использовать как основу)
#### Подключение в HTML
```html
<link rel="stylesheet" href="styles.css" />
```

#### Пример `styles.css`
```css
body {
  font-family: Arial, sans-serif;
  background: #f5f7fb;
  margin: 0;
  padding: 24px;
  color: #1f2937;
}

h1 {
  color: #1d4ed8;
  margin: 0 0 12px 0;
}

h2 {
  margin: 18px 0 8px 0;
}

p {
  margin: 8px 0;
  line-height: 1.4;
}

ul {
  margin: 8px 0 12px 20px;
  padding: 0;
}

li {
  margin: 6px 0;
}

a {
  color: #0f766e;
  text-decoration: none;
}

a:hover {
  color: #115e59;
}

img {
  display: block;
  margin-top: 12px;
  border-radius: 10px;
  border: 1px solid #cbd5e1;
}
```
