# Лабараторная работа №6
# CLI‑утилиты с argparse (cat/grep‑lite + конвертеры)

# cli_text 
```  python
import argparse
from pathlib import Path
# Импортируем ваши функции из ЛР3/ЛР4 (проверьте точный путь, если он другой)
from src.lib.text import normalize, tokenize, count_freq, top_n

def cmd_stats(args):
    path = Path(args.input)
    if not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")

    text = path.read_text(encoding="utf-8")
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    
    # Если ваша функция top_n принимает n, передаем его. Если нет — просто срез.
    try:
        top = top_n(freq, n=args.top)
    except TypeError:
        top = top_n(freq)[:args.top]

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{args.top}:")
    for word, count in top:
        print(f"{word}: {count}")

def cmd_cat(args):
    path = Path(args.input)
    if not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")

    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if args.number:
                print(f"{i:>6}\t{line}", end="")
            else:
                print(line, end="")

def main():
    parser = argparse.ArgumentParser(
        prog="cli_text",
        description="CLI-утилиты для анализа текста (ЛР6)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Подкоманда stats
    p_stats = subparsers.add_parser("stats", help="Анализ частот слов")
    p_stats.add_argument("--input", required=True, help="Путь к txt файлу")
    p_stats.add_argument("--top", type=int, default=5, help="Количество топ-слов (по умолчанию 5)")
    p_stats.set_defaults(func=cmd_stats)

    # Подкоманда cat
    p_cat = subparsers.add_parser("cat", help="Вывод содержимого файла")
    p_cat.add_argument("--input", required=True, help="Путь к файлу")
    p_cat.add_argument("-n", action="store_true", dest="number", help="Нумеровать строки")
    p_cat.set_defaults(func=cmd_cat)

    args = parser.parse_args()
    
    try:
        args.func(args)
    except FileNotFoundError as e:
        parser.error(str(e))

if __name__ == "__main__":
    main()
```  

1. **Подкоманда cat**

Назначение: Вывод содержимого указанного файла в консоль
```  python
python -m src.lab06.cli_text cat --input data/lab06/samples/people.csv -n
```
Терминал

![](../../images/lab06/1.png)

Входные данные

![](../../images/lab06/ppl.csv.png)

2. **Подкоманда stats**

Назначение: Анализ частоты слов в текстовом файле

Входные данные

``` python
python -m src.lab06.cli_text stats --input data/lab06/samples/people.txt --top 5
```

![](../../images/lab06/sts.png)

**HELP**

![](../../images/lab06/help.png)