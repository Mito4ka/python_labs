import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from src.lab04.io_txt_csv import ensure_parent_dir

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Преобразует CSV в XLSX с авто-шириной колонок."""
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    if csv_file.stat().st_size == 0:
        raise ValueError(f"Файл {csv_path} пуст")

    wb = Workbook()
    ws = wb.active
    ws.title = "Data"

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                ws.cell(row=row_idx, column=col_idx, value=value)

    # Авто-ширина колонок
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter # Получаем букву колонки (A, B, C...)
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    ensure_parent_dir(str(xlsx_file))
    wb.save(xlsx_file)

def csv_to_json(csv_path: str, json_path: str) -> None:
    