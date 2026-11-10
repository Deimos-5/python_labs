import argparse
import sys
import os

from src.lib.text import top_n 

def count_words(text: str) -> dict[str, int]:
    if not isinstance(text, str):
        raise TypeError("Ожидается строка")
    clean_chars = []
    for char in text.lower():
        if char.isalnum():
            clean_chars.append(char)
        else:
            clean_chars.append(' ')
    clean_text = ''.join(clean_chars)
    freq = {}
    for word in clean_text.split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def cat_file(input_path: str, number_lines: bool = False):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Файл не найден: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
            clean_line = line.rstrip('\n')
            if number_lines:
                print(f"{idx}: {clean_line}")
            else:
                print(clean_line)
def main():
    parser = argparse.ArgumentParser(description="Функции для работы с текстом")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    parser_stats = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
    parser_stats.add_argument("--input", dest="input_text", required=True, help="Текст для анализа (передаётся строкой в кавычках)")
    parser_stats.add_argument("--top", type=int, default=5, help="Количество топ-слов (по умолчанию 5)")

    parser_cat = subparsers.add_parser("cat", help="Вывод содержимого файла построчно")
    parser_cat.add_argument("--input", dest="input_path", required=True, help="Путь к входному файлу")
    parser_cat.add_argument("-n", dest="number_lines", action="store_true", help="Нумеровать строки")

    args = parser.parse_args()

    try:
        if args.command == "stats":
            freq = count_words(args.input_text)
            top_words = top_n(freq, args.top)
            
            print(f"Топ {args.top} слов:")
            for word, count in top_words:
                print(f"{word}: {count}")

        elif args.command == "cat":
            cat_file(args.input_path, args.number_lines)
        
        else:
            parser.print_help()

    except (FileNotFoundError, ValueError, TypeError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()