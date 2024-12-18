# Advanced Wordle Game

Этот проект реализует улучшенную версию игры **Wordle** с использованием Python. Игра проверяет способность пользователя угадать слово за ограниченное количество попыток (6), давая обратную связь по каждой попытке: 
- **G** (Green) — буква на своём месте.
- **Y** (Yellow) — буква есть в слове, но не на своём месте.
- **B** (Black) — буквы нет в слове.

## Структура проекта

Проект организован с учётом принципов модульности, разделяя логику игры, валидацию слов, обработку пользовательского ввода и другие части на отдельные компоненты.

## Установка

### 1. Клонирование репозитория

Сначала клонируйте репозиторий:

```bash
git clone https://github.com/abdulovia/wordle.git
cd wordle
```

### 2. Установка зависимостей

Для работы проекта требуется установить зависимости. Для этого используйте pip:

```bash
pip install -r requirements.txt
```

### 3. Запуск игры
После установки зависимостей вы можете запустить игру с помощью команды:

```bash
python src/main.py
```

## Внесение изменений

Добавление новых слов: просто добавьте новые слова в файл resources/word_list.txt. Каждое слово должно быть на новой строке и состоять из 5 букв.

Дополнительные функции: Если вы хотите добавить новые особенности игры (например, новые режимы, улучшенные подсказки), это можно сделать, расширив существующие классы в папке game/.