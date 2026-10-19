import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать файл. Кодировку можно указать через encoding."""
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительскую папку, если её нет."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: list[tuple | list],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """Записать строки одинаковой длины в CSV-файл."""
    expected_length = len(header) if header is not None else None

    for row in rows:
        if not isinstance(row, (tuple, list)):
            raise TypeError("строка CSV должна быть кортежем или списком")

        if expected_length is None:
            expected_length = len(row)
        elif len(row) != expected_length:
            raise ValueError("все строки CSV должны иметь одинаковую длину")

    file_path = Path(path)
    ensure_parent_dir(file_path)

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\n")

        if header is not None:
            writer.writerow(header)

        writer.writerows(rows)


txt = read_text("data/lab04/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV
print(txt)