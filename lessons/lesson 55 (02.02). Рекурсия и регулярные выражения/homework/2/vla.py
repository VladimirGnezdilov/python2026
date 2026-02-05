import re

def extract_dates(text):
    date_pateern = r'\b\d{2}\.\d{2}\.\d{4}\b'
    dates_found = re.findall(date_pattern, text)
    return dates_found
if __name__ == "__main__":
    text1 = "Сегодня 25.04.2024, а завтра будет 26.04.2024."
    dates1 = extract_dates(text1)
    print(f"Текст: {text1}")
    print(f"Найденные даты: {dates1}")
