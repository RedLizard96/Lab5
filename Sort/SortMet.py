import re

# Список українського алфавіту
ukrainian_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

# Функція для отримання порядку символів за українським алфавітом
def ukrainian_key(word):
    return [ukrainian_alphabet.index(char.lower()) if char.lower() in ukrainian_alphabet else len(ukrainian_alphabet) for char in word]

# Функція для сортування слів
def custom_sort(words):
    # Фільтруємо та сортуємо українські слова
    ua_words = sorted([word for word in words if re.match(r'[а-яА-ЯіїєґІЇЄҐ]', word)], key=ukrainian_key)
    # Фільтруємо та сортуємо англійські слова
    en_words = sorted([word for word in words if re.match(r'[a-zA-Z]', word)], key=lambda s: s.lower())
    # Об'єднуємо результат
    return ua_words + en_words

# Функція для зчитування файлу та обробки даних
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            first_sentence = text.split('.')[0]  # Перше речення
            # Витягуємо всі слова без знаків пунктуації
            words = re.findall(r'\b\w+\b', text)  # Всі слова (ігноруючи пунктуацію)
            return first_sentence, words
    except FileNotFoundError:
        print("Помилка: Файл не знайдено!")
        return None, None
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return None, None

# Головна функція програми
def main():
    # Вказати ім'я текстового файлу
    filename = 'text.txt'
    
    # Зчитуємо дані з файлу
    sentence, words = read_file(filename)
    
    if sentence:
        print(f"Перше речення: {sentence.strip()}")
        print(f"Кількість слів: {len(words)}")
        
        # Використовуємо К. функцію для сортування
        sorted_words = custom_sort(words)
        
        # Виводимо відсортовані слова в дужках []
        print('Відсортовані слова:')
        print(f"{' '.join(sorted_words)}")  # Виводимо слова в дужках

if __name__ == "__main__":
    main()
