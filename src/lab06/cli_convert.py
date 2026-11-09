import argparse
from pathlib import Path
# Импортируем  функции из ЛР5
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def check_input(path_str):
    path = Path(path_str)
    if not path.is_file():
        raise FileNotFoundError(f"Входной файл не найден: {path}")
    return path

def cmd_json2csv(args):
    src = check_input(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True) # Создаем папку, если нет
    json_to_csv(str(src), str(out_path))

def cmd_csv2json(args):
    src = check_input(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    csv_to_json(str(src), str(out_path))

def cmd_csv2xlsx(args):
    src = check_input(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    csv_to_xlsx(str(src), str(out_path))

def main():
    parser = argparse.ArgumentParser(
        prog="cli_convert",
        description="CLI-конвертеры данных (ЛР6)"
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # json2csv
    p1 = subparsers.add_parser("json2csv", help="JSON -> CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV")
    p1.set_defaults(func=cmd_json2csv)

    # csv2json
    p2 = subparsers.add_parser("csv2json", help="CSV -> JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON")
    p2.set_defaults(func=cmd_csv2json)

    # csv2xlsx
    p3 = subparsers.add_parser("csv2xlsx", help="CSV -> XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX")
    p3.set_defaults(func=cmd_csv2xlsx)

    args = parser.parse_args()
    
    try:
        args.func(args)
    except FileNotFoundError as e:
        parser.error(str(e))
    except ValueError as e:
        parser.error(f"Ошибка данных: {e}")

if __name__ == "__main__":
    main()